from __future__ import annotations

import hashlib
import itertools
import json
import os
import unittest

from nae3sat import profile_corpus_record


def _bits_index(bits: tuple[int, ...]) -> int:
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value


def _completion_mask(
    completion_set: frozenset[tuple[int, ...]],
    width: int,
) -> int:
    mask = 0
    for index, completion in enumerate(
        itertools.product((0, 1), repeat=width)
    ):
        if completion in completion_set:
            mask |= 1 << index
    return mask


def _boundary_count(
    triples: tuple[tuple[int, int, int], ...],
    graph_mask: int,
    ordering: tuple[int, ...],
    level: int,
    assignments: tuple[tuple[int, ...], ...],
) -> int:
    positions = {vertex: index for index, vertex in enumerate(ordering)}
    boundary_positions = tuple(
        position
        for position in range(level)
        if any(
            graph_mask & (1 << edge_index)
            and ordering[position] in edge
            and any(positions[other] >= level for other in edge)
            for edge_index, edge in enumerate(triples)
        )
    )
    completed = tuple(
        tuple(positions[vertex] for vertex in edge)
        for edge_index, edge in enumerate(triples)
        if graph_mask & (1 << edge_index)
        and max(positions[vertex] for vertex in edge) < level
    )
    states: set[tuple[int, ...]] = set()
    for assignment in assignments:
        if all(
            not (assignment[u] == assignment[v] == assignment[w])
            for u, v, w in completed
        ):
            states.add(
                tuple(assignment[position] for position in boundary_positions)
            )
    return len(states)


def _reference_sequence_digest(n: int) -> str:
    triples = tuple(itertools.combinations(range(n), 3))
    digest = hashlib.sha256()

    for ordering in itertools.permutations(range(n)):
        positions = {vertex: index for index, vertex in enumerate(ordering)}
        full_assignments = tuple(itertools.product((0, 1), repeat=n))
        violation_masks: list[int] = []
        for assignment in full_assignments:
            violation_mask = 0
            for edge_index, edge in enumerate(triples):
                a, b, c = (
                    assignment[positions[vertex]] for vertex in edge
                )
                if a == b == c:
                    violation_mask |= 1 << edge_index
            violation_masks.append(violation_mask)

        prefix_assignments = tuple(
            tuple(itertools.product((0, 1), repeat=level))
            for level in range(n + 1)
        )

        for graph_mask in range(1 << len(triples)):
            satisfying = tuple(
                assignment
                for assignment, violation_mask in zip(
                    full_assignments,
                    violation_masks,
                )
                if violation_mask & graph_mask == 0
            )

            level_class_ids: list[tuple[int, ...]] = []
            level_class_sets: list[
                tuple[frozenset[tuple[int, ...]], ...]
            ] = []
            for level in range(n + 1):
                completion_sets: list[set[tuple[int, ...]]] = [
                    set() for _ in range(1 << level)
                ]
                for assignment in satisfying:
                    completion_sets[
                        _bits_index(assignment[:level])
                    ].add(assignment[level:])

                seen: dict[frozenset[tuple[int, ...]], int] = {}
                class_ids: list[int] = []
                classes: list[frozenset[tuple[int, ...]]] = []
                for completion_set in completion_sets:
                    frozen = frozenset(completion_set)
                    class_id = seen.get(frozen)
                    if class_id is None:
                        class_id = len(classes)
                        seen[frozen] = class_id
                        classes.append(frozen)
                    class_ids.append(class_id)
                level_class_ids.append(tuple(class_ids))
                level_class_sets.append(tuple(classes))

            level_signatures: list[object] = []
            for level in range(n + 1):
                class_ids = level_class_ids[level]
                classes = level_class_sets[level]
                class_masks = [
                    _completion_mask(completion_set, n - level)
                    for completion_set in classes
                ]

                transitions = None
                if level < n:
                    next_ids = level_class_ids[level + 1]
                    transition_rows: list[list[int]] = []
                    for class_id in range(len(classes)):
                        pair_set = {
                            (
                                next_ids[2 * prefix],
                                next_ids[2 * prefix + 1],
                            )
                            for prefix, value in enumerate(class_ids)
                            if value == class_id
                        }
                        if len(pair_set) != 1:
                            raise AssertionError(
                                "reference transition is not well-defined"
                            )
                        transition_rows.append(list(next(iter(pair_set))))
                    transitions = transition_rows

                boundary_count = _boundary_count(
                    triples,
                    graph_mask,
                    ordering,
                    level,
                    prefix_assignments[level],
                )
                level_signatures.append(
                    [
                        class_masks,
                        list(class_ids),
                        transitions,
                        boundary_count,
                    ]
                )

            signature = [graph_mask, list(ordering), level_signatures]
            digest.update(
                json.dumps(
                    signature,
                    separators=(",", ":"),
                    ensure_ascii=True,
                ).encode("utf-8")
            )
            digest.update(b"\n")

    return digest.hexdigest()


class IndependentSequenceDigestTests(unittest.TestCase):
    @unittest.skipUnless(
        os.environ.get("NAE3_FULL_VS03_REFERENCE") == "1",
        "full independent sequence digest runs on the pinned CI runtime",
    )
    def test_every_profile_sequence_digest(self):
        record = profile_corpus_record(5)
        expected = record["profile_sequence_sha256_by_n"]
        for n_text, digest in expected.items():
            n = int(n_text)
            with self.subTest(n=n):
                self.assertEqual(
                    _reference_sequence_digest(n),
                    digest,
                )


if __name__ == "__main__":
    unittest.main()
