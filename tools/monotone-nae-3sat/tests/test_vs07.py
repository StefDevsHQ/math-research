from __future__ import annotations

import copy
import hashlib
import itertools
import json
import unittest
from pathlib import Path

from nae3sat.model import incidence_components, normalize_instance
from nae3sat.obstructions import complete_three_graph, fano_plane
from nae3sat.semantic_merging import (
    fan_bad_ordering,
    fan_good_ordering,
    fan_instance,
    measure_semantic_merging_level,
    measure_semantic_merging_profile,
)
from nae3sat.semantic_merging_record import (
    semantic_merging_bytes,
    semantic_merging_record,
)
from nae3sat.semantic_merging_validation import (
    verify_semantic_merging_record,
)

ROOT = Path(__file__).parents[1]
RECORD = ROOT / "semantic-merging" / "vs07-semantic-merging.json"


def _reference_masks(instance, ordering, level):
    result = []
    for prefix in itertools.product((0, 1), repeat=level):
        mask = 0
        for completion_index, completion in enumerate(
            itertools.product((0, 1), repeat=instance.n - level)
        ):
            ordered = prefix + completion
            colours = [0] * instance.n
            for position, vertex in enumerate(ordering):
                colours[vertex] = ordered[position]
            if all(
                not (colours[left] == colours[middle] == colours[right])
                for left, middle, right in instance.edges
            ):
                mask |= 1 << completion_index
        result.append(mask)
    return tuple(result)


def _reference_component_actions(instance, ordering, level):
    positions = {vertex: index for index, vertex in enumerate(ordering)}
    generators = []
    for component in incidence_components(instance):
        prefix_xor = 0
        suffix_xor = 0
        for vertex in component:
            position = positions[vertex]
            if position < level:
                prefix_xor ^= 1 << (level - 1 - position)
            else:
                suffix_xor ^= 1 << (instance.n - 1 - position)
        generators.append((prefix_xor, suffix_xor))

    actions = {(0, 0)}
    for generator in generators:
        actions = actions | {
            (prefix ^ generator[0], suffix ^ generator[1])
            for prefix, suffix in actions
        }
    return tuple(sorted(actions))


def _reference_permute_mask(mask, suffix_xor):
    return sum(
        1 << (completion ^ suffix_xor)
        for completion in range(mask.bit_length())
        if mask & (1 << completion)
    )


def _reference_orbit_counts(instance, ordering, level, masks):
    actions = _reference_component_actions(instance, ordering, level)
    live_prefixes = tuple(
        prefix for prefix, mask in enumerate(masks) if mask != 0
    )
    prefix_representatives = {
        prefix: min(prefix ^ prefix_xor for prefix_xor, _ in actions)
        for prefix in live_prefixes
    }
    live_masks = {masks[prefix] for prefix in live_prefixes}
    semantic_representatives = {
        mask: min(
            _reference_permute_mask(mask, suffix_xor)
            for _, suffix_xor in actions
        )
        for mask in live_masks
    }
    return (
        len(set(prefix_representatives.values())),
        len(set(semantic_representatives.values())),
    )


def _redigest(record):
    payload = {
        key: value for key, value in record.items() if key != "payload_sha256"
    }
    encoded = json.dumps(
        payload,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    record["payload_sha256"] = hashlib.sha256(encoded).hexdigest()


class SemanticMergingWitnessTests(unittest.TestCase):
    def test_first_all_live_cross_orbit_merge(self):
        instance = normalize_instance(
            4,
            ((0, 1, 2), (0, 1, 3)),
        )
        ordering = (0, 2, 3, 1)
        masks = _reference_masks(instance, ordering, 3)
        self.assertEqual(masks, (2, 2, 2, 3, 3, 1, 1, 1))
        self.assertTrue(all(mask != 0 for mask in masks))

        prefix_orbits, semantic_orbits = _reference_orbit_counts(
            instance,
            ordering,
            3,
            masks,
        )
        self.assertEqual(prefix_orbits, 4)
        self.assertEqual(semantic_orbits, 2)

        level = measure_semantic_merging_level(instance, ordering, 3)
        self.assertEqual(level.live_prefix_count, 8)
        self.assertEqual(level.dead_prefix_count, 0)
        self.assertEqual(level.live_semantic_class_count, 3)
        self.assertEqual(level.live_prefix_component_orbit_count, prefix_orbits)
        self.assertEqual(
            level.live_semantic_component_orbit_count,
            semantic_orbits,
        )
        self.assertEqual(level.exact_cross_orbit_merge_class_count, 2)
        self.assertEqual(level.exact_cross_orbit_merge_excess, 4)
        self.assertEqual(level.orbit_normalized_merge_excess, 2)
        self.assertEqual(level.live_boundary_state_count, 8)

    def test_dead_and_live_counts_partition_every_level(self):
        instance = normalize_instance(
            5,
            ((0, 1, 2), (0, 1, 3), (0, 1, 4)),
        )
        profile = measure_semantic_merging_profile(
            instance,
            (0, 2, 3, 4, 1),
        )
        for level in profile.levels:
            self.assertEqual(
                level.prefix_count,
                level.live_prefix_count + level.dead_prefix_count,
            )
            self.assertEqual(
                level.semantic_class_count,
                level.live_semantic_class_count + level.dead_class_count,
            )
            self.assertLessEqual(
                level.live_semantic_class_count,
                level.live_boundary_state_count,
            )

    def test_unsatisfiable_controls_are_pure_dead_collapse(self):
        controls = (complete_three_graph(5), fano_plane())
        for instance in controls:
            with self.subTest(n=instance.n, edges=len(instance.edges)):
                profile = measure_semantic_merging_profile(
                    instance,
                    tuple(range(instance.n)),
                )
                for level in profile.levels:
                    self.assertEqual(level.live_prefix_count, 0)
                    self.assertEqual(
                        level.dead_prefix_count,
                        level.prefix_count,
                    )
                    self.assertEqual(level.semantic_class_count, 1)
                    self.assertEqual(level.live_semantic_class_count, 0)
                    self.assertEqual(level.dead_class_count, 1)
                    self.assertEqual(
                        level.live_prefix_component_orbit_count,
                        0,
                    )
                    self.assertEqual(
                        level.live_semantic_component_orbit_count,
                        0,
                    )
                    self.assertEqual(
                        level.exact_cross_orbit_merge_excess,
                        0,
                    )
                    self.assertEqual(level.live_boundary_state_count, 0)
                    self.assertEqual(
                        level.dead_boundary_state_count,
                        level.processed_valid_boundary_state_count,
                    )


class FanFamilyTests(unittest.TestCase):
    def test_bad_ordering_exact_formulas(self):
        for edge_count in range(1, 7):
            with self.subTest(edge_count=edge_count):
                instance = fan_instance(edge_count)
                ordering = fan_bad_ordering(edge_count)
                level = edge_count + 1
                reference = _reference_masks(instance, ordering, level)
                measurement = measure_semantic_merging_level(
                    instance,
                    ordering,
                    level,
                )
                self.assertTrue(all(mask != 0 for mask in reference))
                self.assertEqual(
                    len(set(reference)),
                    (1 << (edge_count + 1)) - 1,
                )
                prefix_orbits, semantic_orbits = _reference_orbit_counts(
                    instance,
                    ordering,
                    level,
                    reference,
                )
                self.assertEqual(prefix_orbits, 1 << edge_count)
                self.assertEqual(semantic_orbits, 1 << edge_count)
                self.assertEqual(
                    measurement.live_prefix_component_orbit_count,
                    prefix_orbits,
                )
                self.assertEqual(
                    measurement.live_semantic_component_orbit_count,
                    semantic_orbits,
                )
                self.assertEqual(
                    measurement.live_boundary_state_count,
                    1 << (edge_count + 1),
                )
                self.assertEqual(
                    measurement.exact_cross_orbit_merge_excess,
                    0,
                )

    def test_interleaved_ordering_has_constant_width_and_sharp_live_bound(self):
        for edge_count in range(1, 9):
            with self.subTest(edge_count=edge_count):
                profile = measure_semantic_merging_profile(
                    fan_instance(edge_count),
                    fan_good_ordering(edge_count),
                )
                self.assertLessEqual(
                    max(level.boundary_width for level in profile.levels),
                    2,
                )
                self.assertLessEqual(profile.peak_live_semantic_classes, 4)


class RecordTests(unittest.TestCase):
    def test_record_envelope_and_committed_bytes(self):
        record = semantic_merging_record()
        self.assertTrue(verify_semantic_merging_record(record))
        self.assertEqual(RECORD.read_bytes(), semantic_merging_bytes())

    def test_exhaustive_profile_counts(self):
        record = semantic_merging_record()
        rows = record["exhaustive_domain"]["rows"]
        self.assertEqual(
            [row["profiles"] for row in rows],
            [1, 1, 2, 12, 384],
        )
        self.assertGreater(
            rows[4]["all_live_levels_with_cross_orbit_merge"],
            0,
        )

    def test_record_good_ordering_bound_is_conservative_but_valid(self):
        theorem = semantic_merging_record()["fan_family"][
            "good_ordering_theorem"
        ]
        self.assertEqual(theorem["maximum_boundary_width"], 2)
        self.assertEqual(theorem["maximum_live_exact_classes"], 5)
        self.assertLessEqual(
            max(
                sample["good_peak_live_semantic_classes"]
                for sample in semantic_merging_record()["fan_family"]["samples"]
            ),
            4,
        )

    def test_strict_verifier_rejects_redigested_schema_changes(self):
        original = semantic_merging_record()
        for mutation in ("wrong-format", "unknown-field"):
            record = copy.deepcopy(original)
            if mutation == "wrong-format":
                record["format"] = "wrong-format"
            else:
                record["unexpected"] = True
            _redigest(record)
            self.assertFalse(verify_semantic_merging_record(record))

    def test_malformed_digests_are_rejected(self):
        for digest in (None, 0, "", "0" * 63, "G" * 64, "A" * 64):
            record = semantic_merging_record()
            record["payload_sha256"] = digest
            self.assertFalse(verify_semantic_merging_record(record))


if __name__ == "__main__":
    unittest.main()
