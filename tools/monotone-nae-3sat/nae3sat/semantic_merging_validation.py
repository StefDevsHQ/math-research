"""Strict envelope validation for the deterministic VS-07 record."""

from __future__ import annotations

import hashlib
import json

from .semantic_merging_atlas import COMPUTATION, FORMAT


def verify_semantic_merging_record(record: object) -> bool:
    expected = {
        "format",
        "computation",
        "definitions",
        "first_all_live_cross_orbit_merge",
        "fan_family",
        "exhaustive_domain",
        "limitations",
        "payload_sha256",
    }
    if type(record) is not dict or set(record) != expected:
        return False
    if record.get("format") != FORMAT or record.get("computation") != COMPUTATION:
        return False
    digest = record.get("payload_sha256")
    if (
        type(digest) is not str
        or len(digest) != 64
        or any(character not in "0123456789abcdef" for character in digest)
    ):
        return False
    payload = {
        key: value
        for key, value in record.items()
        if key != "payload_sha256"
    }
    encoded = json.dumps(
        payload,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest() == digest
