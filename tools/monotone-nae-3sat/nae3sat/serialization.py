"""Strict versioned JSON parsing and deterministic serialization."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from .errors import ParseError, ValidationError
from .model import Hypergraph3, normalize_instance

FORMAT_VERSION = "nae3-v1"
ID_PREFIX = "nae3-v1-sha256-"


def _reject_constant(value: str) -> None:
    raise ParseError(f"nonstandard JSON numeric constant is not allowed: {value}")


def _strict_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ParseError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def parse_instance_json(data: str | bytes) -> Hypergraph3:
    if isinstance(data, bytes):
        try:
            text = data.decode("utf-8", errors="strict")
        except UnicodeDecodeError as exc:
            raise ParseError("input bytes are not valid UTF-8") from exc
    elif isinstance(data, str):
        text = data
    else:
        raise ParseError("serialized input must be str or bytes")
    try:
        document = json.loads(text, object_pairs_hook=_strict_object, parse_constant=_reject_constant)
    except ParseError:
        raise
    except (json.JSONDecodeError, TypeError, ValueError) as exc:
        raise ParseError(f"invalid JSON: {exc}") from exc
    if type(document) is not dict:
        raise ParseError("top-level JSON value must be an object")
    expected = {"format", "vertices", "edges"}
    if set(document) != expected:
        raise ParseError("top-level schema mismatch")
    if document["format"] != FORMAT_VERSION:
        raise ParseError(f"unsupported format version: {document['format']!r}")
    vertices = document["vertices"]
    if type(vertices) is not list or any(type(v) is not int for v in vertices):
        raise ParseError("vertices must be a JSON array of integers excluding Booleans")
    if len(set(vertices)) != len(vertices) or sorted(vertices) != list(range(len(vertices))):
        raise ParseError("vertex set must be exactly 0, ..., n-1")
    edges = document["edges"]
    if type(edges) is not list or any(type(edge) is not list for edge in edges):
        raise ParseError("edges must be a JSON array of arrays")
    try:
        return normalize_instance(len(vertices), edges)
    except ValidationError as exc:
        raise ParseError(str(exc)) from exc


def to_canonical_json(instance: Hypergraph3) -> str:
    document = {"format": FORMAT_VERSION, "vertices": list(range(instance.n)), "edges": [list(e) for e in instance.edges]}
    return json.dumps(document, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def canonical_bytes(instance: Hypergraph3) -> bytes:
    return to_canonical_json(instance).encode("utf-8")


def instance_id(instance: Hypergraph3) -> str:
    return ID_PREFIX + hashlib.sha256(canonical_bytes(instance)).hexdigest()


def encoded_size_bytes(instance: Hypergraph3) -> int:
    return len(canonical_bytes(instance))
