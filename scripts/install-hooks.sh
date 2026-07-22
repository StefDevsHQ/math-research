#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
command -v git >/dev/null 2>&1 || {
  printf '%s\n' "error: git is required" >&2
  exit 2
}

git -C "$ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
  printf '%s\n' "error: not inside a Git work tree" >&2
  exit 2
}

chmod +x \
  "$ROOT/scripts/check.sh" \
  "$ROOT/scripts/install-hooks.sh" \
  "$ROOT/.githooks/pre-commit" \
  "$ROOT/.githooks/pre-push"
git -C "$ROOT" config core.hooksPath .githooks
printf '%s\n' "installed repository hooks from .githooks"
printf '%s\n' "pre-commit: exact staged syntax and whitespace checks"
printf '%s\n' "pre-push: fast checks; full checks when pushing main"
