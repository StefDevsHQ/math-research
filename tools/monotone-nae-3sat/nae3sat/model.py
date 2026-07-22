"""Canonical labelled 3-uniform hypergraph model and witness verification."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence, TypeAlias

from .errors import ColoringError, ValidationError

Vertex: TypeAlias = int
Edge: TypeAlias = tuple[Vertex, Vertex, Vertex]
Coloring: TypeAlias = tuple[int, ...]


def _is_strict_int(value: object) -> bool:
    return type(value) is int


def _validate_n(n: object) -> int:
    if not _is_strict_int(n):
        raise ValidationError("vertex count n must be an integer, not a Boolean or other numeric type")
    if n < 0:
        raise ValidationError("vertex count n must be nonnegative")
    return n


def _validate_canonical_edge(edge: object, n: int) -> Edge:
    if type(edge) is not tuple:
        raise ValidationError("canonical edges must be tuples")
    if len(edge) != 3:
        raise ValidationError("every edge must contain exactly three vertices")
    if any(not _is_strict_int(vertex) for vertex in edge):
        raise ValidationError("edge vertices must be integers, not Booleans or other numeric types")
    u, v, w = edge
    if not (0 <= u < v < w < n):
        raise ValidationError("canonical edge vertices must be strictly increasing and lie in the range [0, n)")
    return edge


@dataclass(frozen=True, slots=True)
class Hypergraph3:
    n: int
    edges: tuple[Edge, ...]

    def __post_init__(self) -> None:
        n = _validate_n(self.n)
        if type(self.edges) is not tuple:
            raise ValidationError("canonical edge collection must be a tuple")
        previous: Edge | None = None
        for edge in self.edges:
            canonical_edge = _validate_canonical_edge(edge, n)
            if previous is not None and not previous < canonical_edge:
                raise ValidationError("canonical edges must be strictly lexicographically increasing with no duplicates")
            previous = canonical_edge


@dataclass(frozen=True, slots=True)
class RelabeledHypergraph3:
    graph: Hypergraph3
    new_to_old: tuple[Vertex, ...]

    def __post_init__(self) -> None:
        if not isinstance(self.graph, Hypergraph3):
            raise ValidationError("graph must be a Hypergraph3 instance")
        if type(self.new_to_old) is not tuple:
            raise ValidationError("new_to_old must be a tuple")
        if len(self.new_to_old) != self.graph.n:
            raise ValidationError("new_to_old length must equal the relabelled graph vertex count")
        previous: int | None = None
        for vertex in self.new_to_old:
            if not _is_strict_int(vertex) or vertex < 0:
                raise ValidationError("new_to_old entries must be nonnegative integers")
            if previous is not None and vertex <= previous:
                raise ValidationError("new_to_old must be strictly increasing")
            previous = vertex


def normalize_instance(n: int, edges: Iterable[Sequence[int]]) -> Hypergraph3:
    n = _validate_n(n)
    if isinstance(edges, (str, bytes, bytearray)):
        raise ValidationError("edges must be an iterable of three-vertex sequences")
    try:
        iterator = iter(edges)
    except TypeError as exc:
        raise ValidationError("edges must be iterable") from exc
    normalized_edges: set[Edge] = set()
    for raw_edge in iterator:
        if isinstance(raw_edge, (str, bytes, bytearray)):
            raise ValidationError("each edge must be a sequence of exactly three integers")
        try:
            edge_values = tuple(raw_edge)
        except TypeError as exc:
            raise ValidationError("each edge must be iterable") from exc
        if len(edge_values) != 3:
            raise ValidationError("every edge must contain exactly three vertices")
        if any(not _is_strict_int(vertex) for vertex in edge_values):
            raise ValidationError("edge vertices must be integers, not Booleans or other numeric types")
        if len(set(edge_values)) != 3:
            raise ValidationError("an edge cannot repeat a vertex")
        if any(vertex < 0 or vertex >= n for vertex in edge_values):
            raise ValidationError("edge vertex lies outside the range [0, n)")
        normalized_edges.add(tuple(sorted(edge_values)))
    return Hypergraph3(n=n, edges=tuple(sorted(normalized_edges)))


def incidence_components(instance: Hypergraph3) -> tuple[tuple[int, ...], ...]:
    if not isinstance(instance, Hypergraph3):
        raise ValidationError("instance must be a Hypergraph3")
    if instance.n == 0:
        return ()
    adjacency: list[list[int]] = [[] for _ in range(instance.n)]
    for u, v, w in instance.edges:
        adjacency[u].extend((v, w)); adjacency[v].extend((u, w)); adjacency[w].extend((u, v))
    component_of = [-1] * instance.n
    count = 0
    for start in range(instance.n):
        if component_of[start] != -1:
            continue
        component_of[start] = count
        stack = [start]
        while stack:
            vertex = stack.pop()
            for neighbour in adjacency[vertex]:
                if component_of[neighbour] == -1:
                    component_of[neighbour] = count
                    stack.append(neighbour)
        count += 1
    members: list[list[int]] = [[] for _ in range(count)]
    for vertex, component in enumerate(component_of):
        members[component].append(vertex)
    return tuple(tuple(component) for component in members)


def _selected(instance: Hypergraph3, vertices: Iterable[int]) -> tuple[int, ...]:
    if isinstance(vertices, (str, bytes, bytearray)):
        raise ValidationError("vertices must be an iterable of integer labels")
    try:
        values = tuple(vertices)
    except TypeError as exc:
        raise ValidationError("vertices must be iterable") from exc
    if any(type(v) is not int for v in values):
        raise ValidationError("selected vertices must be integers, not Booleans")
    if len(set(values)) != len(values):
        raise ValidationError("selected vertices must not contain duplicates")
    if any(v < 0 or v >= instance.n for v in values):
        raise ValidationError("selected vertex lies outside the instance range")
    return tuple(sorted(values))


def induced_subinstance(instance: Hypergraph3, vertices: Iterable[int]) -> RelabeledHypergraph3:
    selected = _selected(instance, vertices)
    old_to_new = {old: new for new, old in enumerate(selected)}
    chosen = set(selected)
    edges = [(old_to_new[u], old_to_new[v], old_to_new[w]) for u, v, w in instance.edges if u in chosen and v in chosen and w in chosen]
    return RelabeledHypergraph3(normalize_instance(len(selected), edges), selected)


def active_core(instance: Hypergraph3) -> RelabeledHypergraph3:
    return induced_subinstance(instance, sorted({v for edge in instance.edges for v in edge}))


def _validate_coloring(instance: Hypergraph3, coloring: Sequence[int]) -> tuple[int, ...]:
    if isinstance(coloring, (str, bytes, bytearray)):
        raise ColoringError("colouring must be a non-string sequence")
    try:
        if len(coloring) != instance.n:
            raise ColoringError("colouring length does not equal instance vertex count")
        values = tuple(coloring)
    except TypeError as exc:
        raise ColoringError("colouring must be a finite sequence") from exc
    if any(type(v) is not int or v not in (0, 1) for v in values):
        raise ColoringError("colouring entries must be the integers 0 or 1, excluding Booleans")
    return values


def first_violated_edge(instance: Hypergraph3, coloring: Sequence[int]) -> Edge | None:
    values = _validate_coloring(instance, coloring)
    for edge in instance.edges:
        u, v, w = edge
        if values[u] == values[v] == values[w]:
            return edge
    return None


def verify_coloring(instance: Hypergraph3, coloring: Sequence[int]) -> bool:
    return first_violated_edge(instance, coloring) is None
