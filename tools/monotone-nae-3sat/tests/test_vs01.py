from __future__ import annotations

import itertools
import json
import random
import subprocess
import sys
import unittest
from pathlib import Path

from nae3sat import (
    ColoringError,
    Hypergraph3,
    ParseError,
    ValidationError,
    active_core,
    canonical_bytes,
    encoded_size_bytes,
    first_violated_edge,
    incidence_components,
    induced_subinstance,
    instance_id,
    normalize_instance,
    parse_instance_json,
    to_canonical_json,
    verify_coloring,
)

FIXTURES = Path(__file__).parent / "fixtures"


class ModelTests(unittest.TestCase):
    def test_empty_and_edgeless(self):
        self.assertEqual(normalize_instance(0, []), Hypergraph3(0, ()))
        self.assertEqual(normalize_instance(3, []).n, 3)

    def test_normalizes_and_deduplicates(self):
        graph = normalize_instance(5, [[4, 2, 3], [2, 0, 1], [3, 4, 2]])
        self.assertEqual(graph.edges, ((0, 1, 2), (2, 3, 4)))

    def test_generator_input(self):
        graph = normalize_instance(3, (edge for edge in [[2, 1, 0]]))
        self.assertEqual(graph.edges, ((0, 1, 2),))

    def test_rejects_invalid_graph_inputs(self):
        invalid = [
            lambda: normalize_instance(-1, []),
            lambda: normalize_instance(True, []),
            lambda: normalize_instance(3, [[0, 0, 1]]),
            lambda: normalize_instance(3, [[-1, 1, 2]]),
            lambda: normalize_instance(3, [[0, 1, 3]]),
            lambda: normalize_instance(3, [[0, 1]]),
            lambda: normalize_instance(3, [[False, 1, 2]]),
            lambda: normalize_instance(3, [[0.0, 1, 2]]),
        ]
        for operation in invalid:
            with self.subTest(operation=operation), self.assertRaises(ValidationError):
                operation()

    def test_direct_constructor_enforces_canonical_form(self):
        invalid = [
            lambda: Hypergraph3(3, [(0, 1, 2)]),
            lambda: Hypergraph3(3, ((2, 0, 1),)),
            lambda: Hypergraph3(3, ((0, 1, 2), (0, 1, 2))),
            lambda: Hypergraph3(5, ((2, 3, 4), (0, 1, 2))),
        ]
        for operation in invalid:
            with self.subTest(operation=operation), self.assertRaises(ValidationError):
                operation()


class SerializationTests(unittest.TestCase):
    def test_round_trip_and_canonical_order(self):
        graph = normalize_instance(4, [[3, 2, 1], [2, 1, 0]])
        text = to_canonical_json(graph)
        self.assertEqual(text, '{"format":"nae3-v1","vertices":[0,1,2,3],"edges":[[0,1,2],[1,2,3]]}')
        self.assertEqual(parse_instance_json(text), graph)

    def test_noncanonical_inputs_have_same_identity(self):
        a = parse_instance_json((FIXTURES / "single-edge.json").read_bytes())
        b = parse_instance_json((FIXTURES / "duplicate-unsorted.json").read_bytes())
        self.assertEqual(a, b)
        self.assertEqual(canonical_bytes(a), canonical_bytes(b))
        self.assertEqual(instance_id(a), instance_id(b))

    def test_isolated_vertices_affect_identity(self):
        a = normalize_instance(3, [])
        b = normalize_instance(4, [])
        self.assertNotEqual(canonical_bytes(a), canonical_bytes(b))
        self.assertNotEqual(instance_id(a), instance_id(b))

    def test_encoded_size_and_identifier(self):
        graph = normalize_instance(3, [[0, 1, 2]])
        self.assertEqual(encoded_size_bytes(graph), len(canonical_bytes(graph)))
        self.assertRegex(instance_id(graph), r"^nae3-v1-sha256-[0-9a-f]{64}$")

    def test_pinned_identifiers(self):
        expected = {
            "empty.json": "nae3-v1-sha256-95e95c77352dcd2d94e832f3bc4964beb13da79439f89f79632bee4f420f368f",
            "isolated-three.json": "nae3-v1-sha256-3c53e92c81bc5276993163f9cccb0b0934c00e1c0b696d0b7ebfae92d48c6443",
            "single-edge.json": "nae3-v1-sha256-794c043ed817d84d30d57d79bb3dd40bad9cd0f8ebe594100b93e0abf97bebf7",
            "two-disconnected-edges.json": "nae3-v1-sha256-1be9a1eaf7f773add7754fd24c926e13f6cea32bb18b7f0074156ccc7fbb1af9",
            "overlap-chain.json": "nae3-v1-sha256-69636ad41f919734caf63189a5880399cb1062bdf772b85809bfc87f64caef07",
            "fano-plane.json": "nae3-v1-sha256-3b78789e10d0828f0051c7a0cea558bf988e067433a230a5c62af86db9d45de8",
        }
        for name, identifier in expected.items():
            with self.subTest(name=name):
                graph = parse_instance_json((FIXTURES / name).read_bytes())
                self.assertEqual(instance_id(graph), identifier)

    def test_strict_parser_rejections(self):
        fixtures = [
            "duplicate-keys.json",
            "noncontiguous-vertices.json",
            "repeated-edge-vertex.json",
            "unknown-field.json",
            "wrong-version.json",
            "invalid-utf8.bin",
        ]
        for name in fixtures:
            with self.subTest(name=name), self.assertRaises(ParseError):
                parse_instance_json((FIXTURES / name).read_bytes())
        for text in ["{", "[]", '{"format":"nae3-v1","vertices":[]}', '{"format":"nae3-v1","vertices":[],"edges":[],"x":NaN}']:
            with self.subTest(text=text), self.assertRaises(ParseError):
                parse_instance_json(text)

    def test_rejects_wrong_json_types(self):
        bad = [
            {"format":"nae3-v1","vertices":[False],"edges":[]},
            {"format":"nae3-v1","vertices":[0.0],"edges":[]},
            {"format":"nae3-v1","vertices":[],"edges":{}},
            {"format":"nae3-v1","vertices":[0,1,2],"edges":["012"]},
        ]
        for document in bad:
            with self.subTest(document=document), self.assertRaises(ParseError):
                parse_instance_json(json.dumps(document))


class ComponentTests(unittest.TestCase):
    def test_components_include_isolates_and_are_ordered(self):
        graph = normalize_instance(8, [[5, 6, 7], [0, 1, 2]])
        self.assertEqual(incidence_components(graph), ((0,1,2),(3,),(4,),(5,6,7)))

    def test_overlap_chain(self):
        graph = normalize_instance(7, [[0,1,2],[2,3,4],[4,5,6]])
        self.assertEqual(incidence_components(graph), ((0,1,2,3,4,5,6),))

    def test_induced_subinstance_map(self):
        graph = normalize_instance(7, [[0,2,4],[2,4,6],[1,3,5]])
        result = induced_subinstance(graph, [6,2,4])
        self.assertEqual(result.new_to_old, (2,4,6))
        self.assertEqual(result.graph.edges, ((0,1,2),))

    def test_active_core(self):
        graph = normalize_instance(6, [[1,3,5]])
        result = active_core(graph)
        self.assertEqual(result.new_to_old, (1,3,5))
        self.assertEqual(result.graph.edges, ((0,1,2),))
        empty = active_core(normalize_instance(4, []))
        self.assertEqual(empty.graph, Hypergraph3(0, ()))
        self.assertEqual(empty.new_to_old, ())

    def test_invalid_selection(self):
        graph = normalize_instance(4, [[0,1,2]])
        for vertices in [[0,0],[False],[4],[-1],"012"]:
            with self.subTest(vertices=vertices), self.assertRaises(ValidationError):
                induced_subinstance(graph, vertices)


class VerifierTests(unittest.TestCase):
    def test_single_edge_has_six_solutions(self):
        graph = normalize_instance(3, [[0,1,2]])
        solutions = [bits for bits in itertools.product((0,1), repeat=3) if verify_coloring(graph,bits)]
        self.assertEqual(len(solutions), 6)

    def test_empty_and_disconnected(self):
        self.assertTrue(verify_coloring(normalize_instance(0, []), ()))
        graph = normalize_instance(6, [[0,1,2],[3,4,5]])
        self.assertTrue(verify_coloring(graph, (0,0,1,1,0,1)))

    def test_first_violation_is_canonical(self):
        graph = normalize_instance(5, [[2,3,4],[0,1,2]])
        self.assertEqual(first_violated_edge(graph, (0,0,0,0,0)), (0,1,2))

    def test_complement_symmetry_and_api_agreement(self):
        graph = normalize_instance(5, [[0,1,2],[2,3,4]])
        for coloring in itertools.product((0,1), repeat=5):
            complement = tuple(1-bit for bit in coloring)
            self.assertEqual(verify_coloring(graph,coloring), verify_coloring(graph,complement))
            self.assertEqual(verify_coloring(graph,coloring), first_violated_edge(graph,coloring) is None)

    def test_rejects_malformed_coloring(self):
        graph = normalize_instance(3, [[0,1,2]])
        malformed = [
            (0,1), (0,1,2), (0,1,True), (0,1,0.0), "010", b"010",
            {0,1}, {0:"a",1:"b",2:"c"}, (bit for bit in (0,1,0)),
        ]
        for coloring in malformed:
            with self.subTest(coloring=coloring), self.assertRaises(ColoringError):
                verify_coloring(graph, coloring)


class PublicTypeTests(unittest.TestCase):
    def test_public_instance_operations_reject_wrong_type(self):
        operations = [
            lambda: incidence_components(object()),
            lambda: induced_subinstance(object(), []),
            lambda: active_core(object()),
            lambda: verify_coloring(object(), ()),
            lambda: first_violated_edge(object(), ()),
            lambda: to_canonical_json(object()),
            lambda: canonical_bytes(object()),
            lambda: instance_id(object()),
            lambda: encoded_size_bytes(object()),
        ]
        for operation in operations:
            with self.subTest(operation=operation), self.assertRaises(ValidationError):
                operation()


class ReferenceCrossCheckTests(unittest.TestCase):
    @staticmethod
    def _reference_components(n, edges):
        adjacency = [set() for _ in range(n)]
        for edge in edges:
            for u in edge:
                adjacency[u].update(v for v in edge if v != u)
        seen = set()
        components = []
        for start in range(n):
            if start in seen:
                continue
            stack = [start]
            seen.add(start)
            component = []
            while stack:
                vertex = stack.pop()
                component.append(vertex)
                for neighbour in adjacency[vertex]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        stack.append(neighbour)
            components.append(tuple(sorted(component)))
        return tuple(components)

    @staticmethod
    def _reference_verify(edges, coloring):
        return all(len({coloring[v] for v in edge}) == 2 for edge in edges)

    def test_seeded_random_reference_cross_check(self):
        rng = random.Random(20260722)
        checked = 0
        for n in range(9):
            triples = list(itertools.combinations(range(n), 3))
            for _ in range(150):
                raw_edges = []
                for edge in triples:
                    if rng.random() < 0.35:
                        shuffled = list(edge)
                        rng.shuffle(shuffled)
                        raw_edges.append(shuffled)
                        if rng.random() < 0.10:
                            raw_edges.append(list(reversed(shuffled)))
                rng.shuffle(raw_edges)
                graph = normalize_instance(n, raw_edges)
                expected_edges = tuple(sorted(set(tuple(sorted(edge)) for edge in raw_edges)))
                self.assertEqual(graph.edges, expected_edges)
                self.assertEqual(parse_instance_json(to_canonical_json(graph)), graph)
                self.assertEqual(incidence_components(graph), self._reference_components(n, graph.edges))
                core = active_core(graph)
                active = tuple(v for v in range(n) if any(v in edge for edge in graph.edges))
                self.assertEqual(core.new_to_old, active)
                index = {old: new for new, old in enumerate(active)}
                expected_core_edges = tuple(tuple(index[v] for v in edge) for edge in graph.edges)
                self.assertEqual(core.graph.edges, expected_core_edges)
                for coloring in itertools.product((0, 1), repeat=n):
                    expected = self._reference_verify(graph.edges, coloring)
                    self.assertEqual(verify_coloring(graph, coloring), expected)
                    self.assertEqual(first_violated_edge(graph, coloring) is None, expected)
                checked += 1
        self.assertEqual(checked, 1350)


class CLITests(unittest.TestCase):
    def test_success_and_error(self):
        root = Path(__file__).parents[1]
        good = subprocess.run([sys.executable,"-m","nae3sat.cli","validate",str(FIXTURES/"fano-plane.json")],cwd=root,text=True,capture_output=True,check=False)
        self.assertEqual(good.returncode, 0)
        summary = json.loads(good.stdout)
        self.assertEqual((summary["n"],summary["m"],summary["encoded_bytes"]),(7,7,113))
        self.assertNotIn("satisfiable", summary)
        bad = subprocess.run([sys.executable,"-m","nae3sat.cli","validate",str(FIXTURES/"wrong-version.json")],cwd=root,text=True,capture_output=True,check=False)
        self.assertEqual(bad.returncode, 2)
        self.assertTrue(bad.stderr.startswith("error:"))


if __name__ == "__main__":
    unittest.main()
