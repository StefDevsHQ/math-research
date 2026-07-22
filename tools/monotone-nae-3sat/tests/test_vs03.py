from __future__ import annotations

import itertools
import json
import os
import subprocess
import sys
import tempfile
import unittest
from collections import Counter
from pathlib import Path

from nae3sat import (
    Hypergraph3,
    ValidationError,
    build_exact_profile,
    extension_mask,
    labelled_instances,
    profile_bytes,
    profile_corpus_bytes,
    profile_corpus_record,
    profile_record,
    solve_exact,
    validate_ordering,
    verify_profile_corpus_record,
)

ROOT = Path(__file__).parents[1]
FIXTURES = ROOT / "tests" / "fixtures"
CORPUS = ROOT / "profile-corpus" / "all-labelled-orderings-n-le-5.json"


def _bits_index(bits):
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value


def _reference_levels(graph: Hypergraph3, ordering: tuple[int, ...]):
    satisfying = []
    for assignment in itertools.product((0, 1), repeat=graph.n):
        colours = {ordering[index]: assignment[index] for index in range(graph.n)}
        if all(
            not (colours[u] == colours[v] == colours[w])
            for u, v, w in graph.edges
        ):
            satisfying.append(assignment)

    levels = []
    for index in range(graph.n + 1):
        completion_sets = [set() for _ in range(1 << index)]
        for assignment in satisfying:
            completion_sets[_bits_index(assignment[:index])].add(assignment[index:])
        frozen = tuple(frozenset(value) for value in completion_sets)
        seen = {}
        classes = []
        class_ids = []
        for completion_set in frozen:
            if completion_set not in seen:
                seen[completion_set] = len(classes)
                classes.append(completion_set)
            class_ids.append(seen[completion_set])
        transitions = None
        if index < graph.n:
            next_frozen = []
            for prefix in itertools.product((0, 1), repeat=index + 1):
                next_frozen.append(
                    frozenset(
                        assignment[index + 1 :]
                        for assignment in satisfying
                        if assignment[: index + 1] == prefix
                    )
                )
            next_seen = {}
            next_ids = []
            for completion_set in next_frozen:
                if completion_set not in next_seen:
                    next_seen[completion_set] = len(next_seen)
                next_ids.append(next_seen[completion_set])
            transition_rows = []
            for class_id in range(len(classes)):
                member_transitions = {
                    (next_ids[2 * prefix], next_ids[2 * prefix + 1])
                    for prefix, value in enumerate(class_ids)
                    if value == class_id
                }
                if len(member_transitions) != 1:
                    raise AssertionError("reference transition is not well-defined")
                transition_rows.append(next(iter(member_transitions)))
            transitions = tuple(transition_rows)
        levels.append((frozen, tuple(class_ids), tuple(classes), transitions))
    return tuple(levels), bool(satisfying)


def _reference_boundary_count(graph, ordering, index):
    positions = {vertex: position for position, vertex in enumerate(ordering[:index])}
    remainder = set(ordering[index:])
    boundary = tuple(
        vertex
        for vertex in ordering[:index]
        if any(
            vertex in edge and any(other in remainder for other in edge)
            for edge in graph.edges
        )
    )
    completed = tuple(
        edge for edge in graph.edges if all(vertex in positions for vertex in edge)
    )
    states = set()
    for prefix in itertools.product((0, 1), repeat=index):
        if all(
            not (
                prefix[positions[u]]
                == prefix[positions[v]]
                == prefix[positions[w]]
            )
            for u, v, w in completed
        ):
            states.add(tuple(prefix[positions[vertex]] for vertex in boundary))
    return boundary, len(states)


def _assert_profile_matches_reference(testcase, graph, ordering):
    profile = build_exact_profile(graph, ordering)
    reference, satisfiable = _reference_levels(graph, ordering)
    testcase.assertEqual(profile.satisfiable, satisfiable)
    testcase.assertEqual(profile.satisfiable, solve_exact(graph).satisfiable)
    for index, level in enumerate(profile.levels):
        frozen, class_ids, classes, transitions = reference[index]
        testcase.assertEqual(level.assignment_class_ids, class_ids)
        testcase.assertEqual(level.class_count, len(classes))
        testcase.assertEqual(level.transitions, transitions)
        for prefix_index, completion_set in enumerate(frozen):
            expected_mask = 0
            completions = tuple(
                itertools.product((0, 1), repeat=graph.n - index)
            )
            for completion_index, completion in enumerate(completions):
                if completion in completion_set:
                    expected_mask |= 1 << completion_index
            class_id = level.assignment_class_ids[prefix_index]
            testcase.assertEqual(level.class_masks[class_id], expected_mask)
        boundary, count = _reference_boundary_count(graph, ordering, index)
        testcase.assertEqual(level.boundary_vertices, boundary)
        testcase.assertEqual(level.processed_valid_boundary_states, count)


class ProfileContractTests(unittest.TestCase):
    def test_validation(self):
        graph = Hypergraph3(3, ((0, 1, 2),))
        self.assertEqual(validate_ordering(graph, [2, 0, 1]), (2, 0, 1))
        invalid_orderings = ["012", [0, 1], [0, 1, 1], [0, 1, True], [0, 1, 3]]
        for ordering in invalid_orderings:
            with self.subTest(ordering=ordering), self.assertRaises(ValidationError):
                build_exact_profile(graph, ordering)
        for prefix in ["01", [0, 2], [0, True], [0, 1, 0, 1]]:
            with self.subTest(prefix=prefix), self.assertRaises(ValidationError):
                extension_mask(graph, (0, 1, 2), prefix)
        with self.assertRaises(ValidationError):
            build_exact_profile(object(), ())

    def test_single_edge_live_merge_and_dead_class(self):
        graph = Hypergraph3(3, ((0, 1, 2),))
        profile = build_exact_profile(graph, (0, 1, 2))
        level_two = profile.levels[2]
        self.assertEqual(
            level_two.assignment_class_ids[1],
            level_two.assignment_class_ids[2],
        )
        merged_class = level_two.assignment_class_ids[1]
        self.assertNotEqual(level_two.class_masks[merged_class], 0)
        self.assertEqual(extension_mask(graph, (0, 1, 2), (0, 1)), 3)
        self.assertEqual(extension_mask(graph, (0, 1, 2), (1, 0)), 3)
        self.assertIsNotNone(profile.levels[3].dead_class_id)
        _assert_profile_matches_reference(self, graph, (0, 1, 2))

    def test_named_controls(self):
        controls = [
            Hypergraph3(0, ()),
            Hypergraph3(4, ()),
            Hypergraph3(6, ((0, 1, 2), (3, 4, 5))),
            Hypergraph3(7, ((0, 1, 2), (2, 3, 4), (4, 5, 6))),
            Hypergraph3(5, tuple(itertools.combinations(range(5), 3))),
        ]
        orderings = [
            (),
            (3, 1, 0, 2),
            (0, 3, 1, 4, 2, 5),
            (6, 0, 4, 2, 5, 1, 3),
            (4, 3, 2, 1, 0),
        ]
        for graph, ordering in zip(controls, orderings):
            with self.subTest(graph=graph, ordering=ordering):
                _assert_profile_matches_reference(self, graph, ordering)

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
        for ordering in [tuple(range(7)), tuple(reversed(range(7))), (0, 3, 1, 5, 2, 6, 4)]:
            with self.subTest(ordering=ordering):
                _assert_profile_matches_reference(self, fano, ordering)

    def test_complete_exact_reference_through_four_vertices(self):
        checked = 0
        for n in range(5):
            for graph in labelled_instances(n):
                for ordering in itertools.permutations(range(n)):
                    _assert_profile_matches_reference(self, graph, ordering)
                    checked += 1
        self.assertEqual(checked, 400)

    def test_all_orderings_of_complete_five_vertex_obstruction(self):
        graph = Hypergraph3(5, tuple(itertools.combinations(range(5), 3)))
        for ordering in itertools.permutations(range(5)):
            profile = build_exact_profile(graph, ordering)
            self.assertFalse(profile.satisfiable)
            self.assertEqual(profile.levels[0].class_masks, (0,))
            self.assertTrue(all(mask in (0, 1) for mask in profile.levels[5].class_masks))

    def test_canonical_record_determinism(self):
        graph = Hypergraph3(3, ((0, 1, 2),))
        profile = build_exact_profile(graph, (2, 0, 1))
        self.assertEqual(profile_bytes(profile), profile_bytes(profile))
        record = profile_record(profile)
        self.assertEqual(record["format"], "nae3-vs03-profile-v1")
        self.assertEqual(record["ordering"], [2, 0, 1])
        self.assertEqual(json.loads(profile_bytes(profile)), record)


class ProfileCorpusTests(unittest.TestCase):
    def test_committed_corpus_reproduction(self):
        committed = CORPUS.read_bytes()
        generated = profile_corpus_bytes(5)
        self.assertEqual(generated, committed)
        record = profile_corpus_record(5)
        self.assertTrue(verify_profile_corpus_record(record))
        self.assertEqual(record["totals"]["profiles"], 123280)
        self.assertEqual(record["totals"]["exact_classes"], 2153049)
        self.assertEqual(record["totals"]["live_classes"], 1818651)
        self.assertEqual(record["totals"]["unsatisfiable_profiles"], 120)
        self.assertEqual(max(max(row["max_classes_by_level"]) for row in record["counts"]), 8)

    @unittest.skipUnless(
        os.environ.get("NAE3_FULL_VS03_REFERENCE") == "1",
        "full independent reference census runs on the pinned CI runtime",
    )
    def test_full_independent_reference_census(self):
        expected = profile_corpus_record(5)
        reference_rows = []
        total = Counter()

        for n in range(6):
            triples = tuple(itertools.combinations(range(n), 3))
            row = Counter()
            distributions = [Counter() for _ in range(n + 1)]
            maxima = [0] * (n + 1)
            for ordering in itertools.permutations(range(n)):
                positions = {vertex: index for index, vertex in enumerate(ordering)}
                full_assignments = tuple(itertools.product((0, 1), repeat=n))
                violations = []
                for assignment in full_assignments:
                    mask = 0
                    for edge_index, edge in enumerate(triples):
                        a, b, c = (assignment[positions[vertex]] for vertex in edge)
                        if a == b == c:
                            mask |= 1 << edge_index
                    violations.append(mask)
                prefix_assignments = [
                    tuple(itertools.product((0, 1), repeat=index))
                    for index in range(n + 1)
                ]
                prefix_violations = []
                for index, assignments in enumerate(prefix_assignments):
                    level_values = []
                    for assignment in assignments:
                        mask = 0
                        for edge_index, edge in enumerate(triples):
                            edge_positions = tuple(positions[vertex] for vertex in edge)
                            if max(edge_positions) < index:
                                a, b, c = (assignment[position] for position in edge_positions)
                                if a == b == c:
                                    mask |= 1 << edge_index
                        level_values.append(mask)
                    prefix_violations.append(level_values)

                for graph_mask in range(1 << len(triples)):
                    satisfying = [
                        assignment
                        for assignment, violation in zip(full_assignments, violations)
                        if violation & graph_mask == 0
                    ]
                    row["profiles"] += 1
                    row["satisfiable_profiles"] += bool(satisfying)
                    level_ids = []
                    level_classes = []
                    for index in range(n + 1):
                        completion_sets = [set() for _ in range(1 << index)]
                        for assignment in satisfying:
                            completion_sets[_bits_index(assignment[:index])].add(assignment[index:])
                        frozen = [frozenset(value) for value in completion_sets]
                        seen = {}
                        ids = []
                        classes = []
                        for completion_set in frozen:
                            if completion_set not in seen:
                                seen[completion_set] = len(classes)
                                classes.append(completion_set)
                            ids.append(seen[completion_set])
                        level_ids.append(ids)
                        level_classes.append(classes)

                    for index in range(n + 1):
                        classes = level_classes[index]
                        class_count = len(classes)
                        live_count = sum(bool(value) for value in classes)
                        raw_count = 1 << index
                        width = 1 << (n - index)
                        id_bits = 0 if class_count <= 1 else (class_count - 1).bit_length()
                        row["raw_prefixes"] += raw_count
                        row["exact_classes"] += class_count
                        row["live_classes"] += live_count
                        row["dense_unique_completion_bits"] += class_count * width
                        row["assignment_map_bits"] += raw_count * id_bits
                        distributions[index][class_count] += 1
                        maxima[index] = max(maxima[index], class_count)
                        if index < n:
                            next_count = len(level_classes[index + 1])
                            next_bits = 0 if next_count <= 1 else (next_count - 1).bit_length()
                            row["transition_bits"] += 2 * class_count * next_bits
                            for class_id in range(class_count):
                                transitions = {
                                    (
                                        level_ids[index + 1][2 * prefix],
                                        level_ids[index + 1][2 * prefix + 1],
                                    )
                                    for prefix, value in enumerate(level_ids[index])
                                    if value == class_id
                                }
                                self.assertEqual(len(transitions), 1)

                        boundary_positions = []
                        for position in range(index):
                            vertex = ordering[position]
                            if any(
                                graph_mask & (1 << edge_index)
                                and vertex in edge
                                and any(positions[other] >= index for other in edge)
                                for edge_index, edge in enumerate(triples)
                            ):
                                boundary_positions.append(position)
                        states = set()
                        for prefix_index, assignment in enumerate(prefix_assignments[index]):
                            if prefix_violations[index][prefix_index] & graph_mask == 0:
                                states.add(tuple(assignment[position] for position in boundary_positions))
                        row["processed_valid_boundary_states"] += len(states)

            profiles = row["profiles"]
            reference_row = {
                "n": n,
                "instances": 1 << len(triples),
                "orderings_per_instance": 1 if n == 0 else len(tuple(itertools.permutations(range(n)))),
                "profiles": profiles,
                "satisfiable_profiles": row["satisfiable_profiles"],
                "unsatisfiable_profiles": profiles - row["satisfiable_profiles"],
                "raw_prefixes": row["raw_prefixes"],
                "exact_classes": row["exact_classes"],
                "live_classes": row["live_classes"],
                "processed_valid_boundary_states": row["processed_valid_boundary_states"],
                "dense_unique_completion_bits": row["dense_unique_completion_bits"],
                "assignment_map_bits": row["assignment_map_bits"],
                "transition_bits": row["transition_bits"],
                "max_classes_by_level": maxima,
                "class_count_distributions": [
                    {str(key): value for key, value in sorted(distribution.items())}
                    for distribution in distributions
                ],
            }
            reference_rows.append(reference_row)
            total.update({key: reference_row[key] for key in (
                "profiles", "satisfiable_profiles", "unsatisfiable_profiles", "raw_prefixes",
                "exact_classes", "live_classes", "processed_valid_boundary_states",
                "dense_unique_completion_bits", "assignment_map_bits", "transition_bits",
            )})

        self.assertEqual(reference_rows, expected["counts"])
        self.assertEqual(dict(total), expected["totals"])

    def test_cli_profile_and_profile_census(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "profiles.json"
            profile_run = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "nae3sat.cli",
                    "profile",
                    str(FIXTURES / "single-edge.json"),
                    "--ordering",
                    "2,0,1",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(profile_run.returncode, 0, profile_run.stderr)
            summary = json.loads(profile_run.stdout)
            self.assertEqual(summary["format"], "nae3-vs03-summary-v1")
            self.assertEqual(summary["ordering"], [2, 0, 1])

            census_run = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "nae3sat.cli",
                    "profile-census",
                    "--max-vertices",
                    "5",
                    "--output",
                    str(output),
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(census_run.returncode, 0, census_run.stderr)
            self.assertEqual(output.read_bytes(), CORPUS.read_bytes())

            bad = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "nae3sat.cli",
                    "profile",
                    str(FIXTURES / "single-edge.json"),
                    "--ordering",
                    "0,0,2",
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(bad.returncode, 2)
            self.assertTrue(bad.stderr.startswith("error:"))


if __name__ == "__main__":
    unittest.main()
