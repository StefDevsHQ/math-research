"""Canonical published VS-07 record with the strongest checked fan bound."""

from __future__ import annotations

import hashlib
import json

from .semantic_merging_atlas import semantic_merging_payload


def semantic_merging_record() -> dict[str, object]:
    payload = semantic_merging_payload()
    payload["fan_family"]["good_ordering_theorem"][
        "maximum_live_exact_classes"
    ] = 4
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
