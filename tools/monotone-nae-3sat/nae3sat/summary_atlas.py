"""Deterministic VS-06 atlas of naive-summary collisions."""

from __future__ import annotations

import hashlib
import json

from .summaries import (
    bounded_radius_collision,
    bounded_radius_summary,
    boundary_parity_summary,
    boundary_weight_summary,
    complete_five_plus_isolate,
    degree_collision_satisfiable,
    degree_collision_unsatisfiable,
    degree_sequence_summary,
    edge_intersection_summary,
    exact_completion_mask,
    fano_local_obstruction,
    graph_is_bipartite,
    incidence_gram_spectrum_summary,
    local_consistency_star,
    pair_codegree_collision_satisfiable,
    pair_codegree_multiset_summary,
    parity_summary,
    proper_induced_satisfiability_summary,
    root_gac_summary,
    second_moment_summary,
    solution_summary,
    star_six,
)
from .model import Hypergraph3, normalize_instance
from .serialization import instance_id

FORMAT = "nae3-vs06-summary-collision-atlas-v1"


def _instance_record(instance: Hypergraph3) -> dict[str, object]:
    return {
        "id": instance_id(instance),
        "n": instance.n,
        "edges": [list(edge) for edge in instance.edges],
        "semantics": solution_summary(instance),
    }


def _whole_instance_collision(
    name: str,
    left: Hypergraph3,
    right: Hypergraph3,
    summary,
) -> dict[str, object]:
    left_summary = summary(left)
    right_summary = summary(right)
    if left_summary != right_summary:
        raise AssertionError(f"{name} witness pair does not collide")
    left_semantics = solution_summary(left)
    right_semantics = solution_summary(right)
    if left_semantics["satisfiable"] == right_semantics["satisfiable"]:
        raise AssertionError(f"{name} witness pair has equal satisfiability")
    return {
        "name": name,
        "status": "DISPROVED",
        "claim": "the summary determines whole-instance satisfiability",
        "summary": left_summary,
        "left": _instance_record(left),
        "right": _instance_record(right),
    }


def _prefix_collision(
    name: str,
    instance: Hypergraph3,
    ordering: tuple[int, ...],
    left_prefix: tuple[int, ...],
    right_prefix: tuple[int, ...],
    summary,
) -> dict[str, object]:
    left_summary = summary(instance, ordering, left_prefix)
    right_summary = summary(instance, ordering, right_prefix)
    if left_summary != right_summary:
        raise AssertionError(f"{name} prefix pair does not collide")
    left_mask = exact_completion_mask(instance, ordering, left_prefix)
    right_mask = exact_completion_mask(instance, ordering, right_prefix)
    if left_mask == right_mask:
        raise AssertionError(f"{name} prefix pair has equal exact semantics")
    return {
        "name": name,
        "status": "DISPROVED",
        "claim": "the summary determines the exact completion set",
        "instance": _instance_record(instance),
        "ordering": list(ordering),
        "summary": list(left_summary),
        "left_prefix": list(left_prefix),
        "right_prefix": list(right_prefix),
        "left_completion_mask": left_mask,
        "right_completion_mask": right_mask,
    }


def _bounded_radius_samples() -> list[dict[str, object]]:
    samples: list[dict[str, object]] = []
    for radius in (1, 2):
        unsatisfiable, satisfiable = bounded_radius_collision(radius)
        left_summary = bounded_radius_summary(unsatisfiable, radius)
        right_summary = bounded_radius_summary(satisfiable, radius)
        if left_summary != right_summary:
            raise AssertionError("bounded-radius family failed to collide")
        if graph_is_bipartite(unsatisfiable):
            raise AssertionError("odd-cycle control unexpectedly bipartite")
        if not graph_is_bipartite(satisfiable):
            raise AssertionError("even-cycle control unexpectedly non-bipartite")
        samples.append(
            {
                "radius": radius,
                "unsatisfiable_cycle_lengths": [
                    2 * radius + 3,
                    2 * radius + 3,
                ],
                "satisfiable_cycle_lengths": [
                    2 * radius + 2,
                    2 * radius + 4,
                ],
                "vertices": unsatisfiable[0],
                "edges": len(unsatisfiable[1]),
                "rooted_neighbourhood_multiset_size": len(left_summary),
            }
        )
    return samples


def summary_collision_payload() -> dict[str, object]:
    star = star_six()
    complete = complete_five_plus_isolate()
    degree_sat = degree_collision_satisfiable()
    degree_unsat = degree_collision_unsatisfiable()
    pair_sat = pair_codegree_collision_satisfiable()
    fano = fano_local_obstruction()
    local_star = local_consistency_star()

    boundary_instance = normalize_instance(
        4,
        ((0, 1, 2), (0, 1, 3)),
    )
    parity_instance = normalize_instance(3, ((0, 1, 2),))

    collisions = [
        _whole_instance_collision(
            "degree-sequence",
            degree_sat,
            degree_unsat,
            degree_sequence_summary,
        ),
        _whole_instance_collision(
            "edge-intersection-multiset",
            star,
            complete,
            edge_intersection_summary,
        ),
        _whole_instance_collision(
            "pair-codegree-multiset",
            pair_sat,
            degree_unsat,
            pair_codegree_multiset_summary,
        ),
        _whole_instance_collision(
            "parity-data",
            star,
            complete,
            parity_summary,
        ),
        _whole_instance_collision(
            "second-moment-data",
            star,
            complete,
            second_moment_summary,
        ),
        _whole_instance_collision(
            "incidence-gram-spectrum",
            star,
            complete,
            incidence_gram_spectrum_summary,
        ),
        _whole_instance_collision(
            "root-generalized-arc-consistency",
            local_star,
            fano,
            root_gac_summary,
        ),
        _whole_instance_collision(
            "proper-induced-satisfiability-through-n-minus-one",
            local_star,
            fano,
            lambda instance: proper_induced_satisfiability_summary(
                instance,
                maximum_size=instance.n - 1,
            ),
        ),
        _prefix_collision(
            "boundary-weight",
            boundary_instance,
            (3, 2, 1, 0),
            (0, 0, 1),
            (0, 1, 0),
            boundary_weight_summary,
        ),
        _prefix_collision(
            "boundary-parity",
            parity_instance,
            (0, 1, 2),
            (0, 0),
            (1, 1),
            boundary_parity_summary,
        ),
    ]

    return {
        "format": FORMAT,
        "computation": "explicit-counterexamples-plus-constructive-family",
        "semantic_targets": {
            "whole_instance": "satisfiability",
            "prefix_state": "exact completion set",
            "bounded_radius_family": (
                "conditioned residual satisfiability under anchors 0 and 1"
            ),
        },
        "collisions": collisions,
        "bounded_radius_family": {
            "status": "PROVED",
            "claim": (
                "for every fixed radius r>=1, the two unions "
                "C_(2r+3)+C_(2r+3) and C_(2r+2)+C_(2r+4) have "
                "the same multiset of rooted radius-r graph neighbourhoods "
                "but opposite bipartiteness; the anchored NAE encoding "
                "therefore has opposite conditioned residual satisfiability"
            ),
            "samples": _bounded_radius_samples(),
        },
        "retained_control": {
            "name": "exact-boundary-assignment",
            "status": "PROVED / CHECKED",
            "claim": (
                "for a fixed instance, ordering, and processed-consistency "
                "flag, the exact assignment on the processed boundary "
                "determines the remaining completion set"
            ),
            "limitation": (
                "the boundary may have linear size, so this is the known "
                "2^w interface dynamic programme rather than a universal "
                "polynomial compression"
            ),
        },
        "limitations": [
            "each disproof applies only to the explicitly defined summary",
            "the bounded-radius theorem concerns every fixed radius, not radii growing with input size",
            "failure of these summaries is not a lower bound for arbitrary representations or algorithms",
            "the exact-boundary control may require exponentially many states in the boundary width",
        ],
    }


def summary_collision_record() -> dict[str, object]:
    payload = summary_collision_payload()
    payload_bytes = json.dumps(
        payload,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return {
        **payload,
        "payload_sha256": hashlib.sha256(payload_bytes).hexdigest(),
    }


def summary_collision_bytes() -> bytes:
    return json.dumps(
        summary_collision_record(),
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
