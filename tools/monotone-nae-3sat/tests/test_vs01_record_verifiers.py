from __future__ import annotations

import copy
import hashlib
import json
import unittest
from pathlib import Path

from nae3sat import (
    verify_calibration_record,
    verify_corpus_record,
    verify_obstruction_atlas_record,
    verify_profile_corpus_record,
    verify_summary_collision_record,
)

ROOT = Path(__file__).parents[1]


def _load(relative: str) -> dict[str, object]:
    value = json.loads((ROOT / relative).read_text(encoding="utf-8"))
    if type(value) is not dict:
        raise AssertionError("committed record must be a JSON object")
    return value


def _cases():
    return (
        (_load("corpus/all-labelled-n-le-5.json"), verify_corpus_record),
        (
            _load("profile-corpus/all-labelled-orderings-n-le-5.json"),
            verify_profile_corpus_record,
        ),
        (_load("calibration/vs04-calibration.json"), verify_calibration_record),
        (
            _load("obstruction-atlas/vs05-obstruction-atlas.json"),
            verify_obstruction_atlas_record,
        ),
        (
            _load("summary-collisions/vs06-summary-collisions.json"),
            verify_summary_collision_record,
        ),
    )


def _redigest(record: dict[str, object]) -> None:
    payload = {
        key: value for key, value in record.items() if key != "payload_sha256"
    }
    payload_bytes = json.dumps(
        payload,
        separators=(",", ":"),
        ensure_ascii=True,
    ).encode("utf-8")
    record["payload_sha256"] = hashlib.sha256(payload_bytes).hexdigest()


class StrictRecordVerifierTests(unittest.TestCase):
    def test_committed_records_are_accepted(self):
        for record, verify in _cases():
            with self.subTest(format=record["format"]):
                self.assertTrue(verify(record))

    def test_redigested_wrong_format_is_rejected(self):
        for original, verify in _cases():
            record = copy.deepcopy(original)
            record["format"] = "wrong-format"
            _redigest(record)
            with self.subTest(original_format=original["format"]):
                self.assertFalse(verify(record))

    def test_redigested_unknown_field_is_rejected(self):
        for original, verify in _cases():
            record = copy.deepcopy(original)
            record["unexpected"] = True
            _redigest(record)
            with self.subTest(format=original["format"]):
                self.assertFalse(verify(record))

    def test_malformed_digest_is_rejected(self):
        malformed = (None, 0, "", "0" * 63, "G" * 64, "A" * 64)
        for original, verify in _cases():
            for digest in malformed:
                record = copy.deepcopy(original)
                record["payload_sha256"] = digest
                with self.subTest(format=original["format"], digest=digest):
                    self.assertFalse(verify(record))


if __name__ == "__main__":
    unittest.main()
