from __future__ import annotations

import itertools
import unittest

from nae3sat import (
    boundary_width,
    calibration_record,
    color_incidence_forest,
    is_incidence_forest,
    labelled_instances,
    normalize_instance,
    processed_boundary,
    verify_coloring,
)


def _direct_boundary(instance, ordering, level):
    processed = set(ordering[:level])
    remainder = set(ordering[level:])
    return tuple(
        vertex
        for vertex in ordering[:level]
        if any(vertex in edge and any(other in remainder for other in edge) for edge in instance.edges)
    )


class VS04PostMergeRegressionTests(unittest.TestCase):
    def test_high_degree_incidence_tree(self):
        edges = tuple((0, 2 * index + 1, 2 * index + 2) for index in range(20))
        instance = normalize_instance(41, edges)
        self.assertTrue(is_incidence_forest(instance))
        witness = color_incidence_forest(instance)
        self.assertTrue(verify_coloring(instance, witness))

    def test_interval_boundary_matches_direct_definition(self):
        for n in range(6):
            for instance in labelled_instances(n):
                orderings = (tuple(range(n)), tuple(reversed(range(n))))
                for ordering in orderings:
                    direct_width = 0
                    for level in range(n + 1):
                        expected = _direct_boundary(instance, ordering, level)
                        self.assertEqual(processed_boundary(instance, ordering, level), expected)
                        direct_width = max(direct_width, len(expected))
                    self.assertEqual(boundary_width(instance, ordering), direct_width)

    def test_planar_source_identifier(self):
        source = calibration_record()["external_boundaries"]["planar_nae3sat"]["source"]
        self.assertEqual(source, "Moret-1988-planar-nae3sat")


if __name__ == "__main__":
    unittest.main()
