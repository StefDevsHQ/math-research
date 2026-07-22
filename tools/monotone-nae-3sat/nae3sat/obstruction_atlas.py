"""Deterministic VS-05 minimal-obstruction atlas."""

from __future__ import annotations

import hashlib
import json

from .obstructions import complete_three_graph, fano_plane, is_vertex_minimal_unsatisfiable, obstruction_record
from .oracle import is_edge_minimal_unsatisfiable, labelled_instances, solve_exact
from .serialization import instance_id

FORMAT = "nae3-vs05-obstruction-atlas-v1"


def _small_domain_census() -> dict[str, object]:
    counts: list[dict[str, object]] = []
    totals = {
        "instances": 0,
        "unsatisfiable": 0,
        "edge_minimal_unsatisfiable": 0,
        "vertex_minimal_unsatisfiable": 0,
        "both_minimal": 0,
    }
    obstruction_ids: list[str] = []

    for n in range(6):
        row = {
            "n": n,
            "instances": 0,
            "unsatisfiable": 0,
            "edge_minimal_unsatisfiable": 0,
            "vertex_minimal_unsatisfiable": 0,
            "both_minimal": 0,
            "obstruction_ids": [],
        }
        for instance in labelled_instances(n):
            row["instances"] += 1
            exact = solve_exact(instance)
            if exact.satisfiable:
                continue
            row["unsatisfiable"] += 1
            identifier = instance_id(instance)
            row["obstruction_ids"].append(identifier)
            obstruction_ids.append(identifier)
            edge_minimal = is_edge_minimal_unsatisfiable(instance)
            vertex_minimal = is_vertex_minimal_unsatisfiable(instance)
            row["edge_minimal_unsatisfiable"] += edge_minimal
            row["vertex_minimal_unsatisfiable"] += vertex_minimal
            row["both_minimal"] += edge_minimal and vertex_minimal
        counts.append(row)
        for key in totals:
            totals[key] += int(row[key])

    return {
        "domain": "all-labelled-3-uniform-hypergraphs-n-le-5",
        "generator": "edge-mask-v1",
        "counts": counts,
        "totals": totals,
        "obstruction_ids": obstruction_ids,
    }


def obstruction_atlas_payload() -> dict[str, object]:
    return {
        "format": FORMAT,
        "computation": "finite-exhaustive-census-plus-named-controls",
        "definitions": {
            "edge_minimal_unsatisfiable": "unsatisfiable and every single-edge deletion is satisfiable",
            "vertex_minimal_unsatisfiable": "unsatisfiable and every single-vertex induced deletion is satisfiable",
            "single_deletion_sufficiency": "monotonicity under deletion makes single deletions sufficient for every proper edge or induced-vertex subinstance",
        },
        "small_domain_census": _small_domain_census(),
        "named_obstructions": [
            obstruction_record("complete-three-graph-five", complete_three_graph(5)),
            obstruction_record("fano-plane", fano_plane()),
        ],
        "external_sources": {
            "property_b": "Erdos-Hajnal-property-b",
            "fano_edge_minimal_non-two-colourable": "Person-Schacht-2009-fano",
        },
        "limitations": [
            "the exhaustive census stops at five vertices",
            "the Fano plane is a named seven-vertex control rather than an exhaustive seven-vertex census",
            "all-ordering profile evidence is finite and does not imply asymptotic bounds",
            "atlas construction uses the exponential exact oracle and factorially many orderings",
            "two named obstructions do not classify all critical 3-uniform hypergraphs",
        ],
    }


def obstruction_atlas_record() -> dict[str, object]:
    payload = obstruction_atlas_payload()
    payload_bytes = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return {**payload, "payload_sha256": hashlib.sha256(payload_bytes).hexdigest()}


def obstruction_atlas_bytes() -> bytes:
    return json.dumps(obstruction_atlas_record(), separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def verify_obstruction_atlas_record(record: object) -> bool:
    if type(record) is not dict or "payload_sha256" not in record:
        return False
    payload = {key: value for key, value in record.items() if key != "payload_sha256"}
    payload_bytes = json.dumps(payload, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return record["payload_sha256"] == hashlib.sha256(payload_bytes).hexdigest()
