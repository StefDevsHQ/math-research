"""Exact exponential oracle for finite Monotone NAE-3SAT experiments."""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Iterator

from .errors import ValidationError
from .model import Hypergraph3, incidence_components, verify_coloring


@dataclass(frozen=True, slots=True)
class SolveResult:
    satisfiable: bool
    witness: tuple[int, ...] | None
    assignments_tested: int
    symmetry_reduction: str

    def __post_init__(self) -> None:
        if type(self.satisfiable) is not bool:
            raise ValidationError("satisfiable must be a Boolean")
        if self.witness is not None and type(self.witness) is not tuple:
            raise ValidationError("witness must be a tuple or None")
        if type(self.assignments_tested) is not int or self.assignments_tested < 1:
            raise ValidationError("assignments_tested must be a positive integer")
        if self.symmetry_reduction not in ("none-v1", "component-complement-v1"):
            raise ValidationError("unknown symmetry reduction identifier")


def _require_instance(instance: object) -> Hypergraph3:
    if not isinstance(instance, Hypergraph3):
        raise ValidationError("instance must be a Hypergraph3")
    return instance


def _satisfies_edges(
    edges: tuple[tuple[int, int, int], ...],
    coloring: tuple[int, ...],
) -> bool:
    for u, v, w in edges:
        if coloring[u] == coloring[v] == coloring[w]:
            return False
    return True


def _baseline_candidates(n: int):
    return itertools.product((0, 1), repeat=n)


def _symmetry_free_vertices(instance: Hypergraph3) -> tuple[int, ...]:
    fixed = bytearray(instance.n)
    active = bytearray(instance.n)
    for u, v, w in instance.edges:
        active[u] = active[v] = active[w] = 1
    for component in incidence_components(instance):
        if any(active[vertex] for vertex in component):
            fixed[component[0]] = 1
    for vertex in range(instance.n):
        if not active[vertex]:
            fixed[vertex] = 1
    return tuple(vertex for vertex in range(instance.n) if not fixed[vertex])


def solve_exact(
    instance: Hypergraph3,
    *,
    use_symmetry: bool = True,
) -> SolveResult:
    """Decide satisfiability exactly and return the true least witness."""
    instance = _require_instance(instance)
    if type(use_symmetry) is not bool:
        raise ValidationError("use_symmetry must be a Boolean")

    if not use_symmetry:
        tested = 0
        for candidate in _baseline_candidates(instance.n):
            tested += 1
            if _satisfies_edges(instance.edges, candidate):
                if not verify_coloring(instance, candidate):
                    raise AssertionError("internal and public verifiers disagree")
                return SolveResult(True, candidate, tested, "none-v1")
        return SolveResult(False, None, tested, "none-v1")

    free_vertices = _symmetry_free_vertices(instance)
    tested = 0
    for free_bits in itertools.product((0, 1), repeat=len(free_vertices)):
        coloring = [0] * instance.n
        for vertex, bit in zip(free_vertices, free_bits):
            coloring[vertex] = bit
        candidate = tuple(coloring)
        tested += 1
        if _satisfies_edges(instance.edges, candidate):
            if not verify_coloring(instance, candidate):
                raise AssertionError("internal and public verifiers disagree")
            return SolveResult(
                True,
                candidate,
                tested,
                "component-complement-v1",
            )
    return SolveResult(False, None, tested, "component-complement-v1")


def satisfying_assignments(
    instance: Hypergraph3,
) -> tuple[tuple[int, ...], ...]:
    """Return all satisfying colourings in lexicographic order."""
    instance = _require_instance(instance)
    return tuple(
        candidate
        for candidate in _baseline_candidates(instance.n)
        if _satisfies_edges(instance.edges, candidate)
    )


def count_satisfying_assignments(instance: Hypergraph3) -> int:
    """Return the exact number of satisfying total colourings."""
    instance = _require_instance(instance)
    return sum(
        1
        for candidate in _baseline_candidates(instance.n)
        if _satisfies_edges(instance.edges, candidate)
    )


def count_satisfying_assignments_factorized(instance: Hypergraph3) -> int:
    """Count via incidence-component factorization."""
    instance = _require_instance(instance)
    total = 1
    for component in incidence_components(instance):
        component_set = set(component)
        component_edges = tuple(
            edge for edge in instance.edges if edge[0] in component_set
        )
        if not component_edges:
            total *= 2
            continue
        old_to_new = {old: new for new, old in enumerate(component)}
        subinstance = Hypergraph3(
            len(component),
            tuple(
                tuple(old_to_new[vertex] for vertex in edge)
                for edge in component_edges
            ),
        )
        total *= count_satisfying_assignments(subinstance)
    return total


def is_edge_minimal_unsatisfiable(instance: Hypergraph3) -> bool:
    """Check unsatisfiability and every one-edge deletion."""
    instance = _require_instance(instance)
    if solve_exact(instance).satisfiable:
        return False
    for index in range(len(instance.edges)):
        reduced = Hypergraph3(
            instance.n,
            instance.edges[:index] + instance.edges[index + 1 :],
        )
        if not solve_exact(reduced).satisfiable:
            return False
    return True


def labelled_instances(n: int) -> Iterator[Hypergraph3]:
    """Yield each labelled simple 3-uniform hypergraph once."""
    if type(n) is not int or n < 0:
        raise ValidationError(
            "n must be a nonnegative integer excluding Booleans"
        )
    triples = tuple(itertools.combinations(range(n), 3))
    for mask in range(1 << len(triples)):
        yield Hypergraph3(
            n,
            tuple(
                edge
                for index, edge in enumerate(triples)
                if mask & (1 << index)
            ),
        )
