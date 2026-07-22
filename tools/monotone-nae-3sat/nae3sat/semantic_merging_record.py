"""Canonical published VS-07 record.

The version-one artifact was published with the conservative value five for the
interleaved fan's maximum live-class field.  The proved sharp live bound is four;
five is only the corresponding total-class bound when one dead class is allowed.
Core executable assertions use four.  This adapter preserves the immutable
version-one record bytes until a version-two schema separates live and total
bounds explicitly.
"""

from __future__ import annotations

import hashlib
import json

from .semantic_merging_atlas import semantic_merging_payload


def semantic_merging_record() -> dict[str, object]:
    payload = semantic_merging_payload()
    payload["fan_family"]["good_ordering_theorem"][
        "maximum_live_exact_classes"
    ] = 5
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


__all__ = ["semantic_merging_bytes", "semantic_merging_record"]
