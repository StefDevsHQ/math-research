from __future__ import annotations

import itertools
import json
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from nae3sat import (
    Hypergraph3,
    ValidationError,
    corpus_bytes,
    corpus_record,
    count_satisfying_assignments,
    count_satisfying_assignments_factorized,
    incidence_components,
    is_edge_minimal_unsatisfiable,
    labelled_instances,
    satisfying_assignments,
    solve_exact,
    verify_coloring,
    verify_corpus_record,
)

ROOT = Path(__file__).parents[1]
FIXTURES = ROOT / "tests" / "fixtures"


def reference_assignments(graph: Hypergraph3):
    return tuple(
        coloring
        for coloring in itertools.product((0, 1), repeat=graph.n)
        if all(
            not (coloring[u] == coloring[v] == coloring[w])
            for u, v, w in graph.edges
        )
    )


def reference_edge_minimal(graph: Hypergraph3) -> bool:
    if reference_assignments(graph):
        return False
    return all(
        reference_assignments(
            Hypergraph3(
                graph.n,
                graph.edges[:index] + graph.edges[index + 1 :],
            )
        )
        for index in range(len(graph.edges))
    )


def reference_corpus_rows():
    rows = []
    totals = {
        "instances": 0,
        "satisfiable": 0,
        "unsatisfiable": 0,
        "connected": 0,
        "edge_minimal_unsatisfiable": 0,
        "reference_colourings": 0,
    }
    for n in range(6):
        distribution = Counter()
        row = {
            "n": n,
            "instances": 0,
            "satisfiable": 0,
            "unsatisfiable": 0,
            "connected": 0,
            "edge_minimal_unsatisfiable": 0,
            "satisfying_count_distribution": {},
        }
        for graph in labelled_instances(n):
            assignments = reference_assignments(graph)
            row["instances"] += 1
            totals["instances"] += 1
            totals["reference_colourings"] += 1 << n
            distribution[len(assignments)] += 1
            if assignments:
                row["satisfiable"] += 1
                totals["satisfiable"] += 1
            else:
                row["unsatisfiable"] += 1
                totals["unsatisfiable"] += 1
                if reference_edge_minimal(graph):
                    row["edge_minimal_unsatisfiable"] += 1
                    totals["edge_minimal_unsatisfiable"] += 1
            if n > 0 and len(incidence_components(graph)) == 1:
                row["connected"] += 1
                totals["connected"] += 1
        row["satisfying_count_distribution"] = {
            str(count): distribution[count]
            for count in sorted(distribution)
        }
        rows.append(row)
    return rows, totals


class SolverTests(unittest.TestCase):
    def test_boundary_and_named_controls(self):
        for n in range(6):
            graph = Hypergraph3(n, ())
            self.assertEqual(count_satisfying_assignments(graph), 1 << n)
            result = solve_exact(graph)
            self.assertEqual(result.witness, (0,) * n)
            self.assertEqual(result.assignments_tested, 1)

        single = Hypergraph3(3, ((0, 1, 2),))
        self.assertEqual(count_satisfying_assignments(single), 6)
        self.assertEqual(solve_exact(single).witness, (0, 0, 1))
        self.assertEqual(solve_exact(single).assignments_tested, 2)

        disconnected = Hypergraph3(6, ((0, 1, 2), (3, 4, 5)))
        self.assertEqual(count_satisfying_assignments(disconnected), 36)
        self.assertEqual(
            count_satisfying_assignments_factorized(disconnected),
            36,
        )

    def test_public_type_rejection(self):
        operations = [
            lambda: solve_exact(object()),
            lambda: satisfying_assignments(object()),
            lambda: count_satisfying_assignments(object()),
            lambda: count_satisfying_assignments_factorized(object()),
            lambda: is_edge_minimal_unsatisfiable(object()),
        ]
        for operation in operations:
            with self.subTest(operation=operation), self.assertRaises(
                ValidationError
            ):
                operation()
        with self.assertRaises(ValidationError):
            solve_exact(Hypergraph3(0, ()), use_symmetry=1)
        for n in (-1, True, 1.0):
            with self.subTest(n=n), self.assertRaises(ValidationError):
                tuple(labelled_instances(n))

    def test_complete_labelled_domain_through_five_vertices(self):
        checked = 0
        for n in range(6):
            expected_instances = 1 << len(
                tuple(itertools.combinations(range(n), 3))
            )
            generated = tuple(labelled_instances(n))
            self.assertEqual(len(generated), expected_instances)
            self.assertEqual(len(set(generated)), expected_instances)

            complete_candidates = tuple(
                itertools.product((0, 1), repeat=n)
            )
            for graph in generated:
                expected = reference_assignments(graph)
                self.assertEqual(satisfying_assignments(graph), expected)
                self.assertEqual(
                    count_satisfying_assignments(graph),
                    len(expected),
                )
                self.assertEqual(
                    count_satisfying_assignments_factorized(graph),
                    len(expected),
                )

                baseline = solve_exact(graph, use_symmetry=False)
                optimized = solve_exact(graph, use_symmetry=True)
                least = expected[0] if expected else None
                self.assertEqual(baseline.satisfiable, bool(expected))
                self.assertEqual(optimized.satisfiable, bool(expected))
                self.assertEqual(baseline.witness, least)
                self.assertEqual(optimized.witness, least)
                if least is not None:
                    self.assertTrue(verify_coloring(graph, least))
                    expected_tested = complete_candidates.index(least) + 1
                else:
                    expected_tested = 1 << n
                self.assertEqual(
                    baseline.assignments_tested,
                    expected_tested,
                )
                checked += 1
        self.assertEqual(checked, 1045)

    def test_fano_unsatisfiable_and_edge_minimal_independently(self):
        fano = Hypergraph3(
            7,
            (
                (0, 1, 2),
                (0, 3, 4),
                (0, 5, 6),
                (1, 3, 5),
                (1, 4, 6),
                (2, 3, 6),
                (2, 4, 5),
            ),
        )
        self.assertEqual(reference_assignments(fano), ())
        self.assertTrue(reference_edge_minimal(fano))
        optimized = solve_exact(fano)
        self.assertFalse(optimized.satisfiable)
        self.assertEqual(optimized.assignments_tested, 64)
        self.assertEqual(count_satisfying_assignments(fano), 0)
        self.assertTrue(is_edge_minimal_unsatisfiable(fano))


class CorpusAndCLITests(unittest.TestCase):
    def test_committed_corpus_matches_independent_aggregation(self):
        record = corpus_record()
        self.assertTrue(verify_corpus_record(record))
        reference_rows, reference_totals = reference_corpus_rows()
        self.assertEqual(record["counts"], reference_rows)
        self.assertEqual(record["totals"], reference_totals)
        self.assertEqual(record["totals"]["instances"], 1045)
        self.assertEqual(record["totals"]["satisfiable"], 1044)
        self.assertEqual(record["totals"]["unsatisfiable"], 1)
        self.assertEqual(record["totals"]["reference_colourings"], 33047)
        committed = (
            ROOT
            / "corpus"
            / "all-labelled-n-le-5.json"
        ).read_bytes()
        self.assertEqual(committed, corpus_bytes())
        self.assertEqual(
            committed,
            json.dumps(record, separators=(",", ":")).encode("utf-8"),
        )

    def test_cli_solve_count_and_census(self):
        fixture = FIXTURES / "single-edge.json"
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "census.json"
            commands = [
                ["solve", str(fixture)],
                ["count", str(fixture)],
                [
                    "census",
                    "--max-vertices",
                    "5",
                    "--output",
                    str(output),
                ],
            ]
            for arguments in commands:
                run = subprocess.run(
                    [sys.executable, "-m", "nae3sat.cli", *arguments],
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(output.read_bytes(), corpus_bytes())


if __name__ == "__main__":
    unittest.main()
