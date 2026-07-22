"""Certificates for the all-ordering PCRNF lower bound."""

from __future__ import annotations

from collections.abc import Iterable, Sequence as SequenceABC
from dataclasses import dataclass

from .errors import ValidationError
from .model import Hypergraph3, normalize_instance

GraphEdge = tuple[int, int]
CrossingEdge = tuple[int, int]


def _strict_vertex_count(value: object) -> int:
    if type(value) is not int or value < 0:
        raise ValidationError("graph vertex count must be a nonnegative integer")
    return value


def normalize_graph_edges(
    vertex_count: int,
    edges: Iterable[SequenceABC[int]],
) -> tuple[GraphEdge, ...]:
    """Return one simple labelled graph on ``range(vertex_count)``."""
    vertex_count = _strict_vertex_count(vertex_count)
    if isinstance(edges, (str, bytes, bytearray)):
        raise ValidationError("graph edges must be an iterable of pairs")
    normalized: set[GraphEdge] = set()
    try:
        iterator = iter(edges)
    except TypeError as exc:
        raise ValidationError("graph edges must be iterable") from exc
    for raw_edge in iterator:
        if isinstance(raw_edge, (str, bytes, bytearray)):
            raise ValidationError("each graph edge must be a pair")
        try:
            values = tuple(raw_edge)
        except TypeError as exc:
            raise ValidationError("each graph edge must be iterable") from exc
        if len(values) != 2:
            raise ValidationError("each graph edge must contain exactly two vertices")
        left, right = values
        if (
            type(left) is not int
            or type(right) is not int
            or left == right
            or left < 0
            or right < 0
            or left >= vertex_count
            or right >= vertex_count
        ):
            raise ValidationError("graph edges must join distinct vertices in range")
        normalized.add((min(left, right), max(left, right)))
    return tuple(sorted(normalized))


def central_lift(
    vertex_count: int,
    edges: Iterable[SequenceABC[int]],
) -> Hypergraph3:
    """Lift graph edges ``uv`` to NAE triples ``{u,v,c}`` with ``c=n``."""
    graph_edges = normalize_graph_edges(vertex_count, edges)
    center = vertex_count
    return normalize_instance(
        vertex_count + 1,
        ((left, right, center) for left, right in graph_edges),
    )


def _validate_ordering(vertex_count: int, ordering: object) -> tuple[int, ...]:
    if isinstance(ordering, (str, bytes, bytearray)) or not isinstance(
        ordering,
        SequenceABC,
    ):
        raise ValidationError("ordering must be a finite sequence")
    values = tuple(ordering)
    if len(values) != vertex_count + 1 or set(values) != set(
        range(vertex_count + 1)
    ):
        raise ValidationError("ordering must permute graph vertices and the center")
    return values


def _adjacency(
    vertex_count: int,
    edges: tuple[GraphEdge, ...],
) -> tuple[frozenset[int], ...]:
    neighbours = [set() for _ in range(vertex_count)]
    for left, right in edges:
        neighbours[left].add(right)
        neighbours[right].add(left)
    return tuple(frozenset(row) for row in neighbours)


@dataclass(frozen=True, slots=True)
class CutMatchingCertificate:
    """One balanced-prefix cut and a crossing induced matching."""

    level: int
    prefix_vertices: tuple[int, ...]
    suffix_vertices: tuple[int, ...]
    crossing_edges: tuple[CrossingEdge, ...]
    induced_matching: tuple[CrossingEdge, ...]
    maximum_degree: int

    def __post_init__(self) -> None:
        if type(self.level) is not int or self.level < 0:
            raise ValidationError("certificate level must be nonnegative")
        if type(self.maximum_degree) is not int or self.maximum_degree < 0:
            raise ValidationError("maximum degree must be nonnegative")
        if type(self.prefix_vertices) is not tuple or type(self.suffix_vertices) is not tuple:
            raise ValidationError("certificate sides must be tuples")
        if type(self.crossing_edges) is not tuple or type(self.induced_matching) is not tuple:
            raise ValidationError("certificate edge collections must be tuples")

    @property
    def semantic_state_lower_bound(self) -> int:
        return 1 << len(self.induced_matching)


def balanced_prefix_cut(
    vertex_count: int,
    ordering: object,
) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    """Cut after the first ``floor(n/2)`` graph vertices, ignoring the center."""
    vertex_count = _strict_vertex_count(vertex_count)
    ordering = _validate_ordering(vertex_count, ordering)
    target = vertex_count // 2
    if target == 0:
        return 0, (), tuple(range(vertex_count))
    seen: list[int] = []
    level = 0
    for position, vertex in enumerate(ordering):
        if vertex < vertex_count:
            seen.append(vertex)
            if len(seen) == target:
                level = position + 1
                break
    prefix = tuple(sorted(seen))
    prefix_set = frozenset(prefix)
    suffix = tuple(
        vertex for vertex in range(vertex_count) if vertex not in prefix_set
    )
    return level, prefix, suffix


def cut_induced_matching_certificate(
    vertex_count: int,
    edges: Iterable[SequenceABC[int]],
    ordering: object,
) -> CutMatchingCertificate:
    """Greedily extract an induced matching from the balanced crossing cut."""
    graph_edges = normalize_graph_edges(vertex_count, edges)
    ordering = _validate_ordering(vertex_count, ordering)
    level, prefix, suffix = balanced_prefix_cut(vertex_count, ordering)
    prefix_set = frozenset(prefix)
    suffix_set = frozenset(suffix)
    adjacency = _adjacency(vertex_count, graph_edges)
    crossing: set[CrossingEdge] = set()
    for left, right in graph_edges:
        if left in prefix_set and right in suffix_set:
            crossing.add((left, right))
        elif right in prefix_set and left in suffix_set:
            crossing.add((right, left))
    remaining = set(crossing)
    selected: list[CrossingEdge] = []
    while remaining:
        left, right = min(remaining)
        selected.append((left, right))
        forbidden = {left, right} | set(adjacency[left]) | set(adjacency[right])
        remaining = {
            edge
            for edge in remaining
            if edge[0] not in forbidden and edge[1] not in forbidden
        }
    maximum_degree = max((len(row) for row in adjacency), default=0)
    return CutMatchingCertificate(
        level=level,
        prefix_vertices=prefix,
        suffix_vertices=suffix,
        crossing_edges=tuple(sorted(crossing)),
        induced_matching=tuple(selected),
        maximum_degree=maximum_degree,
    )


def certificate_prefixes(
    vertex_count: int,
    ordering: object,
    certificate: CutMatchingCertificate,
) -> tuple[tuple[int, ...], ...]:
    """Return the ``2^k`` live prefixes encoded by one induced matching."""
    ordering = _validate_ordering(vertex_count, ordering)
    if certificate.level > len(ordering):
        raise ValidationError("certificate level exceeds the ordering")
    left_index = {
        left: index
        for index, (left, _right) in enumerate(certificate.induced_matching)
    }
    prefixes: list[tuple[int, ...]] = []
    for mask in range(1 << len(certificate.induced_matching)):
        values: list[int] = []
        for vertex in ordering[: certificate.level]:
            if vertex == vertex_count:
                values.append(0)
            elif vertex in left_index:
                values.append(0 if mask & (1 << left_index[vertex]) else 1)
            else:
                values.append(1)
        prefixes.append(tuple(values))
    return tuple(prefixes)


def is_induced_matching(
    vertex_count: int,
    edges: Iterable[SequenceABC[int]],
    matching: Iterable[SequenceABC[int]],
) -> bool:
    """Check that matching endpoints induce exactly the selected edges."""
    graph_edges = normalize_graph_edges(vertex_count, edges)
    selected = normalize_graph_edges(vertex_count, matching)
    edge_set = frozenset(graph_edges)
    endpoints: list[int] = []
    for left, right in selected:
        if (left, right) not in edge_set:
            return False
        endpoints.extend((left, right))
    if len(endpoints) != len(set(endpoints)):
        return False
    endpoint_set = frozenset(endpoints)
    induced_edges = {
        edge for edge in graph_edges if edge[0] in endpoint_set and edge[1] in endpoint_set
    }
    return induced_edges == set(selected)


def verify_greedy_bound(certificate: CutMatchingCertificate) -> bool:
    """Verify ``|F| <= 2 d(d+1)|M|`` for the greedy certificate."""
    degree = certificate.maximum_degree
    if not certificate.crossing_edges:
        return not certificate.induced_matching
    return len(certificate.crossing_edges) <= (
        2 * degree * (degree + 1) * len(certificate.induced_matching)
    )
