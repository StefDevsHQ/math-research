from __future__ import annotations

import itertools
import unittest

from nae3sat.pcrnf import build_pcrnf, pcrnf_completion_mask
from nae3sat.pcrnf_lower_bound import (
    central_lift,
    certificate_prefixes,
    cut_induced_matching_certificate,
    is_induced_matching,
    normalize_graph_edges,
    verify_greedy_bound,
)


def complete_graph(vertex_count: int):
    return normalize_graph_edges(
        vertex_count,
        itertools.combinations(range(vertex_count), 2),
    )


def complete_bipartite(left_size: int, right_size: int):
    return normalize_graph_edges(
        left_size + right_size,
        (
            (left, left_size + right)
            for left in range(left_size)
            for right in range(right_size)
        ),
    )


class CentralLiftTests(unittest.TestCase):
    def test_center_zero_is_monotone_two_cnf(self):
        graph_edges = ((0, 1), (1, 2), (2, 3))
        instance = central_lift(4, graph_edges)
        center = 4
        for bits in itertools.product((0, 1), repeat=4):
            colours = bits + (0,)
            nae_value = all(
                not (colours[u] == colours[v] == colours[center])
                for u, v, _ in instance.edges
            )
            monotone_value = all(bits[u] or bits[v] for u, v in graph_edges)
            self.assertEqual(nae_value, monotone_value)

    def test_center_one_is_dual_monotone_two_cnf(self):
        graph_edges = ((0, 1), (1, 2), (2, 3))
        instance = central_lift(4, graph_edges)
        center = 4
        for bits in itertools.product((0, 1), repeat=4):
            colours = bits + (1,)
            nae_value = all(
                not (colours[u] == colours[v] == colours[center])
                for u, v, _ in instance.edges
            )
            dual_value = all((not bits[u]) or (not bits[v]) for u, v in graph_edges)
            self.assertEqual(nae_value, dual_value)


class CertificateTests(unittest.TestCase):
    def _check_all_orderings(self, vertex_count, graph_edges):
        instance = central_lift(vertex_count, graph_edges)
        for ordering in itertools.permutations(range(vertex_count + 1)):
            certificate = cut_induced_matching_certificate(
                vertex_count,
                graph_edges,
                ordering,
            )
            self.assertTrue(
                is_induced_matching(
                    vertex_count,
                    graph_edges,
                    certificate.induced_matching,
                )
            )
            self.assertTrue(verify_greedy_bound(certificate))
            prefixes = certificate_prefixes(vertex_count, ordering, certificate)
            masks = {
                pcrnf_completion_mask(
                    build_pcrnf(instance, ordering, prefix),
                    ordering[len(prefix) :],
                )
                for prefix in prefixes
            }
            self.assertEqual(len(masks), 1 << len(certificate.induced_matching))
            self.assertNotIn(0, masks)

    def test_complete_graph_four_all_orderings(self):
        self._check_all_orderings(4, complete_graph(4))

    def test_complete_bipartite_three_three_all_orderings(self):
        self._check_all_orderings(6, complete_bipartite(3, 3))

    def test_center_first_middle_last(self):
        graph_edges = ((0, 4), (1, 5), (2, 6), (3, 7))
        instance = central_lift(8, graph_edges)
        orderings = (
            (8, 0, 1, 2, 3, 4, 5, 6, 7),
            (0, 1, 8, 2, 3, 4, 5, 6, 7),
            (0, 1, 2, 3, 4, 5, 6, 7, 8),
        )
        for ordering in orderings:
            certificate = cut_induced_matching_certificate(8, graph_edges, ordering)
            prefixes = certificate_prefixes(8, ordering, certificate)
            masks = {
                pcrnf_completion_mask(
                    build_pcrnf(instance, ordering, prefix),
                    ordering[len(prefix) :],
                )
                for prefix in prefixes
            }
            self.assertEqual(len(masks), 16)
            self.assertNotIn(0, masks)


if __name__ == "__main__":
    unittest.main()
