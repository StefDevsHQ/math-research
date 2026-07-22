from __future__ import annotations

import unittest
from dataclasses import replace

from nae3sat import (
    ExactProfile,
    Hypergraph3,
    ProfileLevel,
    ValidationError,
    build_exact_profile,
)


class ProfileInvariantTests(unittest.TestCase):
    def test_profile_level_rejects_noncanonical_values(self):
        invalid = [
            lambda: ProfileLevel(
                1, (0,), (), (), (0, 1), (1, 1), None, 1
            ),
            lambda: ProfileLevel(
                1, (0,), (), (), (1, 0), (1, 0), None, 1
            ),
            lambda: ProfileLevel(
                1, (0,), (), (), (0, 0), (1, 0), None, 1
            ),
            lambda: ProfileLevel(
                0, (), (), (), (0,), (1,), ((0,),), 1
            ),
            lambda: ProfileLevel(
                0, (), (), (), (0,), (1,), None, 2
            ),
        ]
        for operation in invalid:
            with self.subTest(operation=operation), self.assertRaises(
                ValidationError
            ):
                operation()

    def test_exact_profile_rejects_cross_level_inconsistency(self):
        graph = Hypergraph3(3, ((0, 1, 2),))
        profile = build_exact_profile(graph, (0, 1, 2))

        first = profile.levels[0]
        assert first.transitions is not None
        bad_first = replace(first, transitions=((99, 0),))
        with self.assertRaises(ValidationError):
            ExactProfile(graph, profile.ordering, (bad_first,) + profile.levels[1:])

        final = profile.levels[-1]
        bad_final = replace(final, class_masks=(2, 0))
        with self.assertRaises(ValidationError):
            ExactProfile(graph, profile.ordering, profile.levels[:-1] + (bad_final,))

        middle = profile.levels[1]
        bad_middle = replace(
            middle,
            processed_valid_boundary_states=(
                middle.processed_valid_boundary_states + 1
            ),
        )
        with self.assertRaises(ValidationError):
            ExactProfile(
                graph,
                profile.ordering,
                profile.levels[:1] + (bad_middle,) + profile.levels[2:],
            )


if __name__ == "__main__":
    unittest.main()
