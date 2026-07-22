#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
MODE=${1:-fast}
PYTHON=${PYTHON:-python3}
TOOL_DIR="$ROOT/tools/monotone-nae-3sat"

fail() {
  printf '%s\n' "error: $*" >&2
  exit 2
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || fail "required command not found: $1"
}

require_clean_tree() {
  require_command git
  git -C "$ROOT" diff --quiet || fail "working tree has unstaged changes; checks must match the pushed commit"
  git -C "$ROOT" diff --cached --quiet || fail "index has staged changes; commit them before running push/full checks"
}

check_staged() {
  require_command git
  require_command "$PYTHON"
  git -C "$ROOT" diff --cached --check

  staged_file=$(mktemp "${TMPDIR:-/tmp}/math-research-staged-list.XXXXXX")
  staged_dir=$(mktemp -d "${TMPDIR:-/tmp}/math-research-staged-files.XXXXXX")
  trap 'rm -f "$staged_file"; rm -rf "$staged_dir"' EXIT HUP INT TERM
  git -C "$ROOT" diff --cached --name-only --diff-filter=ACMR >"$staged_file"

  index=0
  while IFS= read -r path; do
    [ -n "$path" ] || continue
    index=$((index + 1))
    staged_copy="$staged_dir/$index"
    git -C "$ROOT" show ":$path" >"$staged_copy"
    case "$path" in
      *.py)
        "$PYTHON" -m py_compile "$staged_copy"
        ;;
      *.sh|.githooks/*)
        sh -n "$staged_copy"
        ;;
    esac
  done <"$staged_file"

  printf '%s\n' "staged checks passed"
}

check_committed_records() {
  "$PYTHON" - <<'PY'
import json
from pathlib import Path

from nae3sat import (
    verify_calibration_record,
    verify_corpus_record,
    verify_obstruction_atlas_record,
    verify_profile_corpus_record,
)

records = (
    (Path("corpus/all-labelled-n-le-5.json"), verify_corpus_record),
    (Path("profile-corpus/all-labelled-orderings-n-le-5.json"), verify_profile_corpus_record),
    (Path("calibration/vs04-calibration.json"), verify_calibration_record),
    (Path("obstruction-atlas/vs05-obstruction-atlas.json"), verify_obstruction_atlas_record),
)
for path, verify in records:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not verify(value):
        raise SystemExit(f"record verification failed: {path}")
print("committed record digests passed")
PY
}

check_fast() {
  require_command "$PYTHON"
  require_clean_tree
  cd "$TOOL_DIR"
  "$PYTHON" -m compileall -q nae3sat tests
  "$PYTHON" -m unittest discover -s tests -v
  "$PYTHON" -m nae3sat.cli validate tests/fixtures/fano-plane.json >/dev/null
  "$PYTHON" -m nae3sat.cli solve tests/fixtures/single-edge.json >/dev/null
  "$PYTHON" -m nae3sat.cli count tests/fixtures/single-edge.json >/dev/null
  "$PYTHON" -m nae3sat.cli profile tests/fixtures/single-edge.json --ordering 2,0,1 >/dev/null
  check_committed_records
  printf '%s\n' "fast checks passed"
}

check_full() {
  require_command cmp
  check_fast
  cd "$TOOL_DIR"
  NAE3_FULL_VS03_REFERENCE=1 "$PYTHON" -m unittest discover -s tests -p 'test_vs03*.py' -v
  NAE3_FULL_VS05_ATLAS=1 "$PYTHON" -m unittest discover -s tests -p 'test_vs05.py' -v

  output_dir=$(mktemp -d "${TMPDIR:-/tmp}/math-research-full.XXXXXX")
  trap 'rm -rf "$output_dir"' EXIT HUP INT TERM
  "$PYTHON" -m nae3sat.cli census --max-vertices 5 --output "$output_dir/vs02.json"
  cmp "$output_dir/vs02.json" corpus/all-labelled-n-le-5.json
  "$PYTHON" -m nae3sat.cli profile-census --max-vertices 5 --output "$output_dir/vs03.json"
  cmp "$output_dir/vs03.json" profile-corpus/all-labelled-orderings-n-le-5.json
  "$PYTHON" -m nae3sat.cli calibrate --output "$output_dir/vs04.json"
  cmp "$output_dir/vs04.json" calibration/vs04-calibration.json
  printf '%s\n' "full checks passed"
}

case "$MODE" in
  staged) check_staged ;;
  fast) check_fast ;;
  full) check_full ;;
  *) fail "usage: $0 [staged|fast|full]" ;;
esac
