"""Exact minimal-obstruction certificates for VS-05."""

from __future__ import annotations

import itertools
from collections.abc import Sequence as SequenceABC
from dataclasses import dataclass
from typing import Sequence

from .controls import boundary_width, is_incidence_forest, is_linear, vertex_occurrences
from .errors import ValidationError
from .model import Coloring, Edge, Hypergraph3, RelabeledHypergraph3, incidence_components, induced_subinstance, normalize_instance, verify_coloring
from .oracle import is_edge_minimal_unsatisfiable, solve_exact
from .profile import build_exact_profile, profile_bytes
from .serialization import encoded_size_bytes, instance_id


def _require_instance(instance: object) -> Hypergraph3:
    if not isinstance(instance, Hypergraph3):
        raise ValidationError("instance must be a Hypergraph3")
    return instance


def _strict_vertex(value: object, n: int, name: str = "vertex") -> int:
    if type(value) is not int or value < 0 or value >= n:
        raise ValidationError(f"{name} must be an in-range integer excluding Booleans")
    return value


def _strict_coloring(value: object, n: int) -> Coloring:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, SequenceABC):
        raise ValidationError("witness must be a non-string finite sequence")
    witness = tuple(value)
    if len(witness) != n or any(type(bit) is not int or bit not in (0, 1) for bit in witness):
        raise ValidationError("witness must contain exactly one binary integer per vertex")
    return witness


def _canonical_edge(instance: Hypergraph3, edge: Sequence[int]) -> Edge:
    if isinstance(edge, (str, bytes, bytearray)) or not isinstance(edge, SequenceABC):
        raise ValidationError("edge must be a non-string three-vertex sequence")
    values = tuple(edge)
    if len(values) != 3 or any(type(vertex) is not int for vertex in values):
        raise ValidationError("edge must contain exactly three integer vertices")
    if len(set(values)) != 3 or any(vertex < 0 or vertex >= instance.n for vertex in values):
        raise ValidationError("edge vertices must be distinct and in range")
    return tuple(sorted(values))


@dataclass(frozen=True, slots=True)
class EdgeDeletionCertificate:
    edge: Edge
    witness: Coloring

    def __post_init__(self) -> None:
        if type(self.edge) is not tuple or len(self.edge) != 3:
            raise ValidationError("certificate edge must be a canonical triple")
        if any(type(vertex) is not int for vertex in self.edge) or not self.edge[0] < self.edge[1] < self.edge[2]:
            raise ValidationError("certificate edge must be strictly increasing integers")
        _strict_coloring(self.witness, len(self.witness))


@dataclass(frozen=True, slots=True)
class VertexDeletionCertificate:
    vertex: int
    new_to_old: tuple[int, ...]
    witness: Coloring

    def __post_init__(self) -> None:
        if type(self.vertex) is not int or self.vertex < 0:
            raise ValidationError("deleted vertex must be a nonnegative integer")
        if type(self.new_to_old) is not tuple:
            raise ValidationError("new_to_old must be a tuple")
        if any(type(vertex) is not int or vertex < 0 for vertex in self.new_to_old):
            raise ValidationError("new_to_old entries must be nonnegative integers")
        if any(left >= right for left, right in zip(self.new_to_old, self.new_to_old[1:])):
            raise ValidationError("new_to_old must be strictly increasing")
        if self.vertex in self.new_to_old:
            raise ValidationError("deleted vertex cannot remain in new_to_old")
        _strict_coloring(self.witness, len(self.new_to_old))


def complete_three_graph(n: int) -> Hypergraph3:
    if type(n) is not int or n < 0:
        raise ValidationError("vertex count must be a nonnegative integer excluding Booleans")
    return Hypergraph3(n, tuple(itertools.combinations(range(n), 3)))


def fano_plane() -> Hypergraph3:
    return Hypergraph3(
        7,
        (
            (0, 1, 2),
            (0, 3, 4),
            (0, 5, 6),
            (1, 3, 5),
            (1, 4, 6),
            (2, 3, 6),
            (2, 4, 5),
        ),
    )


def delete_edge(instance: Hypergraph3, edge: Sequence[int]) -> Hypergraph3:
    instance = _require_instance(instance)
    canonical = _canonical_edge(instance, edge)
    if canonical not in instance.edges:
        raise ValidationError("edge is not present in the instance")
    return Hypergraph3(instance.n, tuple(value for value in instance.edges if value != canonical))


def delete_vertex(instance: Hypergraph3, vertex: int) -> RelabeledHypergraph3:
    instance = _require_instance(instance)
    vertex = _strict_vertex(vertex, instance.n)
    return induced_subinstance(instance, (value for value in range(instance.n) if value != vertex))


def is_vertex_minimal_unsatisfiable(instance: Hypergraph3) -> bool:
    instance = _require_instance(instance)
    if solve_exact(instance).satisfiable:
        return False
    return all(solve_exact(delete_vertex(instance, vertex).graph).satisfiable for vertex in range(instance.n))


def edge_deletion_certificates(instance: Hypergraph3) -> tuple[EdgeDeletionCertificate, ...]:
    instance = _require_instance(instance)
    if solve_exact(instance).satisfiable:
        raise ValidationError("edge-deletion certificates require an unsatisfiable instance")
    certificates: list[EdgeDeletionCertificate] = []
    for edge in instance.edges:
        reduced = delete_edge(instance, edge)
        result = solve_exact(reduced)
        if not result.satisfiable or result.witness is None:
            raise ValidationError("instance is not edge-minimal unsatisfiable")
        if not verify_coloring(reduced, result.witness):
            raise AssertionError("edge-deletion witness failed verification")
        certificates.append(EdgeDeletionCertificate(edge, result.witness))
    return tuple(certificates)


def vertex_deletion_certificates(instance: Hypergraph3) -> tuple[VertexDeletionCertificate, ...]:
    instance = _require_instance(instance)
    if solve_exact(instance).satisfiable:
        raise ValidationError("vertex-deletion certificates require an unsatisfiable instance")
    certificates: list[VertexDeletionCertificate] = []
    for vertex in range(instance.n):
        reduced = delete_vertex(instance, vertex)
        result = solve_exact(reduced.graph)
        if not result.satisfiable or result.witness is None:
            raise ValidationError("instance is not vertex-minimal unsatisfiable")
        if not verify_coloring(reduced.graph, result.witness):
            raise AssertionError("vertex-deletion witness failed verification")
        certificates.append(VertexDeletionCertificate(vertex, reduced.new_to_old, result.witness))
    return tuple(certificates)


def _pair_codegree_distribution(instance: Hypergraph3) -> dict[str, int]:
    counts: dict[tuple[int, int], int] = {
        pair: 0 for pair in itertools.combinations(range(instance.n), 2)
    }
    for edge in instance.edges:
        for pair in itertools.combinations(edge, 2):
            counts[pair] += 1
    distribution: dict[str, int] = {}
    for value in counts.values():
        key = str(value)
        distribution[key] = distribution.get(key, 0) + 1
    return dict(sorted(distribution.items(), key=lambda item: int(item[0])))


def _distribution(values: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    for value in values:
        key = str(value)
        result[key] = result.get(key, 0) + 1
    return dict(sorted(result.items(), key=lambda item: int(item[0])))


def _profile_signature(profile) -> list[object]:
    return [
        list(profile.ordering),
        [
            [
                list(level.class_masks),
                list(level.assignment_class_ids),
                None if level.transitions is None else [list(pair) for pair in level.transitions],
                level.processed_valid_boundary_states,
            ]
            for level in profile.levels
        ],
    ]


def all_ordering_profile_aggregate(instance: Hypergraph3) -> dict[str, object]:
    import hashlib
    import json

    instance = _require_instance(instance)
    max_classes: list[int] = []
    total_classes: list[int] = []
    widths: list[int] = []
    byte_lengths: list[int] = []
    digest = hashlib.sha256()
    ordering_count = 0

    for ordering in itertools.permutations(range(instance.n)):
        profile = build_exact_profile(instance, ordering)
        class_counts = [level.class_count for level in profile.levels]
        max_classes.append(max(class_counts))
        total_classes.append(sum(class_counts))
        widths.append(boundary_width(instance, ordering))
        byte_lengths.append(len(profile_bytes(profile)))
        digest.update(json.dumps(_profile_signature(profile), separators=(",", ":"), ensure_ascii=True).encode("utf-8"))
        digest.update(b"\n")
        ordering_count += 1

    def range_record(values: list[int]) -> dict[str, object]:
        return {
            "minimum": min(values),
            "maximum": max(values),
            "distribution": _distribution(values),
        }

    return {
        "ordering_count": ordering_count,
        "max_classes": range_record(max_classes),
        "total_classes": range_record(total_classes),
        "boundary_width": range_record(widths),
        "profile_bytes": range_record(byte_lengths),
        "profile_sequence_sha256": digest.hexdigest(),
    }


def obstruction_record(name: str, instance: Hypergraph3) -> dict[str, object]:
    instance = _require_instance(instance)
    if type(name) is not str or not name:
        raise ValidationError("obstruction name must be a nonempty string")
    exact = solve_exact(instance)
    if exact.satisfiable:
        raise ValidationError("obstruction record requires an unsatisfiable instance")

    edge_certificates = edge_deletion_certificates(instance)
    vertex_certificates = vertex_deletion_certificates(instance)
    occurrences = vertex_occurrences(instance)
    return {
        "name": name,
        "id": instance_id(instance),
        "n": instance.n,
        "m": len(instance.edges),
        "edges": [list(edge) for edge in instance.edges],
        "encoded_bytes": encoded_size_bytes(instance),
        "degree_sequence": sorted(occurrences),
        "regular": len(set(occurrences)) <= 1,
        "maximum_occurrence": max(occurrences, default=0),
        "pair_codegree_distribution": _pair_codegree_distribution(instance),
        "components": len(incidence_components(instance)),
        "linear": is_linear(instance),
        "incidence_forest": is_incidence_forest(instance),
        "natural_boundary_width": boundary_width(instance, tuple(range(instance.n))),
        "satisfiable": False,
        "edge_minimal_unsatisfiable": is_edge_minimal_unsatisfiable(instance),
        "vertex_minimal_unsatisfiable": is_vertex_minimal_unsatisfiable(instance),
        "edge_deletion_certificates": [
            {"edge": list(certificate.edge), "witness": list(certificate.witness)}
            for certificate in edge_certificates
        ],
        "vertex_deletion_certificates": [
            {
                "vertex": certificate.vertex,
                "new_to_old": list(certificate.new_to_old),
                "witness": list(certificate.witness),
            }
            for certificate in vertex_certificates
        ],
        "all_ordering_profiles": all_ordering_profile_aggregate(instance),
    }
