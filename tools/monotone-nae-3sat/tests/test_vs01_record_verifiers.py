from __future__ import annotations

import copy
import hashlib
import json
import unittest

from nae3sat import (
    calibration_record,
    corpus_record,
    obstruction_atlas_record,
    profile_corpus_record,
    verify_calibration_record,
    verify_corpus_record,
    verify_obstruction_atlas_record,
    verify_profile_corpus_record,
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
    def test_generated_records_are_accepted(self):
        cases = (
            (corpus_record(), verify_corpus_record),
            (profile_corpus_record(0), verify_profile_corpus_record),
            (calibration_record(), verify_calibration_record),
            (obstruction_atlas_record(), verify_obstruction_atlas_record),
        )
        for record, verify in cases:
            with self.subTest(format=record["format"]):
                self.assertTrue(verify(record))

    def test_redigested_wrong_format_is_rejected(self):
        cases = (
            (corpus_record(), verify_corpus_record),
            (profile_corpus_record(0), verify_profile_corpus_record),
            (calibration_record(), verify_calibration_record),
            (obstruction_atlas_record(), verify_obstruction_atlas_record),
        )
        for original, verify in cases:
            record = copy.deepcopy(original)
            record["format"] = "wrong-format"
            _redigest(record)
            with self.subTest(original_format=original["format"]):
                self.assertFalse(verify(record))

    def test_redigested_unknown_field_is_rejected(self):
        cases = (
            (corpus_record(), verify_corpus_record),
            (profile_corpus_record(0), verify_profile_corpus_record),
            (calibration_record(), verify_calibration_record),
            (obstruction_atlas_record(), verify_obstruction_atlas_record),
        )
        for original, verify in cases:
            record = copy.deepcopy(original)
            record["unexpected"] = True
            _redigest(record)
            with self.subTest(format=original["format"]):
                self.assertFalse(verify(record))

    def test_malformed_digest_is_rejected(self):
        cases = (
            (corpus_record(), verify_corpus_record),
            (profile_corpus_record(0), verify_profile_corpus_record),
            (calibration_record(), verify_calibration_record),
            (obstruction_atlas_record(), verify_obstruction_atlas_record),
        )
        malformed = (None, 0, "", "0" * 63, "G" * 64, "A" * 64)
        for original, verify in cases:
            for digest in malformed:
                record = copy.deepcopy(original)
                record["payload_sha256"] = digest
                with self.subTest(format=original["format"], digest=digest):
                    self.assertFalse(verify(record))


if __name__ == "__main__":
    unittest.main()
