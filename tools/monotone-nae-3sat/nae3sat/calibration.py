"""Deterministic VS-04 tractable-control calibration report."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter

from .controls import (
    Graph2,
    XorSystem,
    boundary_width,
    color_incidence_forest,
    is_incidence_forest,
    is_linear,
    labelled_graphs,
    labelled_xor_systems,
    solve_graph2,
    solve_xor,
    vertex_occurrences,
)
from .model import Hypergraph3, incidence_components, normalize_instance
from .oracle import count_satisfying_assignments, labelled_instances, solve_exact
from .profile import build_exact_profile, profile_bytes
from .serialization import instance_id

FORMAT = "nae3-vs04-calibration-v1"


def _graph_summary(name: str, graph: Graph2) -> dict[str, object]:
    result = solve_graph2(graph)
    return {
        "name": name,
        "n": graph.n,
        "edges": [list(edge) for edge in graph.edges],
        "bipartite": result.bipartite,
        "witness": None if result.witness is None else list(result.witness),
        "components": result.components,
        "solution_count": result.solution_count,
        "conflict_edge": None if result.conflict_edge is None else list(result.conflict_edge),
    }


def _xor_summary(name: str, system: XorSystem) -> dict[str, object]:
    result = solve_xor(system)
    return {
        "name": name,
        "n": system.n,
        "equations": [[mask, rhs] for mask, rhs in system.equations],
        "consistent": result.consistent,
        "rank": result.rank,
        "free_variables": result.free_variables,
        "witness": None if result.witness is None else list(result.witness),
        "solution_count": result.solution_count,
        "reduced_rows": [[mask, rhs] for mask, rhs in result.reduced_rows],
    }


def _nae_summary(name: str, instance: Hypergraph3) -> dict[str, object]:
    ordering = tuple(range(instance.n))
    exact = solve_exact(instance)
    profile = build_exact_profile(instance, ordering)
    occurrence = vertex_occurrences(instance)
    forest = is_incidence_forest(instance)
    return {
        "name": name,
        "id": instance_id(instance),
        "n": instance.n,
        "m": len(instance.edges),
        "edges": [list(edge) for edge in instance.edges],
        "satisfiable": exact.satisfiable,
        "solution_count": count_satisfying_assignments(instance),
        "components": len(incidence_components(instance)),
        "maximum_occurrence": max(occurrence, default=0),
        "linear": is_linear(instance),
        "incidence_forest": forest,
        "forest_witness": list(color_incidence_forest(instance)) if forest else None,
        "ordering": list(ordering),
        "boundary_width": boundary_width(instance, ordering),
        "raw_prefixes": sum(level.raw_assignment_count for level in profile.levels),
        "exact_classes": sum(level.class_count for level in profile.levels),
        "live_classes": sum(level.live_class_count for level in profile.levels),
        "max_classes": max(level.class_count for level in profile.levels),
        "profile_bytes": len(profile_bytes(profile)),
    }


def _graph_census() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    totals: Counter[str] = Counter()
    for n in range(6):
        row: Counter[str] = Counter()
        component_distribution: Counter[int] = Counter()
        for graph in labelled_graphs(n):
            result = solve_graph2(graph)
            row["total"] += 1
            if result.bipartite:
                row["bipartite"] += 1
                component_distribution[result.components] += 1
            else:
                row["non_bipartite"] += 1
        record = {
            "n": n,
            "total": row["total"],
            "bipartite": row["bipartite"],
            "non_bipartite": row["non_bipartite"],
            "bipartite_component_distribution": {
                str(key): value for key, value in sorted(component_distribution.items())
            },
        }
        rows.append(record)
        totals.update({key: record[key] for key in ("total", "bipartite", "non_bipartite")})
    return {"counts": rows, "totals": dict(totals)}


def _xor_census() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    totals: Counter[str] = Counter()
    for n in range(4):
        row: Counter[str] = Counter()
        rank_distribution: Counter[int] = Counter()
        for system in labelled_xor_systems(n):
            result = solve_xor(system)
            row["total"] += 1
            if result.consistent:
                row["consistent"] += 1
                rank_distribution[result.rank] += 1
            else:
                row["inconsistent"] += 1
        record = {
            "n": n,
            "total": row["total"],
            "consistent": row["consistent"],
            "inconsistent": row["inconsistent"],
            "consistent_rank_distribution": {
                str(key): value for key, value in sorted(rank_distribution.items())
            },
        }
        rows.append(record)
        totals.update({key: record[key] for key in ("total", "consistent", "inconsistent")})
    return {"counts": rows, "totals": dict(totals)}


def _nae_filtered_census() -> dict[str, object]:
    rows: list[dict[str, object]] = []
    totals: Counter[str] = Counter()
    for n in range(6):
        row: Counter[str] = Counter()
        for instance in labelled_instances(n):
            profile = build_exact_profile(instance, tuple(range(n)))
            occurrence_at_most_three = max(vertex_occurrences(instance), default=0) <= 3
            forest = is_incidence_forest(instance)
            if occurrence_at_most_three:
                row["occurrence_at_most_three"] += 1
                row["occurrence_at_most_three_unsatisfiable"] += not profile.satisfiable
                row["occurrence_exact_classes"] += sum(level.class_count for level in profile.levels)
                row["occurrence_boundary_states"] += sum(
                    level.processed_valid_boundary_states for level in profile.levels
                )
            if forest:
                row["incidence_forest"] += 1
                row["incidence_forest_unsatisfiable"] += not profile.satisfiable
                row["forest_exact_classes"] += sum(level.class_count for level in profile.levels)
                row["forest_boundary_states"] += sum(
                    level.processed_valid_boundary_states for level in profile.levels
                )
                color_incidence_forest(instance)
        record = {"n": n, **dict(row)}
        for key in (
            "occurrence_at_most_three",
            "occurrence_at_most_three_unsatisfiable",
            "occurrence_exact_classes",
            "occurrence_boundary_states",
            "incidence_forest",
            "incidence_forest_unsatisfiable",
            "forest_exact_classes",
            "forest_boundary_states",
        ):
            record.setdefault(key, 0)
        rows.append(record)
        totals.update({key: value for key, value in record.items() if key != "n"})
    return {"counts": rows, "totals": dict(totals)}


def calibration_payload() -> dict[str, object]:
    graph_controls = (
        _graph_summary("path-4", Graph2(4, ((0, 1), (1, 2), (2, 3)))),
        _graph_summary("cycle-4", Graph2(4, ((0, 1), (0, 3), (1, 2), (2, 3)))),
        _graph_summary("cycle-3", Graph2(3, ((0, 1), (0, 2), (1, 2)))),
        _graph_summary("odd-cycle-plus-edge", Graph2(5, ((0, 1), (0, 2), (1, 2), (3, 4)))),
    )
    xor_controls = (
        _xor_summary("independent", XorSystem(3, ((1, 1), (2, 0), (4, 1)))),
        _xor_summary("dependent-consistent", XorSystem(3, ((3, 1), (5, 0), (6, 1)))),
        _xor_summary("contradictory-left-side", XorSystem(2, ((3, 0), (3, 1)))),
        _xor_summary("free-variables", XorSystem(5, ((3, 1),))),
    )
    nae_controls = (
        _nae_summary("single-edge", normalize_instance(3, ((0, 1, 2),))),
        _nae_summary("loose-path-3", normalize_instance(7, ((0, 1, 2), (2, 3, 4), (4, 5, 6)))),
        _nae_summary("loose-cycle-3", normalize_instance(6, ((0, 1, 2), (0, 4, 5), (2, 3, 4)))),
        _nae_summary("two-disconnected-edges", normalize_instance(6, ((0, 1, 2), (3, 4, 5)))),
        _nae_summary("loose-path-4", normalize_instance(9, ((0, 1, 2), (2, 3, 4), (4, 5, 6), (6, 7, 8)))),
        _nae_summary("complete-five", normalize_instance(5, itertools.combinations(range(5), 3))),
    )
    return {
        "format": FORMAT,
        "computation": "finite-exhaustive-controls",
        "mechanisms": {
            "graph_bipartiteness": "one parity bit per vertex relative to a component root",
            "xor": "polynomial affine row space under Gaussian elimination",
            "incidence_forest": "leaf/subtree elimination with no returning compatibility path",
            "bounded_boundary": "explicit complete interface state exponential only in boundary width",
            "disconnected_components": "exact conjunction and solution-count product across independent components",
        },
        "graph": {"census": _graph_census(), "controls": list(graph_controls)},
        "xor": {"census": _xor_census(), "controls": list(xor_controls)},
        "nae": {"filtered_census": _nae_filtered_census(), "controls": list(nae_controls)},
        "external_boundaries": {
            "planar_nae3sat": {
                "status": "ESTABLISHED / CHECKED",
                "source": "Moret-1988-planar-nae3sat",
            },
            "occurrence_at_most_three": {
                "status": "ESTABLISHED / CHECKED",
                "source": "Porschen-Randerath-Speckenmeyer-2003",
            },
        },
        "limitations": [
            "finite control censuses do not prove unrestricted tractability",
            "exact profile counts do not imply efficient profile construction",
            "planar and bounded-occurrence algorithms are imported rather than reimplemented",
            "minimum boundary width is not exhaustively optimized in this report",
        ],
    }


def calibration_record() -> dict[str, object]:
    payload = calibration_payload()
    payload_bytes = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return {**payload, "payload_sha256": hashlib.sha256(payload_bytes).hexdigest()}


def calibration_bytes() -> bytes:
    return json.dumps(calibration_record(), separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def verify_calibration_record(record: object) -> bool:
    if type(record) is not dict or "payload_sha256" not in record:
        return False
    payload = {key: value for key, value in record.items() if key != "payload_sha256"}
    payload_bytes = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return record["payload_sha256"] == hashlib.sha256(payload_bytes).hexdigest()
