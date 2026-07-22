from __future__ import annotations

import itertools
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from nae3sat import (
    Graph2,
    ValidationError,
    XorSystem,
    boundary_width,
    build_exact_profile,
    calibration_bytes,
    calibration_record,
    color_incidence_forest,
    is_incidence_forest,
    labelled_graphs,
    labelled_instances,
    labelled_xor_systems,
    minimum_boundary_width,
    normalize_graph2,
    normalize_instance,
    normalize_xor_system,
    processed_boundary,
    solve_exact,
    solve_graph2,
    solve_xor,
    verify_calibration_record,
    verify_coloring,
    verify_graph2_coloring,
    verify_xor_assignment,
    vertex_occurrences,
)

ROOT = Path(__file__).parents[1]


def _reference_graph(graph: Graph2):
    solutions = tuple(
        coloring
        for coloring in itertools.product((0, 1), repeat=graph.n)
        if all(coloring[u] != coloring[v] for u, v in graph.edges)
    )
    return solutions


def _reference_xor(system: XorSystem):
    solutions = tuple(
        assignment
        for assignment in itertools.product((0, 1), repeat=system.n)
        if all(
            sum(assignment[index] for index in range(system.n) if mask & (1 << index)) % 2 == rhs
            for mask, rhs in system.equations
        )
    )
    return solutions


class GraphControlTests(unittest.TestCase):
    def test_validation_and_normalization(self):
        self.assertEqual(normalize_graph2(3, [(2, 0), (0, 2)]), Graph2(3, ((0, 2),)))
        for bad in (-1, True, 2.0):
            with self.assertRaises(ValidationError):
                normalize_graph2(bad, [])
        with self.assertRaises(ValidationError):
            Graph2(2, ((0, 0),))
        with self.assertRaises(ValidationError):
            normalize_graph2(2, [(0, 2)])
        with self.assertRaises(ValidationError):
            solve_graph2(object())

    def test_complete_labelled_graph_domain_through_five(self):
        total = bipartite = non_bipartite = 0
        expected_by_n = {
            0: (1, 1, 0),
            1: (1, 1, 0),
            2: (2, 2, 0),
            3: (8, 7, 1),
            4: (64, 41, 23),
            5: (1024, 376, 648),
        }
        for n in range(6):
            row_total = row_bipartite = 0
            for graph in labelled_graphs(n):
                solutions = _reference_graph(graph)
                result = solve_graph2(graph)
                self.assertEqual(result.bipartite, bool(solutions))
                self.assertEqual(result.solution_count, len(solutions))
                self.assertEqual(result.witness, solutions[0] if solutions else None)
                if result.witness is not None:
                    self.assertTrue(verify_graph2_coloring(graph, result.witness))
                row_total += 1
                row_bipartite += result.bipartite
            self.assertEqual((row_total, row_bipartite, row_total - row_bipartite), expected_by_n[n])
            total += row_total
            bipartite += row_bipartite
            non_bipartite += row_total - row_bipartite
        self.assertEqual((total, bipartite, non_bipartite), (1100, 428, 672))

    def test_odd_cycle_and_disconnected_conflict(self):
        triangle = Graph2(3, ((0, 1), (0, 2), (1, 2)))
        result = solve_graph2(triangle)
        self.assertFalse(result.bipartite)
        self.assertIn(result.conflict_edge, triangle.edges)
        disconnected = Graph2(5, ((0, 1), (0, 2), (1, 2), (3, 4)))
        self.assertFalse(solve_graph2(disconnected).bipartite)


class XorControlTests(unittest.TestCase):
    def test_validation_and_normalization(self):
        self.assertEqual(
            normalize_xor_system(3, [([0, 2], 1), (5, 1)]),
            XorSystem(3, ((5, 1),)),
        )
        with self.assertRaises(ValidationError):
            normalize_xor_system(2, [([], 0)])
        with self.assertRaises(ValidationError):
            normalize_xor_system(2, [([0, 0], 0)])
        with self.assertRaises(ValidationError):
            XorSystem(2, ((0, 1),))
        with self.assertRaises(ValidationError):
            solve_xor(object())

    def test_complete_labelled_xor_domain_through_three(self):
        expected_by_n = {
            0: (1, 1, 0),
            1: (4, 3, 1),
            2: (64, 23, 41),
            3: (16384, 863, 15521),
        }
        total = consistent = inconsistent = 0
        for n in range(4):
            row_total = row_consistent = 0
            for system in labelled_xor_systems(n):
                solutions = _reference_xor(system)
                result = solve_xor(system)
                self.assertEqual(result.consistent, bool(solutions))
                self.assertEqual(result.solution_count, len(solutions))
                self.assertEqual(result.witness, solutions[0] if solutions else None)
                if result.witness is not None:
                    self.assertTrue(verify_xor_assignment(system, result.witness))
                    self.assertEqual(result.free_variables, system.n - result.rank)
                row_total += 1
                row_consistent += result.consistent
            self.assertEqual((row_total, row_consistent, row_total - row_consistent), expected_by_n[n])
            total += row_total
            consistent += row_consistent
            inconsistent += row_total - row_consistent
        self.assertEqual((total, consistent, inconsistent), (16453, 890, 15563))

    def test_dependent_and_inconsistent_controls(self):
        dependent = XorSystem(3, ((3, 1), (5, 0), (6, 1)))
        result = solve_xor(dependent)
        self.assertTrue(result.consistent)
        self.assertEqual((result.rank, result.solution_count), (2, 2))
        contradictory = XorSystem(2, ((3, 0), (3, 1)))
        self.assertFalse(solve_xor(contradictory).consistent)


class NAEControlTests(unittest.TestCase):
    def test_complete_filtered_domain_through_five(self):
        forest_counts = [1, 1, 1, 2, 5, 26]
        occurrence_counts = [1, 1, 1, 2, 16, 323]
        for n in range(6):
            forests = occurrence = 0
            for instance in labelled_instances(n):
                ordering = tuple(range(n))
                profile = build_exact_profile(instance, ordering)
                oracle = solve_exact(instance)
                self.assertEqual(profile.satisfiable, oracle.satisfiable)
                for level in range(n + 1):
                    self.assertEqual(
                        tuple(profile.levels[level].boundary_vertices),
                        processed_boundary(instance, ordering, level),
                    )
                self.assertEqual(
                    boundary_width(instance, ordering),
                    max(len(level.boundary_vertices) for level in profile.levels),
                )
                if max(vertex_occurrences(instance), default=0) <= 3:
                    occurrence += 1
                    self.assertTrue(oracle.satisfiable)
                if is_incidence_forest(instance):
                    forests += 1
                    witness = color_incidence_forest(instance)
                    self.assertTrue(verify_coloring(instance, witness))
            self.assertEqual(forests, forest_counts[n])
            self.assertEqual(occurrence, occurrence_counts[n])

    def test_forest_and_cycle_boundaries(self):
        path = normalize_instance(7, ((0, 1, 2), (2, 3, 4), (4, 5, 6)))
        self.assertTrue(is_incidence_forest(path))
        self.assertTrue(verify_coloring(path, color_incidence_forest(path)))
        cycle = normalize_instance(6, ((0, 1, 2), (0, 4, 5), (2, 3, 4)))
        self.assertFalse(is_incidence_forest(cycle))
        with self.assertRaises(ValidationError):
            color_incidence_forest(cycle)

    def test_minimum_boundary_width_guard(self):
        single = normalize_instance(3, ((0, 1, 2),))
        self.assertEqual(minimum_boundary_width(single), 2)
        guarded = normalize_instance(9, ())
        with self.assertRaises(ValidationError):
            minimum_boundary_width(guarded)


class CalibrationRecordTests(unittest.TestCase):
    def test_record_semantics_and_digest(self):
        record = calibration_record()
        self.assertTrue(verify_calibration_record(record))
        self.assertEqual(record["graph"]["census"]["totals"], {"total": 1100, "bipartite": 428, "non_bipartite": 672})
        self.assertEqual(record["xor"]["census"]["totals"], {"total": 16453, "consistent": 890, "inconsistent": 15563})
        self.assertEqual(record["nae"]["filtered_census"]["totals"]["incidence_forest"], 36)
        self.assertEqual(record["nae"]["filtered_census"]["totals"]["occurrence_at_most_three"], 344)
        self.assertEqual(record["nae"]["filtered_census"]["totals"]["incidence_forest_unsatisfiable"], 0)
        self.assertEqual(record["nae"]["filtered_census"]["totals"]["occurrence_at_most_three_unsatisfiable"], 0)

    def test_cli_calibrate(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "calibration.json"
            run = subprocess.run(
                [sys.executable, "-m", "nae3sat.cli", "calibrate", "--output", str(output)],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(output.read_bytes(), calibration_bytes())
            self.assertTrue(verify_calibration_record(json.loads(output.read_text())))


if __name__ == "__main__":
    unittest.main()
