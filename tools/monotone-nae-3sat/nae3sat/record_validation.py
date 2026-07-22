"""Strict public envelope verification for committed research records.

Digest agreement alone proves only internal byte integrity. These wrappers also
validate the versioned top-level contract before accepting a record. Full
semantic verification remains regeneration plus byte comparison.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping

from .calibration import FORMAT as CALIBRATION_FORMAT
from .census import CORPUS_FORMAT, GENERATOR as CORPUS_GENERATOR
from .obstruction_atlas import FORMAT as ATLAS_FORMAT
from .profile_census import (
    FORMAT as PROFILE_FORMAT,
    GENERATOR as PROFILE_GENERATOR,
)
from .summary_atlas import FORMAT as SUMMARY_COLLISION_FORMAT


def _compact_json(value: object) -> bytes:
    return json.dumps(
        value,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")


def _valid_digest(value: object) -> bool:
    return (
        type(value) is str
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _verify_envelope(
    record: object,
    *,
    keys: frozenset[str],
    format_name: str,
    fixed_fields: Mapping[str, object],
) -> bool:
    if type(record) is not dict or set(record) != keys:
        return False
    if record.get("format") != format_name:
        return False
    if any(record.get(key) != value for key, value in fixed_fields.items()):
        return False
    digest = record.get("payload_sha256")
    if not _valid_digest(digest):
        return False
    payload = {
        key: value
        for key, value in record.items()
        if key != "payload_sha256"
    }
    return hashlib.sha256(_compact_json(payload)).hexdigest() == digest


def verify_corpus_record(record: object) -> bool:
    return _verify_envelope(
        record,
        keys=frozenset(
            {
                "format",
                "domain",
                "generator",
                "computation",
                "counts",
                "totals",
                "payload_sha256",
            }
        ),
        format_name=CORPUS_FORMAT,
        fixed_fields={
            "generator": CORPUS_GENERATOR,
            "computation": "finite-exhaustive",
        },
    )


def verify_profile_corpus_record(record: object) -> bool:
    return _verify_envelope(
        record,
        keys=frozenset(
            {
                "format",
                "domain",
                "generator",
                "computation",
                "profile_sequence_sha256_by_n",
                "counts",
                "totals",
                "payload_sha256",
            }
        ),
        format_name=PROFILE_FORMAT,
        fixed_fields={
            "generator": PROFILE_GENERATOR,
            "computation": "finite-exhaustive",
        },
    )


def verify_calibration_record(record: object) -> bool:
    return _verify_envelope(
        record,
        keys=frozenset(
            {
                "format",
                "computation",
                "mechanisms",
                "graph",
                "xor",
                "nae",
                "external_boundaries",
                "limitations",
                "payload_sha256",
            }
        ),
        format_name=CALIBRATION_FORMAT,
        fixed_fields={"computation": "finite-exhaustive-controls"},
    )


def verify_obstruction_atlas_record(record: object) -> bool:
    return _verify_envelope(
        record,
        keys=frozenset(
            {
                "format",
                "computation",
                "definitions",
                "small_domain_census",
                "named_obstructions",
                "external_sources",
                "limitations",
                "payload_sha256",
            }
        ),
        format_name=ATLAS_FORMAT,
        fixed_fields={
            "computation": (
                "finite-exhaustive-census-plus-named-controls"
            )
        },
    )


def verify_summary_collision_record(record: object) -> bool:
    return _verify_envelope(
        record,
        keys=frozenset(
            {
                "format",
                "computation",
                "semantic_targets",
                "collisions",
                "bounded_radius_family",
                "retained_control",
                "limitations",
                "payload_sha256",
            }
        ),
        format_name=SUMMARY_COLLISION_FORMAT,
        fixed_fields={
            "computation": (
                "explicit-counterexamples-plus-constructive-family"
            )
        },
    )
