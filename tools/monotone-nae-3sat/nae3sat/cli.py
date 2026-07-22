from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Sequence

from .calibration import calibration_bytes
from .census import corpus_bytes
from .errors import NAE3Error, ValidationError
from .model import incidence_components
from .obstruction_atlas import obstruction_atlas_bytes
from .oracle import count_satisfying_assignments, solve_exact
from .profile import build_exact_profile, profile_bytes
from .profile_census import profile_corpus_bytes
from .serialization import (
    FORMAT_VERSION,
    encoded_size_bytes,
    instance_id,
    parse_instance_json,
)
from .summary_atlas import summary_collision_bytes


def _load(path: Path):
    return parse_instance_json(path.read_bytes())


def _dump(value: object) -> None:
    print(json.dumps(value, separators=(",", ":"), ensure_ascii=True))


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


def _parse_ordering(text: str | None, n: int) -> tuple[int, ...]:
    if text is None:
        return tuple(range(n))
    if text == "" and n == 0:
        return ()
    try:
        return tuple(int(part) for part in text.split(","))
    except ValueError as exc:
        raise ValidationError(
            "ordering must be a comma-separated integer permutation"
        ) from exc


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python3 -m nae3sat.cli")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate")
    validate.add_argument("path", type=Path)

    solve = sub.add_parser("solve")
    solve.add_argument("path", type=Path)
    solve.add_argument("--no-symmetry", action="store_true")

    count = sub.add_parser("count")
    count.add_argument("path", type=Path)

    census = sub.add_parser("census")
    census.add_argument("--max-vertices", type=int, default=5)
    census.add_argument("--output", type=Path, required=True)
    census.add_argument("--allow-large-domain", action="store_true")

    profile = sub.add_parser("profile")
    profile.add_argument("path", type=Path)
    profile.add_argument("--ordering")

    profile_census = sub.add_parser("profile-census")
    profile_census.add_argument("--max-vertices", type=int, default=5)
    profile_census.add_argument("--output", type=Path, required=True)
    profile_census.add_argument("--allow-large-domain", action="store_true")

    calibrate = sub.add_parser("calibrate")
    calibrate.add_argument("--output", type=Path, required=True)

    obstruction_atlas = sub.add_parser("obstruction-atlas")
    obstruction_atlas.add_argument("--output", type=Path, required=True)

    summary_collisions = sub.add_parser("summary-collisions")
    summary_collisions.add_argument("--output", type=Path, required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            instance = _load(args.path)
            components = incidence_components(instance)
            active = {
                vertex
                for edge in instance.edges
                for vertex in edge
            }
            _dump(
                {
                    "format": f"{FORMAT_VERSION}-summary",
                    "id": instance_id(instance),
                    "n": instance.n,
                    "m": len(instance.edges),
                    "components_total": len(components),
                    "components_nontrivial": sum(
                        1
                        for component in components
                        if any(vertex in active for vertex in component)
                    ),
                    "encoded_bytes": encoded_size_bytes(instance),
                }
            )
        elif args.command == "solve":
            instance = _load(args.path)
            result = solve_exact(
                instance,
                use_symmetry=not args.no_symmetry,
            )
            _dump(
                {
                    "format": f"{FORMAT_VERSION}-solve",
                    "id": instance_id(instance),
                    "satisfiable": result.satisfiable,
                    "witness": (
                        list(result.witness)
                        if result.witness is not None
                        else None
                    ),
                    "assignments_tested": result.assignments_tested,
                    "symmetry_reduction": result.symmetry_reduction,
                }
            )
        elif args.command == "count":
            instance = _load(args.path)
            _dump(
                {
                    "format": f"{FORMAT_VERSION}-count",
                    "id": instance_id(instance),
                    "satisfying_assignments": (
                        count_satisfying_assignments(instance)
                    ),
                }
            )
        elif args.command == "census":
            if args.max_vertices < 0:
                raise ValidationError("max vertices must be nonnegative")
            if args.max_vertices > 5 and not args.allow_large_domain:
                raise ValidationError(
                    "max vertices above 5 requires --allow-large-domain"
                )
            _write_atomic(args.output, corpus_bytes(args.max_vertices))
        elif args.command == "profile":
            instance = _load(args.path)
            ordering = _parse_ordering(args.ordering, instance.n)
            exact = build_exact_profile(instance, ordering)
            classes = [level.class_count for level in exact.levels]
            _dump(
                {
                    "format": "nae3-vs03-summary-v1",
                    "id": instance_id(instance),
                    "ordering": list(exact.ordering),
                    "satisfiable": exact.satisfiable,
                    "max_classes": max(classes),
                    "total_classes": sum(classes),
                    "profile_bytes": len(profile_bytes(exact)),
                }
            )
        elif args.command == "profile-census":
            if args.max_vertices < 0:
                raise ValidationError("max vertices must be nonnegative")
            if args.max_vertices > 5 and not args.allow_large_domain:
                raise ValidationError(
                    "max vertices above 5 requires --allow-large-domain"
                )
            _write_atomic(
                args.output,
                profile_corpus_bytes(args.max_vertices),
            )
        elif args.command == "calibrate":
            _write_atomic(args.output, calibration_bytes())
        elif args.command == "obstruction-atlas":
            _write_atomic(args.output, obstruction_atlas_bytes())
        else:
            _write_atomic(args.output, summary_collision_bytes())
        return 0
    except (NAE3Error, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
