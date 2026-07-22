from __future__ import annotations

import copy
import hashlib
import itertools
import json
import unittest
from pathlib import Path

from nae3sat.model import normalize_instance
from nae3sat.semantic_merging import (
    fan_bad_ordering,
    fan_good_ordering,
    fan_instance,
    measure_semantic_merging_level,
    measure_semantic_merging_profile,
)
from nae3sat.semantic_merging_atlas import (
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

        level = measure_semantic_merging_level(instance, ordering, 3)
        self.assertEqual(level.live_prefix_count, 8)
        self.assertEqual(level.dead_prefix_count, 0)
        self.assertEqual(level.live_semantic_class_count, 3)
        self.assertEqual(level.live_prefix_component_orbit_count, 4)
        self.assertEqual(level.live_semantic_component_orbit_count, 2)
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
                self.assertEqual(
                    measurement.live_prefix_component_orbit_count,
                    1 << edge_count,
                )
                self.assertEqual(
                    measurement.live_semantic_component_orbit_count,
                    1 << edge_count,
                )
                self.assertEqual(
                    measurement.live_boundary_state_count,
                    1 << (edge_count + 1),
                )
                self.assertEqual(
                    measurement.exact_cross_orbit_merge_excess,
                    0,
                )

    def test_interleaved_ordering_has_constant_width_and_class_bound(self):
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
                self.assertLessEqual(profile.peak_live_semantic_classes, 5)


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
