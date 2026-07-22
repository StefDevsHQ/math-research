from __future__ import annotations

import itertools
import json
import tempfile
import unittest
from pathlib import Path

from nae3sat import (
    bounded_radius_collision,
    bounded_radius_summary,
    boundary_parity_summary,
    boundary_weight_summary,
    complete_five_plus_isolate,
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


class WholeInstanceCollisionTests(unittest.TestCase):
    def assert_satisfiability_collision(self, left, right, summary):
        self.assertEqual(summary(left), summary(right))
        self.assertNotEqual(
            solution_summary(left)["satisfiable"],
            solution_summary(right)["satisfiable"],
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


class AtlasTests(unittest.TestCase):
    def test_record_and_committed_bytes(self):
        record = summary_collision_record()
        self.assertTrue(verify_summary_collision_record(record))
        self.assertEqual(len(record["collisions"]), 10)
        self.assertEqual(
            ATLAS.read_bytes(),
            summary_collision_bytes(),
        )

    def test_record_round_trip(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "atlas.json"
            path.write_bytes(summary_collision_bytes())
            value = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(verify_summary_collision_record(value))


if __name__ == "__main__":
    unittest.main()
