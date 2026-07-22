"""Deterministic finite census for VS-02."""

from __future__ import annotations

import hashlib
import json
from collections import Counter

from .errors import ValidationError
from .model import incidence_components
from .oracle import (
    count_satisfying_assignments,
    is_edge_minimal_unsatisfiable,
    labelled_instances,
)

CORPUS_FORMAT = "nae3-vs02-corpus-v1"
DOMAIN = "all-labelled-3-uniform-hypergraphs-n-le-5"
GENERATOR = "edge-mask-v1"


def _compact_json(value: object) -> bytes:
    return json.dumps(
        value,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def corpus_payload(max_vertices: int = 5) -> dict[str, object]:
    if type(max_vertices) is not int or max_vertices < 0:
        raise ValidationError(
            "max_vertices must be a nonnegative integer excluding Booleans"
        )

    counts: list[dict[str, object]] = []
    totals = {
        "instances": 0,
        "satisfiable": 0,
        "unsatisfiable": 0,
        "connected": 0,
        "edge_minimal_unsatisfiable": 0,
        "reference_colourings": 0,
    }

    for n in range(max_vertices + 1):
        row: dict[str, object] = {
            "n": n,
            "instances": 0,
            "satisfiable": 0,
            "unsatisfiable": 0,
            "connected": 0,
            "edge_minimal_unsatisfiable": 0,
            "satisfying_count_distribution": {},
        }
        distribution: Counter[int] = Counter()

        for graph in labelled_instances(n):
            row["instances"] += 1
            totals["instances"] += 1
            totals["reference_colourings"] += 1 << n

            satisfying_count = count_satisfying_assignments(graph)
            distribution[satisfying_count] += 1
            if satisfying_count:
                row["satisfiable"] += 1
                totals["satisfiable"] += 1
            else:
                row["unsatisfiable"] += 1
                totals["unsatisfiable"] += 1
                if is_edge_minimal_unsatisfiable(graph):
                    row["edge_minimal_unsatisfiable"] += 1
                    totals["edge_minimal_unsatisfiable"] += 1

            connected = n > 0 and len(incidence_components(graph)) == 1
            if connected:
                row["connected"] += 1
                totals["connected"] += 1

        row["satisfying_count_distribution"] = {
            str(count): distribution[count]
            for count in sorted(distribution)
        }
        counts.append(row)

    domain = (
        DOMAIN
        if max_vertices == 5
        else f"all-labelled-3-uniform-hypergraphs-n-le-{max_vertices}"
    )
    return {
        "format": CORPUS_FORMAT,
        "domain": domain,
        "generator": GENERATOR,
        "computation": "finite-exhaustive",
        "counts": counts,
        "totals": totals,
    }


def corpus_record(max_vertices: int = 5) -> dict[str, object]:
    payload = corpus_payload(max_vertices)
    digest = hashlib.sha256(_compact_json(payload)).hexdigest()
    return {**payload, "payload_sha256": digest}


def corpus_bytes(max_vertices: int = 5) -> bytes:
    return _compact_json(corpus_record(max_vertices))


def verify_corpus_record(record: object) -> bool:
    if type(record) is not dict or "payload_sha256" not in record:
        return False
    payload = {
        key: value
        for key, value in record.items()
        if key != "payload_sha256"
    }
    return (
        hashlib.sha256(_compact_json(payload)).hexdigest()
        == record["payload_sha256"]
    )
