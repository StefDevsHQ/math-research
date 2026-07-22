"""Deterministic exhaustive aggregate census for exact extension profiles."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from collections import Counter

from .errors import ValidationError

FORMAT = "nae3-vs03-corpus-v1"
DOMAIN = "all-labelled-instance-ordering-pairs-n-le-5"
GENERATOR = "edge-mask-permutation-v1"


def _validate_bound(max_vertices: object) -> int:
    if type(max_vertices) is not int or max_vertices < 0:
        raise ValidationError("max vertices must be a nonnegative integer")
    return max_vertices


def _ordered_violation_masks(
    n: int,
    triples: tuple[tuple[int, int, int], ...],
    ordering: tuple[int, ...],
) -> tuple[
    tuple[int, ...],
    tuple[tuple[int, ...], ...],
    tuple[tuple[tuple[int, ...], ...], ...],
]:
    positions = {vertex: index for index, vertex in enumerate(ordering)}
    full_violations: list[int] = []
    for assignment in itertools.product((0, 1), repeat=n):
        violation_mask = 0
        for edge_index, edge in enumerate(triples):
            a, b, c = (assignment[positions[vertex]] for vertex in edge)
            if a == b == c:
                violation_mask |= 1 << edge_index
        full_violations.append(violation_mask)

    prefix_violations: list[tuple[int, ...]] = []
    prefix_assignments: list[tuple[tuple[int, ...], ...]] = []
    for level in range(n + 1):
        violations: list[int] = []
        assignments = tuple(itertools.product((0, 1), repeat=level))
        for assignment in assignments:
            violation_mask = 0
            for edge_index, edge in enumerate(triples):
                edge_positions = tuple(positions[vertex] for vertex in edge)
                if max(edge_positions) < level:
                    a, b, c = (assignment[position] for position in edge_positions)
                    if a == b == c:
                        violation_mask |= 1 << edge_index
            violations.append(violation_mask)
        prefix_violations.append(tuple(violations))
        prefix_assignments.append(assignments)

    return (
        tuple(full_violations),
        tuple(prefix_violations),
        tuple(prefix_assignments),
    )


def _boundary_positions(
    triples: tuple[tuple[int, int, int], ...],
    graph_mask: int,
    ordering: tuple[int, ...],
    level: int,
) -> tuple[int, ...]:
    positions = {vertex: index for index, vertex in enumerate(ordering)}
    result: list[int] = []
    for position in range(level):
        vertex = ordering[position]
        if any(
            graph_mask & (1 << edge_index)
            and vertex in edge
            and any(positions[other] >= level for other in edge)
            for edge_index, edge in enumerate(triples)
        ):
            result.append(position)
    return tuple(result)


def _count_row(n: int) -> dict[str, object]:
    triples = tuple(itertools.combinations(range(n), 3))
    orderings = tuple(itertools.permutations(range(n)))
    counters: Counter[str] = Counter()
    distributions = [Counter() for _ in range(n + 1)]
    max_classes = [0] * (n + 1)
    profile_digest = hashlib.sha256()

    for ordering in orderings:
        full_violations, prefix_violations, prefix_assignments = (
            _ordered_violation_masks(n, triples, ordering)
        )

        for graph_mask in range(1 << len(triples)):
            assignment_masks: list[tuple[int, ...]] = [()] * (n + 1)
            assignment_masks[n] = tuple(
                1 if violation & graph_mask == 0 else 0
                for violation in full_violations
            )
            for level in range(n - 1, -1, -1):
                child_width = 1 << (n - level - 1)
                children = assignment_masks[level + 1]
                assignment_masks[level] = tuple(
                    children[2 * prefix]
                    | (children[2 * prefix + 1] << child_width)
                    for prefix in range(1 << level)
                )

            level_ids: list[tuple[int, ...]] = []
            level_classes: list[tuple[int, ...]] = []
            for masks in assignment_masks:
                seen: dict[int, int] = {}
                ids: list[int] = []
                classes: list[int] = []
                for mask in masks:
                    class_id = seen.get(mask)
                    if class_id is None:
                        class_id = len(classes)
                        seen[mask] = class_id
                        classes.append(mask)
                    ids.append(class_id)
                level_ids.append(tuple(ids))
                level_classes.append(tuple(classes))

            counters["profiles"] += 1
            counters["satisfiable_profiles"] += assignment_masks[0][0] != 0
            level_signatures: list[object] = []

            for level in range(n + 1):
                classes = level_classes[level]
                class_ids = level_ids[level]
                class_count = len(classes)
                live_count = sum(mask != 0 for mask in classes)
                raw_count = 1 << level
                completion_width = 1 << (n - level)
                class_id_bits = (
                    0 if class_count <= 1 else (class_count - 1).bit_length()
                )

                counters["raw_prefixes"] += raw_count
                counters["exact_classes"] += class_count
                counters["live_classes"] += live_count
                counters["dense_unique_completion_bits"] += (
                    class_count * completion_width
                )
                counters["assignment_map_bits"] += raw_count * class_id_bits
                distributions[level][class_count] += 1
                max_classes[level] = max(max_classes[level], class_count)

                transitions: tuple[tuple[int, int], ...] | None = None
                if level < n:
                    child_width = 1 << (n - level - 1)
                    lower_mask = (1 << child_width) - 1
                    next_lookup = {
                        mask: class_id
                        for class_id, mask in enumerate(level_classes[level + 1])
                    }
                    transitions = tuple(
                        (
                            next_lookup[mask & lower_mask],
                            next_lookup[mask >> child_width],
                        )
                        for mask in classes
                    )
                    next_count = len(level_classes[level + 1])
                    next_bits = (
                        0 if next_count <= 1 else (next_count - 1).bit_length()
                    )
                    counters["transition_bits"] += 2 * class_count * next_bits

                boundary_positions = _boundary_positions(
                    triples,
                    graph_mask,
                    ordering,
                    level,
                )
                boundary_states: set[tuple[int, ...]] = set()
                for prefix_index, assignment in enumerate(
                    prefix_assignments[level]
                ):
                    if prefix_violations[level][prefix_index] & graph_mask == 0:
                        boundary_states.add(
                            tuple(
                                assignment[position]
                                for position in boundary_positions
                            )
                        )
                boundary_count = len(boundary_states)
                counters["processed_valid_boundary_states"] += boundary_count
                level_signatures.append(
                    [
                        list(classes),
                        list(class_ids),
                        (
                            None
                            if transitions is None
                            else [list(value) for value in transitions]
                        ),
                        boundary_count,
                    ]
                )

            signature = [graph_mask, list(ordering), level_signatures]
            profile_digest.update(
                json.dumps(
                    signature,
                    separators=(",", ":"),
                    ensure_ascii=True,
                ).encode("utf-8")
            )
            profile_digest.update(b"\n")

    profiles = counters["profiles"]
    return {
        "n": n,
        "instances": 1 << len(triples),
        "orderings_per_instance": math.factorial(n),
        "profiles": profiles,
        "satisfiable_profiles": counters["satisfiable_profiles"],
        "unsatisfiable_profiles": profiles - counters["satisfiable_profiles"],
        "raw_prefixes": counters["raw_prefixes"],
        "exact_classes": counters["exact_classes"],
        "live_classes": counters["live_classes"],
        "processed_valid_boundary_states": counters[
            "processed_valid_boundary_states"
        ],
        "dense_unique_completion_bits": counters[
            "dense_unique_completion_bits"
        ],
        "assignment_map_bits": counters["assignment_map_bits"],
        "transition_bits": counters["transition_bits"],
        "max_classes_by_level": max_classes,
        "class_count_distributions": [
            {str(key): value for key, value in sorted(distribution.items())}
            for distribution in distributions
        ],
        "profile_sequence_sha256": profile_digest.hexdigest(),
    }


def profile_corpus_payload(max_vertices: int = 5) -> dict[str, object]:
    max_vertices = _validate_bound(max_vertices)
    counts = [_count_row(n) for n in range(max_vertices + 1)]
    total_keys = (
        "profiles",
        "satisfiable_profiles",
        "unsatisfiable_profiles",
        "raw_prefixes",
        "exact_classes",
        "live_classes",
        "processed_valid_boundary_states",
        "dense_unique_completion_bits",
        "assignment_map_bits",
        "transition_bits",
    )
    totals = {
        key: sum(int(row[key]) for row in counts)
        for key in total_keys
    }
    return {
        "format": FORMAT,
        "domain": f"all-labelled-instance-ordering-pairs-n-le-{max_vertices}",
        "generator": GENERATOR,
        "computation": "finite-exhaustive",
        "counts": counts,
        "totals": totals,
    }


def profile_corpus_record(max_vertices: int = 5) -> dict[str, object]:
    payload = profile_corpus_payload(max_vertices)
    payload_bytes = json.dumps(
        payload,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return {
        **payload,
        "payload_sha256": hashlib.sha256(payload_bytes).hexdigest(),
    }


def profile_corpus_bytes(max_vertices: int = 5) -> bytes:
    return json.dumps(
        profile_corpus_record(max_vertices),
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def verify_profile_corpus_record(record: object) -> bool:
    if type(record) is not dict or "payload_sha256" not in record:
        return False
    payload = {
        key: value for key, value in record.items() if key != "payload_sha256"
    }
    payload_bytes = json.dumps(
        payload,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return record["payload_sha256"] == hashlib.sha256(payload_bytes).hexdigest()
