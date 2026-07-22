from __future__ import annotations

import copy
import hashlib
import itertools
import json
import unittest
from pathlib import Path

from nae3sat.model import normalize_instance
from nae3sat.obstructions import complete_three_graph, fano_plane
from nae3sat.pcrnf import (
    build_pcrnf,
    compare_pcrnf_profile,
    pcrnf_completion_mask,
    satisfies_pcrnf,
    transition_pcrnf,
    traverse_pcrnf,
    unoriented_pcrnf_key,
)
from nae3sat.pcrnf_atlas import (
    incompleteness_witness,
    orientation_counterexample,
    pcrnf_attack_bytes,
    pcrnf_attack_record,
)
from nae3sat.pcrnf_validation import verify_pcrnf_attack_record
from nae3sat.semantic_merging import fan_bad_ordering, fan_good_ordering, fan_instance

ROOT = Path(__file__).parents[1]
RECORD = ROOT / "pcrnf" / "vs08-pcrnf-attack.json"


def _reference_mask(instance, ordering, prefix):
    level = len(prefix)
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
    return mask


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


class OrientationTests(unittest.TestCase):
    def test_unoriented_component_normalization_is_unsound(self):
        instance = normalize_instance(3, ((0, 1, 2),))
        ordering = (0, 1, 2)
        left = build_pcrnf(instance, ordering, (0, 0))
        right = build_pcrnf(instance, ordering, (1, 1))
        self.assertEqual(unoriented_pcrnf_key(left), unoriented_pcrnf_key(right))
        self.assertNotEqual(left, right)
        self.assertEqual(pcrnf_completion_mask(left, (2,)), 2)
        self.assertEqual(pcrnf_completion_mask(right, (2,)), 1)
        self.assertEqual(orientation_counterexample()["status"], "DISPROVED")

    def test_recorded_orientation_decodes_original_labelled_colours(self):
        instance = normalize_instance(3, ((0, 1, 2),))
        residual = build_pcrnf(instance, (0, 1, 2), (1, 1))
        self.assertFalse(satisfies_pcrnf(residual, {2: 1}))
        self.assertTrue(satisfies_pcrnf(residual, {2: 0}))


class ExactnessTests(unittest.TestCase):
    def test_direct_and_incremental_residualization_agree(self):
        instances = (
            normalize_instance(4, ((0, 1, 2), (0, 1, 3))),
            complete_three_graph(5),
            fano_plane(),
        )
        for instance in instances:
            ordering = tuple(range(instance.n))
            levels = traverse_pcrnf(instance, ordering)
            for level in range(instance.n + 1):
                direct = {
                    build_pcrnf(instance, ordering, prefix)
                    for prefix in itertools.product((0, 1), repeat=level)
                }
                self.assertEqual(set(levels[level]), direct)

    def test_named_controls_match_bruteforce_completion_masks(self):
        instances = (
            normalize_instance(4, ((0, 1, 2), (0, 1, 3))),
            complete_three_graph(5),
            fano_plane(),
        )
        for instance in instances:
            ordering = tuple(range(instance.n))
            for level in range(instance.n + 1):
                for prefix in itertools.product((0, 1), repeat=level):
                    residual = build_pcrnf(instance, ordering, prefix)
                    self.assertEqual(
                        pcrnf_completion_mask(residual, ordering[level:]),
                        _reference_mask(instance, ordering, prefix),
                    )

    def test_unsatisfiable_controls_end_in_one_contradictory_state(self):
        for instance in (complete_three_graph(5), fano_plane()):
            levels = traverse_pcrnf(instance, tuple(range(instance.n)))
            final = levels[-1]
            self.assertEqual(len(final), 1)
            self.assertTrue(final[0].contradiction)


class QuotientTests(unittest.TestCase):
    def test_exhaustive_agreement_through_four_vertices(self):
        for n in range(5):
            triples = tuple(itertools.combinations(range(n), 3))
            for mask in range(1 << len(triples)):
                instance = normalize_instance(
                    n,
                    (
                        edge
                        for index, edge in enumerate(triples)
                        if mask & (1 << index)
                    ),
                )
                for ordering in itertools.permutations(range(n)):
                    comparison = compare_pcrnf_profile(instance, ordering)
                    self.assertTrue(
                        all(
                            level.incompleteness_excess == 0
                            for level in comparison.levels
                        )
                    )

    def test_first_strict_incompleteness_witness(self):
        record = incompleteness_witness()
        self.assertEqual(record["completion_mask"], 40)
        self.assertNotEqual(record["left_pcrnf"], record["right_pcrnf"])
        self.assertEqual(record["status"], "COMPUTATIONAL / CHECKED")

    def test_fan_ordering_separation(self):
        for edge_count in range(1, 7):
            instance = fan_instance(edge_count)
            bad = traverse_pcrnf(instance, fan_bad_ordering(edge_count))
            good = traverse_pcrnf(instance, fan_good_ordering(edge_count))
            self.assertEqual(
                max(len(level) for level in bad),
                (1 << (edge_count + 1)) - 1,
            )
            self.assertLessEqual(max(len(level) for level in good), 5)


class RecordTests(unittest.TestCase):
    def test_record_envelope_and_committed_bytes(self):
        record = pcrnf_attack_record()
        self.assertTrue(verify_pcrnf_attack_record(record))
        self.assertEqual(RECORD.read_bytes(), pcrnf_attack_bytes())

    def test_route_decision_is_retracted_not_disproved(self):
        decision = pcrnf_attack_record()["route_decision"]
        self.assertEqual(decision["candidate"], "NAE-016")
        self.assertEqual(decision["status"], "RETRACTED")

    def test_strict_verifier_rejects_redigested_schema_changes(self):
        original = pcrnf_attack_record()
        for mutation in ("wrong-format", "unknown-field"):
            record = copy.deepcopy(original)
            if mutation == "wrong-format":
                record["format"] = "wrong-format"
            else:
                record["unexpected"] = True
            _redigest(record)
            self.assertFalse(verify_pcrnf_attack_record(record))


if __name__ == "__main__":
    unittest.main()
