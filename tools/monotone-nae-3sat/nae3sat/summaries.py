"""VS-06 candidate summaries and exact collision witnesses."""

from __future__ import annotations

import itertools
from collections import deque
from collections.abc import Sequence as SequenceABC
from typing import Sequence

from .controls import processed_boundary, vertex_occurrences
from .errors import ValidationError
from .model import Hypergraph3, induced_subinstance, normalize_instance
from .obstructions import fano_plane
from .oracle import count_satisfying_assignments, solve_exact
from .profile import extension_mask, validate_ordering

GraphEdge = tuple[int, int]
Graph = tuple[int, tuple[GraphEdge, ...]]


def _require_instance(instance: object) -> Hypergraph3:
    if not isinstance(instance, Hypergraph3):
        raise ValidationError("instance must be a Hypergraph3")
    return instance


def _strict_nonnegative_int(value: object, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValidationError(f"{name} must be a nonnegative integer excluding Booleans")
    return value


def pair_codegree_matrix(instance: Hypergraph3) -> tuple[tuple[int, ...], ...]:
    instance = _require_instance(instance)
    values = [[0] * instance.n for _ in range(instance.n)]
    for edge in instance.edges:
        for left, right in itertools.combinations(edge, 2):
            values[left][right] += 1
            values[right][left] += 1
    return tuple(tuple(row) for row in values)


def degree_sequence_summary(instance: Hypergraph3) -> tuple[int, ...]:
    return tuple(sorted(vertex_occurrences(_require_instance(instance))))


def edge_intersection_summary(instance: Hypergraph3) -> tuple[int, ...]:
    instance = _require_instance(instance)
    return tuple(
        sorted(
            len(set(left) & set(right))
            for index, left in enumerate(instance.edges)
            for right in instance.edges[index + 1 :]
        )
    )


def pair_codegree_multiset_summary(instance: Hypergraph3) -> tuple[int, ...]:
    instance = _require_instance(instance)
    matrix = pair_codegree_matrix(instance)
    return tuple(
        sorted(
            matrix[left][right]
            for left in range(instance.n)
            for right in range(left + 1, instance.n)
        )
    )


def parity_summary(instance: Hypergraph3) -> tuple[object, ...]:
    instance = _require_instance(instance)
    degrees = vertex_occurrences(instance)
    pair_values = pair_codegree_multiset_summary(instance)
    return (
        instance.n % 2,
        len(instance.edges) % 2,
        tuple(sorted(value % 2 for value in degrees)),
        tuple(sorted(value % 2 for value in pair_values)),
    )


def second_moment_summary(instance: Hypergraph3) -> tuple[int, ...]:
    instance = _require_instance(instance)
    degrees = vertex_occurrences(instance)
    pair_values = pair_codegree_multiset_summary(instance)
    return (
        instance.n,
        len(instance.edges),
        sum(degrees),
        sum(value * value for value in degrees),
        sum(pair_values),
        sum(value * value for value in pair_values),
    )


def incidence_gram_matrix(instance: Hypergraph3) -> tuple[tuple[int, ...], ...]:
    instance = _require_instance(instance)
    degrees = vertex_occurrences(instance)
    pair_values = pair_codegree_matrix(instance)
    return tuple(
        tuple(
            degrees[row] if row == column else pair_values[row][column]
            for column in range(instance.n)
        )
        for row in range(instance.n)
    )


def _matrix_product(
    left: Sequence[Sequence[int]],
    right: Sequence[Sequence[int]],
) -> list[list[int]]:
    size = len(left)
    return [
        [
            sum(
                left[row][index] * right[index][column]
                for index in range(size)
            )
            for column in range(size)
        ]
        for row in range(size)
    ]


def characteristic_polynomial(matrix: object) -> tuple[int, ...]:
    if isinstance(matrix, (str, bytes, bytearray)) or not isinstance(
        matrix, SequenceABC
    ):
        raise ValidationError("matrix must be a finite square integer sequence")
    rows = tuple(matrix)
    size = len(rows)
    if any(
        isinstance(row, (str, bytes, bytearray))
        or not isinstance(row, SequenceABC)
        or len(row) != size
        for row in rows
    ):
        raise ValidationError("matrix must be square")
    values = tuple(tuple(entry for entry in row) for row in rows)
    if any(type(entry) is not int for row in values for entry in row):
        raise ValidationError("matrix entries must be integers excluding Booleans")

    identity = [
        [1 if row == column else 0 for column in range(size)]
        for row in range(size)
    ]
    accumulator = [row[:] for row in identity]
    coefficients = [1]
    for degree in range(1, size + 1):
        product = _matrix_product(values, accumulator)
        trace = sum(product[index][index] for index in range(size))
        quotient, remainder = divmod(-trace, degree)
        if remainder:
            raise AssertionError(
                "integer characteristic-polynomial recurrence failed"
            )
        coefficients.append(quotient)
        accumulator = [
            [
                product[row][column]
                + (quotient if row == column else 0)
                for column in range(size)
            ]
            for row in range(size)
        ]
    return tuple(coefficients)


def incidence_gram_spectrum_summary(
    instance: Hypergraph3,
) -> tuple[int, ...]:
    return characteristic_polynomial(
        incidence_gram_matrix(_require_instance(instance))
    )


def root_gac_summary(
    instance: Hypergraph3,
) -> tuple[tuple[int, int], ...]:
    """Return the generalized-arc-consistency fixed point at the root.

    Every strict NAE triple gives each value of each variable a supporting local
    tuple while all domains are {0,1}; therefore root GAC never prunes.
    """

    instance = _require_instance(instance)
    return tuple((0, 1) for _ in range(instance.n))


def proper_induced_satisfiability_summary(
    instance: Hypergraph3,
    *,
    maximum_size: int,
) -> tuple[bool, ...]:
    instance = _require_instance(instance)
    maximum_size = _strict_nonnegative_int(
        maximum_size, "maximum induced size"
    )
    if maximum_size >= instance.n:
        raise ValidationError(
            "maximum induced size must be strictly smaller than n"
        )
    return tuple(
        solve_exact(induced_subinstance(instance, vertices).graph).satisfiable
        for size in range(maximum_size + 1)
        for vertices in itertools.combinations(range(instance.n), size)
    )


def _strict_prefix(prefix_bits: object, maximum: int) -> tuple[int, ...]:
    if isinstance(prefix_bits, (str, bytes, bytearray)) or not isinstance(
        prefix_bits, SequenceABC
    ):
        raise ValidationError(
            "prefix bits must be a finite non-string sequence"
        )
    values = tuple(prefix_bits)
    if len(values) > maximum:
        raise ValidationError("prefix is longer than the ordering")
    if any(
        type(value) is not int or value not in (0, 1)
        for value in values
    ):
        raise ValidationError("prefix bits must be strict integer bits")
    return values


def processed_prefix_consistent(
    instance: Hypergraph3,
    ordering: object,
    prefix_bits: object,
) -> bool:
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    prefix = _strict_prefix(prefix_bits, instance.n)
    positions = {
        vertex: position
        for position, vertex in enumerate(ordering[: len(prefix)])
    }
    for edge in instance.edges:
        if all(vertex in positions for vertex in edge):
            values = tuple(prefix[positions[vertex]] for vertex in edge)
            if values[0] == values[1] == values[2]:
                return False
    return True


def exact_boundary_summary(
    instance: Hypergraph3,
    ordering: object,
    prefix_bits: object,
) -> tuple[bool, tuple[int, ...]]:
    instance = _require_instance(instance)
    ordering = validate_ordering(instance, ordering)
    prefix = _strict_prefix(prefix_bits, instance.n)
    boundary = processed_boundary(instance, ordering, len(prefix))
    positions = {
        vertex: position
        for position, vertex in enumerate(ordering[: len(prefix)])
    }
    return (
        processed_prefix_consistent(instance, ordering, prefix),
        tuple(prefix[positions[vertex]] for vertex in boundary),
    )


def boundary_weight_summary(
    instance: Hypergraph3,
    ordering: object,
    prefix_bits: object,
) -> tuple[bool, int, int]:
    consistent, boundary_bits = exact_boundary_summary(
        instance, ordering, prefix_bits
    )
    return consistent, len(boundary_bits), sum(boundary_bits)


def boundary_parity_summary(
    instance: Hypergraph3,
    ordering: object,
    prefix_bits: object,
) -> tuple[bool, int, int]:
    consistent, width, weight = boundary_weight_summary(
        instance, ordering, prefix_bits
    )
    return consistent, width, weight % 2


def exact_completion_mask(
    instance: Hypergraph3,
    ordering: object,
    prefix_bits: object,
) -> int:
    return extension_mask(
        _require_instance(instance), ordering, prefix_bits
    )


def _normalize_graph(n: object, edges: object) -> Graph:
    n = _strict_nonnegative_int(n, "graph vertex count")
    if isinstance(edges, (str, bytes, bytearray)):
        raise ValidationError("graph edges must be iterable")
    try:
        iterator = iter(edges)
    except TypeError as exc:
        raise ValidationError("graph edges must be iterable") from exc
    values: set[GraphEdge] = set()
    for raw in iterator:
        if isinstance(raw, (str, bytes, bytearray)) or not isinstance(
            raw, SequenceABC
        ):
            raise ValidationError(
                "graph edge must be a two-vertex sequence"
            )
        edge = tuple(raw)
        if len(edge) != 2 or any(type(vertex) is not int for vertex in edge):
            raise ValidationError(
                "graph edge must contain two integer vertices"
            )
        left, right = edge
        if (
            left == right
            or left < 0
            or right < 0
            or left >= n
            or right >= n
        ):
            raise ValidationError(
                "graph edge vertices must be distinct and in range"
            )
        values.add((left, right) if left < right else (right, left))
    return n, tuple(sorted(values))


def cycle_union(lengths: object) -> Graph:
    if isinstance(lengths, (str, bytes, bytearray)) or not isinstance(
        lengths, SequenceABC
    ):
        raise ValidationError("cycle lengths must be a finite sequence")
    values = tuple(
        _strict_nonnegative_int(length, "cycle length")
        for length in lengths
    )
    if any(length < 3 for length in values):
        raise ValidationError("every cycle length must be at least three")
    edges: list[GraphEdge] = []
    offset = 0
    for length in values:
        edges.extend(
            (offset + index, offset + ((index + 1) % length))
            for index in range(length)
        )
        offset += length
    return _normalize_graph(offset, edges)


def anchored_inequality_instance(graph: Graph) -> Hypergraph3:
    n, edges = _normalize_graph(*graph)
    triples = [
        (anchor, left + 2, right + 2)
        for anchor in (0, 1)
        for left, right in edges
    ]
    return normalize_instance(n + 2, triples)


def _graph_adjacency(graph: Graph) -> tuple[tuple[int, ...], ...]:
    n, edges = _normalize_graph(*graph)
    adjacency = [set() for _ in range(n)]
    for left, right in edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    return tuple(tuple(sorted(values)) for values in adjacency)


def graph_is_bipartite(graph: Graph) -> bool:
    adjacency = _graph_adjacency(graph)
    colours = [-1] * len(adjacency)
    for start in range(len(adjacency)):
        if colours[start] != -1:
            continue
        colours[start] = 0
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            for neighbour in adjacency[vertex]:
                if colours[neighbour] == -1:
                    colours[neighbour] = 1 - colours[vertex]
                    queue.append(neighbour)
                elif colours[neighbour] == colours[vertex]:
                    return False
    return True


def _rooted_radius_code(
    graph: Graph,
    root: int,
    radius: int,
) -> tuple[object, ...]:
    n, _ = _normalize_graph(*graph)
    root = _strict_nonnegative_int(root, "root")
    radius = _strict_nonnegative_int(radius, "radius")
    if root >= n:
        raise ValidationError("root lies outside the graph")
    adjacency = _graph_adjacency(graph)
    distance = {root: 0}
    queue = deque([root])
    while queue:
        vertex = queue.popleft()
        if distance[vertex] == radius:
            continue
        for neighbour in adjacency[vertex]:
            if neighbour not in distance:
                distance[neighbour] = distance[vertex] + 1
                queue.append(neighbour)

    remaining = tuple(vertex for vertex in distance if vertex != root)
    best: tuple[object, ...] | None = None
    for permutation in itertools.permutations(remaining):
        ordering = (root, *permutation)
        labels = tuple(
            (distance[vertex], len(adjacency[vertex]))
            for vertex in ordering
        )
        edge_bits = tuple(
            int(ordering[right] in adjacency[ordering[left]])
            for left in range(len(ordering))
            for right in range(left + 1, len(ordering))
        )
        candidate = labels, edge_bits
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    return best


def bounded_radius_summary(
    graph: Graph,
    radius: int,
) -> tuple[tuple[object, ...], ...]:
    n, _ = _normalize_graph(*graph)
    radius = _strict_nonnegative_int(radius, "radius")
    return tuple(
        sorted(
            _rooted_radius_code(graph, root, radius)
            for root in range(n)
        )
    )


def bounded_radius_collision(radius: int) -> tuple[Graph, Graph]:
    radius = _strict_nonnegative_int(radius, "radius")
    if radius < 1:
        raise ValidationError("collision radius must be at least one")
    unsatisfiable = cycle_union(
        (2 * radius + 3, 2 * radius + 3)
    )
    satisfiable = cycle_union(
        (2 * radius + 2, 2 * radius + 4)
    )
    return unsatisfiable, satisfiable


def star_six() -> Hypergraph3:
    return normalize_instance(
        6,
        (
            (0, left, right)
            for left, right in itertools.combinations(range(1, 6), 2)
        ),
    )


def complete_five_plus_isolate() -> Hypergraph3:
    return normalize_instance(6, itertools.combinations(range(5), 3))


def degree_collision_satisfiable() -> Hypergraph3:
    return normalize_instance(
        6,
        (
            (0, 1, 3),
            (0, 1, 4),
            (0, 2, 3),
            (0, 2, 4),
            (0, 3, 4),
            (0, 3, 5),
            (0, 4, 5),
            (1, 2, 3),
            (1, 2, 4),
            (1, 2, 5),
        ),
    )


def degree_collision_unsatisfiable() -> Hypergraph3:
    return normalize_instance(
        6,
        (
            (0, 1, 2),
            (0, 1, 3),
            (0, 1, 4),
            (0, 2, 3),
            (0, 2, 4),
            (0, 3, 5),
            (0, 4, 5),
            (1, 2, 5),
            (1, 3, 4),
            (2, 3, 4),
        ),
    )


def pair_codegree_collision_satisfiable() -> Hypergraph3:
    return normalize_instance(
        6,
        (
            (0, 1, 3),
            (0, 1, 5),
            (0, 2, 3),
            (0, 2, 4),
            (0, 3, 5),
            (0, 4, 5),
            (1, 2, 3),
            (1, 2, 4),
            (1, 2, 5),
            (1, 3, 4),
        ),
    )


def local_consistency_star() -> Hypergraph3:
    pairs = tuple(itertools.combinations(range(1, 7), 2))[:7]
    return normalize_instance(
        7,
        ((0, left, right) for left, right in pairs),
    )


def fano_local_obstruction() -> Hypergraph3:
    return fano_plane()


def solution_summary(instance: Hypergraph3) -> dict[str, object]:
    instance = _require_instance(instance)
    result = solve_exact(instance)
    return {
        "satisfiable": result.satisfiable,
        "solution_count": count_satisfying_assignments(instance),
        "least_witness": (
            None if result.witness is None else list(result.witness)
        ),
    }
