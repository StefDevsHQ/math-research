"""Deterministic VS-08 record for oriented PCRNF attacks."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter

from .model import Hypergraph3, normalize_instance
from .oracle import labelled_instances
from .pcrnf import (
    build_pcrnf,
    compare_pcrnf_profile,
    pcrnf_bytes,
    pcrnf_completion_mask,
    pcrnf_record,
    traverse_pcrnf,
    unoriented_pcrnf_key,
)
from .semantic_merging import fan_bad_ordering, fan_good_ordering, fan_instance
from .serialization import instance_id

FORMAT = "nae3-vs08-pcrnf-attack-v1"
COMPUTATION = "finite-exhaustive-through-four-plus-explicit-five-vertex-and-fan-controls"


def _instance_record(instance: Hypergraph3) -> dict[str, object]:
    return {
        "id": instance_id(instance),
        "n": instance.n,
        "edges": [list(edge) for edge in instance.edges],
    }


def orientation_counterexample() -> dict[str, object]:
    instance = normalize_instance(3, ((0, 1, 2),))
    ordering = (0, 1, 2)
    left = build_pcrnf(instance, ordering, (0, 0))
    right = build_pcrnf(instance, ordering, (1, 1))
    left_mask = pcrnf_completion_mask(left, ordering[2:])
    right_mask = pcrnf_completion_mask(right, ordering[2:])
    if unoriented_pcrnf_key(left) != unoriented_pcrnf_key(right):
        raise AssertionError("orientation counterexample no longer collides")
    if left_mask == right_mask:
        raise AssertionError("orientation counterexample lost semantic separation")
    return {
        "status": "DISPROVED",
        "claim": (
            "component-complement normalization may discard the orientation "
            "needed for exact labelled completion semantics"
        ),
        "instance": _instance_record(instance),
        "ordering": list(ordering),
        "left_prefix": [0, 0],
        "right_prefix": [1, 1],
        "unoriented_key_equal": True,
        "left_completion_mask": left_mask,
        "right_completion_mask": right_mask,
        "repair": "store one explicit orientation bit per residual component",
    }


def incompleteness_witness() -> dict[str, object]:
    instance = normalize_instance(
        5,
        (
            (0, 1, 2),
            (0, 1, 3),
            (0, 2, 3),
            (0, 3, 4),
            (1, 2, 3),
            (1, 2, 4),
        ),
    )
    ordering = (0, 4, 1, 2, 3)
    left_prefix = (0, 0)
    right_prefix = (0, 1)
    left = build_pcrnf(instance, ordering, left_prefix)
    right = build_pcrnf(instance, ordering, right_prefix)
    left_mask = pcrnf_completion_mask(left, ordering[2:])
    right_mask = pcrnf_completion_mask(right, ordering[2:])
    if left == right:
        raise AssertionError("PCRNF incompleteness witness became syntactically equal")
    if left_mask != right_mask:
        raise AssertionError("PCRNF incompleteness witness lost semantic equality")
    return {
        "status": "COMPUTATIONAL / CHECKED",
        "claim": (
            "byte equality of oriented PCRNF is strictly finer than exact "
            "completion equivalence"
        ),
        "instance": _instance_record(instance),
        "ordering": list(ordering),
        "level": 2,
        "left_prefix": list(left_prefix),
        "right_prefix": list(right_prefix),
        "completion_mask": left_mask,
        "left_pcrnf": pcrnf_record(left),
        "right_pcrnf": pcrnf_record(right),
    }


def _exhaustive_row(n: int) -> dict[str, object]:
    counters: Counter[str] = Counter()
    maxima: Counter[str] = Counter()
    digest = hashlib.sha256()
    orderings = tuple(itertools.permutations(range(n)))
    for instance in labelled_instances(n):
        for ordering in orderings:
            comparison = compare_pcrnf_profile(instance, ordering)
            counters["profiles"] += 1
            for level in comparison.levels:
                counters["levels"] += 1
                counters["prefixes"] += level.prefix_count
                counters["pcrnf_states"] += level.pcrnf_state_count
                counters["exact_classes"] += level.exact_class_count
                counters["live_pcrnf_states"] += level.live_pcrnf_state_count
                counters["dead_pcrnf_states"] += level.dead_pcrnf_state_count
                counters["incompleteness_excess"] += level.incompleteness_excess
                counters["unique_encoded_bytes"] += level.total_unique_encoded_bytes
                maxima["pcrnf_states"] = max(
                    maxima["pcrnf_states"],
                    level.pcrnf_state_count,
                )
                maxima["exact_classes"] = max(
                    maxima["exact_classes"],
                    level.exact_class_count,
                )
                maxima["incompleteness_excess"] = max(
                    maxima["incompleteness_excess"],
                    level.incompleteness_excess,
                )
                signature = [
                    instance_id(instance),
                    list(ordering),
                    level.level,
                    level.pcrnf_state_count,
                    level.exact_class_count,
                    level.live_pcrnf_state_count,
                    level.dead_pcrnf_state_count,
                    level.incompleteness_excess,
                    level.total_unique_encoded_bytes,
                ]
                digest.update(
                    json.dumps(
                        signature,
                        separators=(",", ":"),
                        ensure_ascii=True,
                    ).encode("utf-8")
                )
                digest.update(b"\n")
    return {
        "n": n,
        "instances": sum(1 for _ in labelled_instances(n)),
        "orderings_per_instance": len(orderings),
        **dict(counters),
        "maxima": dict(maxima),
        "measurement_sequence_sha256": digest.hexdigest(),
    }


def _fan_samples() -> list[dict[str, object]]:
    samples: list[dict[str, object]] = []
    for edge_count in range(1, 7):
        instance = fan_instance(edge_count)
        bad_levels = traverse_pcrnf(instance, fan_bad_ordering(edge_count))
        good_levels = traverse_pcrnf(instance, fan_good_ordering(edge_count))
        bad_counts = [len(level) for level in bad_levels]
        good_counts = [len(level) for level in good_levels]
        expected_peak = (1 << (edge_count + 1)) - 1
        if max(bad_counts) != expected_peak:
            raise AssertionError("bad fan PCRNF peak formula failed")
        if max(good_counts) > 5:
            raise AssertionError("good fan PCRNF state count exceeded five")
        samples.append(
            {
                "edge_count": edge_count,
                "vertices": instance.n,
                "bad_state_counts_by_level": bad_counts,
                "bad_peak_states": max(bad_counts),
                "bad_total_level_states": sum(bad_counts),
                "good_state_counts_by_level": good_counts,
                "good_peak_states": max(good_counts),
                "good_total_level_states": sum(good_counts),
            }
        )
    return samples


def pcrnf_attack_payload() -> dict[str, object]:
    rows = [_exhaustive_row(n) for n in range(5)]
    if any(row["incompleteness_excess"] != 0 for row in rows):
        raise AssertionError("PCRNF ceased to equal exact classes through four vertices")
    return {
        "format": FORMAT,
        "computation": COMPUTATION,
        "representation": {
            "name": "oriented propagation-closed signed residual normal form",
            "equality": "byte equality of canonical labelled residuals",
            "semantics": "exact labelled completion set",
            "orientation_repair": (
                "one component flip bit records how canonical component colours "
                "map back to original labelled colours"
            ),
        },
        "unoriented_normalization": orientation_counterexample(),
        "oriented_exactness": {
            "status": "PROVED / CHECKED",
            "claim": (
                "direct substitution, deterministic propagation closure, and "
                "recorded component orientation preserve exact labelled residual semantics"
            ),
        },
        "exhaustive_domain": {
            "status": "COMPUTATIONAL / CHECKED",
            "domain": "all labelled instances and all orderings through n=4",
            "rows": rows,
        },
        "first_strict_incompleteness": incompleteness_witness(),
        "fan_family": {
            "status": "PROVED / CHECKED",
            "bad_order_peak_states": "2^(k+1)-1",
            "good_order_peak_states": "at most 5 including a possible dead state",
            "samples": _fan_samples(),
        },
        "route_decision": {
            "candidate": "NAE-016",
            "status": "RETRACTED",
            "reason": (
                "oriented PCRNF is an exact residual syntax but byte equality is "
                "not exact semantic equivalence; the first strict gap occurs on "
                "five vertices, and no polynomial total reachable-state bound "
                "survived the required attacks"
            ),
            "retained": (
                "exact oriented residualization and propagation closure as a "
                "reference representation and restricted algorithmic control"
            ),
        },
        "limitations": [
            "the five-vertex witness disproves semantic completeness of byte equality, not soundness",
            "failure of PCRNF does not lower-bound arbitrary representations or algorithms",
            "the fan theorem separates orderings but is not an every-ordering lower bound",
            "finite exhaustive agreement through four vertices is not a universal proof by itself",
            "no conclusion about P=NP or P!=NP follows",
        ],
    }


def pcrnf_attack_record() -> dict[str, object]:
    payload = pcrnf_attack_payload()
    payload_bytes = json.dumps(
        payload,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return {
        **payload,
        "payload_sha256": hashlib.sha256(payload_bytes).hexdigest(),
    }


def pcrnf_attack_bytes() -> bytes:
    return json.dumps(
        pcrnf_attack_record(),
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
