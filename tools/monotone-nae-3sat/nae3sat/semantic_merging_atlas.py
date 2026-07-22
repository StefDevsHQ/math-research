"""Deterministic VS-07 record for live semantic merging."""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter

from .model import Hypergraph3, normalize_instance
from .oracle import labelled_instances, solve_exact
from .semantic_merging import (
    fan_bad_ordering,
    fan_good_ordering,
    fan_instance,
    measure_semantic_merging_level,
    measure_semantic_merging_profile,
)
from .serialization import instance_id

FORMAT = "nae3-vs07-semantic-merging-v1"
COMPUTATION = "finite-exhaustive-through-four-plus-proved-fan-family"


def _instance_record(instance: Hypergraph3) -> dict[str, object]:
    return {
        "id": instance_id(instance),
        "n": instance.n,
        "edges": [list(edge) for edge in instance.edges],
    }


def _level_record(level) -> dict[str, int]:
    return {
        field: getattr(level, field)
        for field in level.__dataclass_fields__
    }


def first_all_live_cross_orbit_merge() -> dict[str, object]:
    instance = normalize_instance(
        4,
        ((0, 1, 2), (0, 1, 3)),
    )
    ordering = (0, 2, 3, 1)
    level = 3
    measurement = measure_semantic_merging_level(
        instance,
        ordering,
        level,
    )
    expected = {
        "live_prefix_count": 8,
        "dead_prefix_count": 0,
        "live_semantic_class_count": 3,
        "live_prefix_component_orbit_count": 4,
        "live_semantic_component_orbit_count": 2,
        "exact_cross_orbit_merge_class_count": 2,
        "exact_cross_orbit_merge_excess": 4,
        "orbit_normalized_merge_excess": 2,
        "boundary_width": 3,
        "live_boundary_state_count": 8,
    }
    for key, value in expected.items():
        if getattr(measurement, key) != value:
            raise AssertionError(f"first live merge metric changed: {key}")
    return {
        "status": "COMPUTATIONAL / CHECKED",
        "claim": (
            "an all-live fixed-level profile can merge distinct component-"
            "complement prefix orbits into the same exact completion class"
        ),
        "instance": _instance_record(instance),
        "ordering": list(ordering),
        "level": level,
        "completion_masks_by_prefix": [2, 2, 2, 3, 3, 1, 1, 1],
        "measurement": _level_record(measurement),
    }


def _fan_samples() -> list[dict[str, object]]:
    samples: list[dict[str, object]] = []
    for edge_count in range(1, 7):
        instance = fan_instance(edge_count)
        bad_ordering = fan_bad_ordering(edge_count)
        good_ordering = fan_good_ordering(edge_count)
        bad = measure_semantic_merging_profile(instance, bad_ordering)
        good = measure_semantic_merging_profile(instance, good_ordering)
        middle = bad.levels[edge_count + 1]
        expected_exact = (1 << (edge_count + 1)) - 1
        expected_orbits = 1 << edge_count
        if middle.live_prefix_count != 1 << (edge_count + 1):
            raise AssertionError("fan middle level must be entirely live")
        if middle.live_semantic_class_count != expected_exact:
            raise AssertionError("fan exact-class formula failed")
        if middle.live_prefix_component_orbit_count != expected_orbits:
            raise AssertionError("fan prefix-orbit formula failed")
        if middle.live_semantic_component_orbit_count != expected_orbits:
            raise AssertionError("fan semantic-orbit formula failed")
        if middle.live_boundary_state_count != 1 << (edge_count + 1):
            raise AssertionError("fan boundary-state formula failed")
        if middle.exact_cross_orbit_merge_excess != 0:
            raise AssertionError(
                "fan exact merging must not cross symmetry orbits"
            )
        if max(level.boundary_width for level in good.levels) > 2:
            raise AssertionError("interleaved fan ordering exceeded width two")
        if good.peak_live_semantic_classes > 4:
            raise AssertionError(
                "interleaved fan ordering exceeded four live classes"
            )
        samples.append(
            {
                "edge_count": edge_count,
                "vertices": instance.n,
                "bad_middle": _level_record(middle),
                "bad_peak_live_semantic_classes": (
                    bad.peak_live_semantic_classes
                ),
                "bad_peak_live_semantic_component_orbits": (
                    bad.peak_live_semantic_component_orbits
                ),
                "bad_peak_live_boundary_states": (
                    bad.peak_live_boundary_states
                ),
                "bad_profile_json_bytes": bad.exact_profile_json_bytes,
                "good_max_boundary_width": max(
                    level.boundary_width for level in good.levels
                ),
                "good_peak_live_semantic_classes": (
                    good.peak_live_semantic_classes
                ),
                "good_peak_live_semantic_component_orbits": (
                    good.peak_live_semantic_component_orbits
                ),
                "good_peak_live_boundary_states": (
                    good.peak_live_boundary_states
                ),
                "good_profile_json_bytes": good.exact_profile_json_bytes,
            }
        )
    return samples


def _exhaustive_row(n: int) -> dict[str, object]:
    counters: Counter[str] = Counter()
    maxima: Counter[str] = Counter()
    digest = hashlib.sha256()
    orderings = tuple(itertools.permutations(range(n)))
    for instance in labelled_instances(n):
        satisfiable = solve_exact(instance).satisfiable
        for ordering in orderings:
            profile = measure_semantic_merging_profile(instance, ordering)
            counters["profiles"] += 1
            counters["satisfiable_profiles"] += int(satisfiable)
            counters["profile_json_bytes"] += profile.exact_profile_json_bytes
            maxima["profile_json_bytes"] = max(
                maxima["profile_json_bytes"],
                profile.exact_profile_json_bytes,
            )
            signature: list[object] = [
                instance_id(instance),
                list(ordering),
                [],
            ]
            for level in profile.levels:
                counters["levels"] += 1
                counters["prefixes"] += level.prefix_count
                counters["live_prefixes"] += level.live_prefix_count
                counters["dead_prefixes"] += level.dead_prefix_count
                counters["semantic_classes"] += level.semantic_class_count
                counters["live_semantic_classes"] += (
                    level.live_semantic_class_count
                )
                counters["live_prefix_component_orbits"] += (
                    level.live_prefix_component_orbit_count
                )
                counters["live_semantic_component_orbits"] += (
                    level.live_semantic_component_orbit_count
                )
                counters["processed_valid_boundary_states"] += (
                    level.processed_valid_boundary_state_count
                )
                counters["live_boundary_states"] += (
                    level.live_boundary_state_count
                )
                counters["levels_with_cross_orbit_merge"] += int(
                    level.exact_cross_orbit_merge_excess > 0
                )
                counters["all_live_levels_with_cross_orbit_merge"] += int(
                    level.dead_prefix_count == 0
                    and level.exact_cross_orbit_merge_excess > 0
                )
                maxima["live_semantic_classes"] = max(
                    maxima["live_semantic_classes"],
                    level.live_semantic_class_count,
                )
                maxima["live_semantic_component_orbits"] = max(
                    maxima["live_semantic_component_orbits"],
                    level.live_semantic_component_orbit_count,
                )
                maxima["live_boundary_states"] = max(
                    maxima["live_boundary_states"],
                    level.live_boundary_state_count,
                )
                signature[2].append(_level_record(level))
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


def semantic_merging_payload() -> dict[str, object]:
    exhaustive = [_exhaustive_row(n) for n in range(5)]
    return {
        "format": FORMAT,
        "computation": COMPUTATION,
        "definitions": {
            "live_prefix": "prefix with at least one satisfying completion",
            "exact_semantic_class": "equality class of exact completion masks",
            "component_complement_orbit": (
                "orbit under independently complementing incidence components"
            ),
            "genuine_exact_merge": (
                "one exact completion class containing multiple live prefix "
                "component-complement orbits"
            ),
            "boundary_state": (
                "exact assignment on the processed boundary at one fixed level"
            ),
        },
        "first_all_live_cross_orbit_merge": (
            first_all_live_cross_orbit_merge()
        ),
        "fan_family": {
            "status": "PROVED / CHECKED",
            "instance": (
                "F_k has edges {c,a_i,b_i} for 1<=i<=k and 2k+1 vertices"
            ),
            "bad_ordering": "c,a_1,...,a_k,b_1,...,b_k",
            "bad_middle_level_theorem": {
                "level": "k+1",
                "all_prefixes_live": "2^(k+1)",
                "exact_live_classes": "2^(k+1)-1",
                "component_complement_prefix_orbits": "2^k",
                "component_complement_semantic_orbits": "2^k",
                "live_boundary_states": "2^(k+1)",
                "cross_orbit_exact_merge_excess": "0",
            },
            "good_ordering": "c,a_1,b_1,...,a_k,b_k",
            "good_ordering_theorem": {
                "maximum_boundary_width": 2,
                # The v1 record retains the original conservative live-class
                # ceiling. The authoritative sharp theorem and executable
                # assertion are four live classes; five is also a valid but
                # weaker ceiling and leaves the committed v1 bytes stable.
                "maximum_live_exact_classes": 5,
            },
            "samples": _fan_samples(),
        },
        "exhaustive_domain": {
            "domain": "all labelled instances and all orderings through n=4",
            "status": "COMPUTATIONAL / CHECKED",
            "rows": exhaustive,
        },
        "limitations": [
            "the exhaustive census stops at four vertices",
            "the fan theorem is an ordering-separation theorem, not a universal lower bound",
            "exact class count does not bound the size of an unspecified symbolic representation",
            "dense completion masks and JSON bytes are reference encodings, not optimal encodings",
            "no result proves P=NP or P!=NP",
        ],
    }


def semantic_merging_record() -> dict[str, object]:
    payload = semantic_merging_payload()
    payload_bytes = json.dumps(
        payload,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return {
        **payload,
        "payload_sha256": hashlib.sha256(payload_bytes).hexdigest(),
    }


def semantic_merging_bytes() -> bytes:
    return json.dumps(
        semantic_merging_record(),
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
