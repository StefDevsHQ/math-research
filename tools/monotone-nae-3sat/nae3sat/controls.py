"""Exact tractable controls for VS-04 calibration."""

from __future__ import annotations

import itertools
from collections import deque
from collections.abc import Iterable, Sequence as SequenceABC
from dataclasses import dataclass
from typing import Sequence

from .errors import ValidationError
from .model import Hypergraph3, verify_coloring
from .profile import validate_ordering


def _strict_nonnegative_int(value: object, name: str) -> int:
    if type(value) is not int or value < 0:
        raise ValidationError(f"{name} must be a nonnegative integer")
    return value


def _require_sequence(value: object, name: str) -> Sequence[object]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, SequenceABC):
        raise ValidationError(f"{name} must be a non-string finite sequence")
    return value


@dataclass(frozen=True, slots=True)
class Graph2:
    n: int
    edges: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        n = _strict_nonnegative_int(self.n, "vertex count")
        if type(self.edges) is not tuple:
            raise ValidationError("graph edges must be a tuple")
        previous: tuple[int, int] | None = None
        for edge in self.edges:
            if type(edge) is not tuple or len(edge) != 2:
                raise ValidationError("canonical graph edges must be two-vertex tuples")
            u, v = edge
            if type(u) is not int or type(v) is not int or not (0 <= u < v < n):
                raise ValidationError("canonical graph edges must be increasing and in range")
            if previous is not None and not previous < edge:
                raise ValidationError("canonical graph edges must be strictly ordered without duplicates")
            previous = edge


@dataclass(frozen=True, slots=True)
class Graph2Result:
    bipartite: bool
    witness: tuple[int, ...] | None
    components: int
    solution_count: int
    conflict_edge: tuple[int, int] | None

    def __post_init__(self) -> None:
        if type(self.bipartite) is not bool:
            raise ValidationError("bipartite must be Boolean")
        if type(self.components) is not int or self.components < 0:
            raise ValidationError("components must be nonnegative")
        if type(self.solution_count) is not int or self.solution_count < 0:
            raise ValidationError("solution count must be nonnegative")
        if self.bipartite:
            if type(self.witness) is not tuple or self.conflict_edge is not None:
                raise ValidationError("bipartite results require a witness and no conflict")
            if self.solution_count != 1 << self.components:
                raise ValidationError("bipartite solution count must equal two to the component count")
        else:
            if self.witness is not None or self.solution_count != 0:
                raise ValidationError("non-bipartite results have no witness and zero solutions")
            if type(self.conflict_edge) is not tuple or len(self.conflict_edge) != 2:
                raise ValidationError("non-bipartite results require a conflict edge")


def _require_graph(graph: object) -> Graph2:
    if not isinstance(graph, Graph2):
        raise ValidationError("graph must be a Graph2")
    return graph


def normalize_graph2(n: int, edges: Iterable[Sequence[int]]) -> Graph2:
    n = _strict_nonnegative_int(n, "vertex count")
    if isinstance(edges, (str, bytes, bytearray)):
        raise ValidationError("edges must be iterable")
    try:
        iterator = iter(edges)
    except TypeError as exc:
        raise ValidationError("edges must be iterable") from exc
    result: set[tuple[int, int]] = set()
    for raw in iterator:
        values = _require_sequence(raw, "edge")
        if len(values) != 2:
            raise ValidationError("every graph edge must contain exactly two vertices")
        u, v = values
        if type(u) is not int or type(v) is not int:
            raise ValidationError("graph vertices must be integers excluding Booleans")
        if u == v or u < 0 or v < 0 or u >= n or v >= n:
            raise ValidationError("graph edges must contain distinct in-range vertices")
        result.add((u, v) if u < v else (v, u))
    return Graph2(n, tuple(sorted(result)))


def verify_graph2_coloring(graph: Graph2, coloring: Sequence[int]) -> bool:
    graph = _require_graph(graph)
    values = _require_sequence(coloring, "colouring")
    if len(values) != graph.n or any(type(bit) is not int or bit not in (0, 1) for bit in values):
        raise ValidationError("colouring must contain exactly one binary integer per vertex")
    return all(values[u] != values[v] for u, v in graph.edges)


def solve_graph2(graph: Graph2) -> Graph2Result:
    graph = _require_graph(graph)
    adjacency: list[list[int]] = [[] for _ in range(graph.n)]
    for u, v in graph.edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    relative = [-1] * graph.n
    components: list[tuple[int, ...]] = []
    conflict: tuple[int, int] | None = None
    for start in range(graph.n):
        if relative[start] != -1:
            continue
        relative[start] = 0
        members: list[int] = []
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            members.append(vertex)
            for neighbour in adjacency[vertex]:
                if relative[neighbour] == -1:
                    relative[neighbour] = 1 - relative[vertex]
                    queue.append(neighbour)
                elif relative[neighbour] == relative[vertex] and conflict is None:
                    conflict = (vertex, neighbour) if vertex < neighbour else (neighbour, vertex)
        components.append(tuple(sorted(members)))
    if conflict is not None:
        return Graph2Result(False, None, len(components), 0, conflict)
    witness = list(relative)
    for component in components:
        least = component[0]
        if witness[least] == 1:
            for vertex in component:
                witness[vertex] ^= 1
    result = tuple(witness)
    if not verify_graph2_coloring(graph, result):
        raise AssertionError("internal graph witness failed verification")
    return Graph2Result(True, result, len(components), 1 << len(components), None)


def labelled_graphs(n: int):
    n = _strict_nonnegative_int(n, "vertex count")
    edges = tuple(itertools.combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        yield Graph2(n, tuple(edge for index, edge in enumerate(edges) if mask & (1 << index)))


@dataclass(frozen=True, slots=True)
class XorSystem:
    n: int
    equations: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        n = _strict_nonnegative_int(self.n, "variable count")
        if type(self.equations) is not tuple:
            raise ValidationError("equations must be a tuple")
        previous: tuple[int, int] | None = None
        for equation in self.equations:
            if type(equation) is not tuple or len(equation) != 2:
                raise ValidationError("canonical equations must be (mask, rhs) tuples")
            mask, rhs = equation
            if type(mask) is not int or mask <= 0 or mask >= (1 << n):
                raise ValidationError("equation masks must be nonzero and fit the variable count")
            if type(rhs) is not int or rhs not in (0, 1):
                raise ValidationError("equation right-hand sides must be binary integers")
            if previous is not None and not previous < equation:
                raise ValidationError("canonical equations must be strictly ordered without duplicates")
            previous = equation


@dataclass(frozen=True, slots=True)
class XorResult:
    consistent: bool
    rank: int
    free_variables: int
    witness: tuple[int, ...] | None
    solution_count: int
    reduced_rows: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        if type(self.consistent) is not bool:
            raise ValidationError("consistent must be Boolean")
        if type(self.rank) is not int or self.rank < 0:
            raise ValidationError("rank must be nonnegative")
        if type(self.free_variables) is not int or self.free_variables < 0:
            raise ValidationError("free variable count must be nonnegative")
        if type(self.reduced_rows) is not tuple:
            raise ValidationError("reduced rows must be a tuple")
        if self.consistent:
            if type(self.witness) is not tuple or self.solution_count != 1 << self.free_variables:
                raise ValidationError("consistent XOR result requires witness and exact affine count")
        elif self.witness is not None or self.solution_count != 0:
            raise ValidationError("inconsistent XOR result has no witness and zero solutions")


def _require_xor(system: object) -> XorSystem:
    if not isinstance(system, XorSystem):
        raise ValidationError("system must be an XorSystem")
    return system


def normalize_xor_system(n: int, equations: Iterable[tuple[Iterable[int] | int, int]]) -> XorSystem:
    n = _strict_nonnegative_int(n, "variable count")
    if isinstance(equations, (str, bytes, bytearray)):
        raise ValidationError("equations must be iterable")
    try:
        iterator = iter(equations)
    except TypeError as exc:
        raise ValidationError("equations must be iterable") from exc
    result: set[tuple[int, int]] = set()
    for raw in iterator:
        values = _require_sequence(raw, "equation")
        if len(values) != 2:
            raise ValidationError("every equation must contain a left side and right side")
        left, rhs = values
        if type(rhs) is not int or rhs not in (0, 1):
            raise ValidationError("equation right-hand sides must be binary integers")
        if type(left) is int:
            mask = left
        else:
            if isinstance(left, (str, bytes, bytearray)):
                raise ValidationError("equation variables must be iterable")
            try:
                variables = tuple(left)
            except TypeError as exc:
                raise ValidationError("equation variables must be iterable") from exc
            mask = 0
            for vertex in variables:
                if type(vertex) is not int or vertex < 0 or vertex >= n:
                    raise ValidationError("equation variables must be distinct in-range integers")
                mask ^= 1 << vertex
        if mask <= 0 or mask >= (1 << n):
            raise ValidationError("equation left side must be a nonempty in-range parity mask")
        result.add((mask, rhs))
    return XorSystem(n, tuple(sorted(result)))


def _eliminate(n: int, equations: Sequence[tuple[int, int]]) -> tuple[bool, int, tuple[tuple[int, int], ...]]:
    rows = [mask | (rhs << n) for mask, rhs in equations]
    rank = 0
    for column in range(n):
        pivot = next((index for index in range(rank, len(rows)) if rows[index] & (1 << column)), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for index in range(len(rows)):
            if index != rank and rows[index] & (1 << column):
                rows[index] ^= rows[rank]
        rank += 1
    coefficient_mask = (1 << n) - 1
    consistent = all((row & coefficient_mask) != 0 or ((row >> n) & 1) == 0 for row in rows)
    reduced = tuple(sorted((row & coefficient_mask, (row >> n) & 1) for row in rows if row & coefficient_mask))
    return consistent, rank, reduced


def verify_xor_assignment(system: XorSystem, assignment: Sequence[int]) -> bool:
    system = _require_xor(system)
    values = _require_sequence(assignment, "assignment")
    if len(values) != system.n or any(type(bit) is not int or bit not in (0, 1) for bit in values):
        raise ValidationError("assignment must contain exactly one binary integer per variable")
    packed = sum(bit << index for index, bit in enumerate(values))
    return all((packed & mask).bit_count() % 2 == rhs for mask, rhs in system.equations)


def solve_xor(system: XorSystem) -> XorResult:
    system = _require_xor(system)
    consistent, rank, reduced = _eliminate(system.n, system.equations)
    if not consistent:
        return XorResult(False, rank, max(0, system.n - rank), None, 0, reduced)
    fixed: list[tuple[int, int]] = []
    witness: list[int] = []
    for variable in range(system.n):
        zero = (*system.equations, *fixed, (1 << variable, 0))
        zero_consistent, _, _ = _eliminate(system.n, zero)
        bit = 0 if zero_consistent else 1
        fixed.append((1 << variable, bit))
        witness.append(bit)
    result = tuple(witness)
    if not verify_xor_assignment(system, result):
        raise AssertionError("internal XOR witness failed verification")
    return XorResult(True, rank, system.n - rank, result, 1 << (system.n - rank), reduced)


def labelled_xor_systems(n: int):
    n = _strict_nonnegative_int(n, "variable count")
    equations = tuple((mask, rhs) for mask in range(1, 1 << n) for rhs in (0, 1))
    for selection in range(1 << len(equations)):
        yield XorSystem(n, tuple(equation for index, equation in enumerate(equations) if selection & (1 << index)))


def _require_instance(instance: object) -> Hypergraph3:
    if not isinstance(instance, Hypergraph3):
        raise ValidationError("instance must be a Hypergraph3")
    return instance


def vertex_occurrences(instance: Hypergraph3) -> tuple[int, ...]:
    instance = _require_instance(instance)
    values = [0] * instance.n
    for edge in instance.edges:
        for vertex in edge:
            values[vertex] += 1
    return tuple(values)


def is_linear(instance: Hypergraph3) -> bool:
    instance = _require_instance(instance)
    seen: set[tuple[int, int]] = set()
    for edge in instance.edges:
        for pair in itertools.combinations(edge, 2):
            if pair in seen:
                return False
            seen.add(pair)
    return True


def _incidence_adjacency(instance: Hypergraph3) -> list[list[int]]:
    adjacency = [[] for _ in range(instance.n + len(instance.edges))]
    for edge_index, edge in enumerate(instance.edges):
        edge_node = instance.n + edge_index
        for vertex in edge:
            adjacency[vertex].append(edge_node)
            adjacency[edge_node].append(vertex)
    return adjacency


def is_incidence_forest(instance: Hypergraph3) -> bool:
    instance = _require_instance(instance)
    adjacency = _incidence_adjacency(instance)
    visited = [False] * len(adjacency)
    for start in range(len(adjacency)):
        if visited[start]:
            continue
        visited[start] = True
        stack = [(start, -1)]
        while stack:
            node, parent = stack.pop()
            for neighbour in adjacency[node]:
                if neighbour == parent:
                    continue
                if visited[neighbour]:
                    return False
                visited[neighbour] = True
                stack.append((neighbour, node))
    return True


def color_incidence_forest(instance: Hypergraph3) -> tuple[int, ...]:
    instance = _require_instance(instance)
    if not is_incidence_forest(instance):
        raise ValidationError("instance incidence graph is not a forest")
    colors = [-1] * instance.n
    edge_adjacency: list[list[int]] = [[] for _ in instance.edges]
    vertex_edges: list[list[int]] = [[] for _ in range(instance.n)]
    for edge_index, edge in enumerate(instance.edges):
        for vertex in edge:
            vertex_edges[vertex].append(edge_index)
    for edges in vertex_edges:
        for first, second in itertools.combinations(edges, 2):
            edge_adjacency[first].append(second)
            edge_adjacency[second].append(first)
    seen_edges = [False] * len(instance.edges)
    for root in range(len(instance.edges)):
        if seen_edges[root]:
            continue
        root_edge = instance.edges[root]
        colors[root_edge[0]], colors[root_edge[1]], colors[root_edge[2]] = 0, 0, 1
        seen_edges[root] = True
        queue = deque([root])
        while queue:
            parent = queue.popleft()
            for child in edge_adjacency[parent]:
                if seen_edges[child]:
                    continue
                shared = set(instance.edges[parent]) & set(instance.edges[child])
                if len(shared) != 1:
                    raise AssertionError("forest edge adjacency must share exactly one vertex")
                inherited = next(iter(shared))
                fresh = [vertex for vertex in instance.edges[child] if vertex != inherited]
                if any(colors[vertex] != -1 for vertex in fresh):
                    raise AssertionError("forest traversal encountered previously coloured fresh vertex")
                colors[fresh[0]], colors[fresh[1]] = 0, 1
                seen_edges[child] = True
                queue.append(child)
    for vertex in range(instance.n):
        if colors[vertex] == -1:
            colors[vertex] = 0
    result = tuple(colors)
    if not verify_coloring(instance, result):
        raise AssertionError("incidence-forest colouring failed verification")
    return result


def processed_boundary(instance: Hypergraph3, ordering: Sequence[int], level: int) -> tuple[int, ...]:
    instance = _require_instance(instance)
    order = validate_ordering(instance, ordering)
    if type(level) is not int or level < 0 or level > instance.n:
        raise ValidationError("level must be an integer between zero and n")
    remainder = set(order[level:])
    return tuple(
        vertex
        for vertex in order[:level]
        if any(vertex in edge and any(other in remainder for other in edge) for edge in instance.edges)
    )


def boundary_width(instance: Hypergraph3, ordering: Sequence[int]) -> int:
    instance = _require_instance(instance)
    order = validate_ordering(instance, ordering)
    return max((len(processed_boundary(instance, order, level)) for level in range(instance.n + 1)), default=0)


def minimum_boundary_width(instance: Hypergraph3, *, max_vertices: int = 8) -> int:
    instance = _require_instance(instance)
    max_vertices = _strict_nonnegative_int(max_vertices, "maximum exhaustive vertex count")
    if instance.n > max_vertices:
        raise ValidationError("instance exceeds exhaustive ordering guard")
    return min((boundary_width(instance, ordering) for ordering in itertools.permutations(range(instance.n))), default=0)
