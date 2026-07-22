from __future__ import annotations

import itertools
import os
import subprocess
import sys
import unittest

from nae3sat import (
    Hypergraph3,
    active_core,
    canonical_bytes,
    first_violated_edge,
    incidence_components,
    induced_subinstance,
    parse_instance_json,
    verify_coloring,
)


class ExhaustiveFoundationTests(unittest.TestCase):
    @staticmethod
    def _reference_components(n: int, edges: tuple[tuple[int, int, int], ...]):
        adjacency = [set() for _ in range(n)]
        for edge in edges:
            for vertex in edge:
                adjacency[vertex].update(other for other in edge if other != vertex)
        seen: set[int] = set()
        components: list[tuple[int, ...]] = []
        for start in range(n):
            if start in seen:
                continue
            seen.add(start)
            stack = [start]
            component: list[int] = []
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
        return all(not (coloring[u] == coloring[v] == coloring[w]) for u, v, w in edges)

    def test_all_labelled_hypergraphs_through_five_vertices(self):
        instance_count = 0
        coloring_count = 0
        induced_count = 0

        for n in range(6):
            triples = list(itertools.combinations(range(n), 3))
            for edge_mask in range(1 << len(triples)):
                edges = tuple(
                    edge for index, edge in enumerate(triples)
                    if edge_mask & (1 << index)
                )
                graph = Hypergraph3(n, edges)

                self.assertEqual(parse_instance_json(canonical_bytes(graph)), graph)
                self.assertEqual(
                    incidence_components(graph),
                    self._reference_components(n, edges),
                )

                active = tuple(
                    vertex for vertex in range(n)
                    if any(vertex in edge for edge in edges)
                )
                core = active_core(graph)
                self.assertEqual(core.new_to_old, active)
                active_index = {old: new for new, old in enumerate(active)}
                self.assertEqual(
                    core.graph.edges,
                    tuple(tuple(active_index[v] for v in edge) for edge in edges),
                )

                for coloring in itertools.product((0, 1), repeat=n):
                    expected = self._reference_verify(edges, coloring)
                    self.assertEqual(verify_coloring(graph, coloring), expected)
                    self.assertEqual(first_violated_edge(graph, coloring) is None, expected)
                    coloring_count += 1

                for vertex_mask in range(1 << n):
                    selected = tuple(
                        vertex for vertex in range(n)
                        if vertex_mask & (1 << vertex)
                    )
                    derived = induced_subinstance(graph, reversed(selected))
                    self.assertEqual(derived.new_to_old, selected)
                    selected_index = {old: new for new, old in enumerate(selected)}
                    expected_edges = tuple(
                        tuple(selected_index[v] for v in edge)
                        for edge in edges
                        if all(v in selected_index for v in edge)
                    )
                    self.assertEqual(derived.graph.edges, expected_edges)
                    induced_count += 1

                instance_count += 1

        self.assertEqual(instance_count, 1045)
        self.assertEqual(coloring_count, 33047)
        self.assertEqual(induced_count, 33047)

    def test_cross_process_determinism_under_hash_seeds(self):
        script = (
            "from nae3sat import *; "
            "g=normalize_instance(7,[[0,1,2],[0,3,4],[0,5,6],"
            "[1,3,5],[1,4,6],[2,3,6],[2,4,5]]); "
            "print(to_canonical_json(g)); print(instance_id(g)); "
            "print(incidence_components(g))"
        )
        root = os.path.dirname(os.path.dirname(__file__))
        outputs: list[str] = []
        for seed in ("0", "1", "42", "random"):
            environment = dict(os.environ)
            environment["PYTHONHASHSEED"] = seed
            run = subprocess.run(
                [sys.executable, "-c", script],
                cwd=root,
                env=environment,
                text=True,
                capture_output=True,
                check=True,
            )
            outputs.append(run.stdout)
        self.assertEqual(len(set(outputs)), 1)


if __name__ == "__main__":
    unittest.main()
