"""Command-line writer for the deterministic VS-07 record."""

from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path
from typing import Sequence

from .semantic_merging_record import semantic_merging_bytes


def _write_atomic(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=path.name + ".",
        suffix=".tmp",
        dir=path.parent,
    )
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python3 -m nae3sat.semantic_merging_cli"
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    _write_atomic(args.output, semantic_merging_bytes())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
