from __future__ import annotations

import itertools
import json
import tempfile
import unittest
from pathlib import Path

from nae3sat import (
    anchored_inequality_instance,
    bounded_radius_collision,
    bounded_radius_summary,
    boundary_parity_summary,
    boundary_weight_summary,
    characteristic_polynomial,
    complete_five_plus_isolate,
    cycle_union,
    degree_collision_satisfiable,
    degree_collision_unsatisfiable,
    degree_sequence_summary,
    edge_intersection_summary,
    exact_boundary_summary,
    exact_completion_mask,
    fano_local_obstruction,
    graph_is_bipartite,
    incidence_gram_spectrum_summary,
    labelled_instances,
    local_consistency_star,
    pair_codegree_collision_satisfiable,
    pair_codegree_multiset_summary,
    parity_summary,
    proper_induced_satisfiability_summary,
    root_gac_summary,
    second_moment_summary,
    solution_summary,
    star_six,
    summary_collision_bytes,
    summary_collision_record,
    verify_summary_collision_record,
)

ROOT = Path(__file__).parents[1]
ATLAS = ROOT / "summary-collisions" / "vs06-summary-collisions.json"


def _reference_solutions(instance):
    return tuple(
        assignment
        for assignment in itertools.product((0, 1), repeat=instance.n)
        if all(
            not (assignment[left] == assignment[middle] == assignment[right])
            for left, middle, right in instance.edges
        )
    )


def _conditioned_anchor_satisfiable(graph) -> bool:
    instance = anchored_inequality_instance(graph)
    for tail in itertools.product((0, 1), repeat=graph[0]):
        assignment = (0, 1, *tail)
        if all(
            not (assignment[left] == assignment[middle] == assignment[right])
            for left, middle, right in instance.edges
        ):
            return True
    return False


class WholeInstanceCollisionTests(unittest.TestCase):
    def assert_satisfiability_collision(self, left, right, summary):
        self.assertEqual(summary(left), summary(right))
        left_reference = _reference_solutions(left)
        right_reference = _reference_solutions(right)
        self.assertNotEqual(bool(left_reference), bool(right_reference))

        left_production = solution_summary(left)
        right_production = solution_summary(right)
        self.assertEqual(left_production["satisfiable"], bool(left_reference))
        self.assertEqual(right_production["satisfiable"], bool(right_reference))
        self.assertEqual(left_production["solution_count"], len(left_reference))
        self.assertEqual(right_production["solution_count"], len(right_reference))
        self.assertEqual(
            left_production["least_witness"],
            None if not left_reference else list(left_reference[0]),
        )
        self.assertEqual(
            right_production["least_witness"],
            None if not right_reference else list(right_reference[0]),
        )

    def test_degree_sequence_collision(self):
        self.assert_satisfiability_collision(
            degree_collision_satisfiable(),
            degree_collision_unsatisfiable(),
            degree_sequence_summary,
        )

    def test_pair_codegree_multiset_collision(self):
        self.assert_satisfiability_collision(
            pair_codegree_collision_satisfiable(),
            degree_collision_unsatisfiable(),
            pair_codegree_multiset_summary,
        )

    def test_shared_star_complete_collisions(self):
        star = star_six()
        complete = complete_five_plus_isolate()
        for summary in (
            edge_intersection_summary,
            parity_summary,
            second_moment_summary,
            incidence_gram_spectrum_summary,
        ):
            with self.subTest(summary=summary.__name__):
                self.assert_satisfiability_collision(star, complete, summary)

    def test_local_consistency_collisions(self):
        star = local_consistency_star()
        fano = fano_local_obstruction()
        self.assert_satisfiability_collision(star, fano, root_gac_summary)
        self.assert_satisfiability_collision(
            star,
            fano,
            lambda instance: proper_induced_satisfiability_summary(
                instance,
                maximum_size=instance.n - 1,
            ),
        )
        self.assertTrue(
            all(
                proper_induced_satisfiability_summary(
                    fano,
                    maximum_size=fano.n - 1,
                )
            )
        )


class AlgebraicSummaryTests(unittest.TestCase):
    def test_characteristic_polynomial_known_matrices(self):
        self.assertEqual(characteristic_polynomial(()), (1,))
        self.assertEqual(characteristic_polynomial(((2,),)), (1, -2))
        self.assertEqual(
            characteristic_polynomial(((1, 0), (0, 1))),
            (1, -2, 1),
        )
        self.assertEqual(
            characteristic_polynomial(((0, 1), (1, 0))),
            (1, 0, -1),
        )


class PrefixCollisionTests(unittest.TestCase):
    def test_boundary_weight_collision(self):
        from nae3sat import normalize_instance

        instance = normalize_instance(4, ((0, 1, 2), (0, 1, 3)))
        ordering = (3, 2, 1, 0)
        left = (0, 0, 1)
        right = (0, 1, 0)
        self.assertEqual(
            boundary_weight_summary(instance, ordering, left),
            boundary_weight_summary(instance, ordering, right),
        )
        self.assertNotEqual(
            exact_completion_mask(instance, ordering, left),
            exact_completion_mask(instance, ordering, right),
        )

    def test_boundary_parity_collision(self):
        from nae3sat import normalize_instance

        instance = normalize_instance(3, ((0, 1, 2),))
        ordering = (0, 1, 2)
        left = (0, 0)
        right = (1, 1)
        self.assertEqual(
            boundary_parity_summary(instance, ordering, left),
            boundary_parity_summary(instance, ordering, right),
        )
        self.assertNotEqual(
            exact_completion_mask(instance, ordering, left),
            exact_completion_mask(instance, ordering, right),
        )

    def test_exact_boundary_assignment_is_a_complete_control_through_four(self):
        checked = 0
        for n in range(5):
            for instance in labelled_instances(n):
                for ordering in itertools.permutations(range(n)):
                    for level in range(n + 1):
                        seen = {}
                        for prefix in itertools.product((0, 1), repeat=level):
                            summary = exact_boundary_summary(
                                instance,
                                ordering,
                                prefix,
                            )
                            semantics = exact_completion_mask(
                                instance,
                                ordering,
                                prefix,
                            )
                            if summary in seen:
                                self.assertEqual(seen[summary], semantics)
                            else:
                                seen[summary] = semantics
                            checked += 1
        self.assertGreater(checked, 0)


class BoundedRadiusFamilyTests(unittest.TestCase):
    def test_samples_have_equal_local_views_and_opposite_global_parity(self):
        for radius in (1, 2):
            unsatisfiable, satisfiable = bounded_radius_collision(radius)
            self.assertEqual(
                bounded_radius_summary(unsatisfiable, radius),
                bounded_radius_summary(satisfiable, radius),
            )
            self.assertFalse(graph_is_bipartite(unsatisfiable))
            self.assertTrue(graph_is_bipartite(satisfiable))

    def test_constructive_lengths(self):
        for radius in range(1, 8):
            unsatisfiable, satisfiable = bounded_radius_collision(radius)
            self.assertEqual(unsatisfiable[0], 4 * radius + 6)
            self.assertEqual(satisfiable[0], 4 * radius + 6)
            self.assertEqual(len(unsatisfiable[1]), 4 * radius + 6)
            self.assertEqual(len(satisfiable[1]), 4 * radius + 6)

    def test_anchored_reduction_in_both_directions(self):
        controls = (
            cycle_union((3,)),
            cycle_union((4,)),
            *bounded_radius_collision(1),
        )
        for graph in controls:
            with self.subTest(graph=graph):
                self.assertEqual(
                    _conditioned_anchor_satisfiable(graph),
                    graph_is_bipartite(graph),
                )


class AtlasTests(unittest.TestCase):
    def test_record_and_committed_bytes(self):
        record = summary_collision_record()
        self.assertTrue(verify_summary_collision_record(record))
        self.assertEqual(len(record["collisions"]), 10)
        self.assertEqual(
            ATLAS.read_bytes(),
            summary_collision_bytes(),
        )

    def test_committed_semantics_match_independent_enumeration(self):
        record = json.loads(ATLAS.read_text(encoding="utf-8"))
        for collision in record["collisions"]:
            if "left" not in collision:
                continue
            for side in ("left", "right"):
                item = collision[side]
                from nae3sat import normalize_instance

                instance = normalize_instance(item["n"], item["edges"])
                reference = _reference_solutions(instance)
                self.assertEqual(item["semantics"]["satisfiable"], bool(reference))
                self.assertEqual(item["semantics"]["solution_count"], len(reference))
                self.assertEqual(
                    item["semantics"]["least_witness"],
                    None if not reference else list(reference[0]),
                )

    def test_record_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "atlas.json"
            path.write_bytes(summary_collision_bytes())
            value = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(verify_summary_collision_record(value))


if __name__ == "__main__":
    unittest.main()
