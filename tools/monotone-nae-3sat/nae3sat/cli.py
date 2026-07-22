from __future__ import annotations
import argparse, json, sys
from pathlib import Path
from typing import Sequence
from .errors import NAE3Error
from .model import incidence_components
from .serialization import FORMAT_VERSION, encoded_size_bytes, instance_id, parse_instance_json

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python3 -m nae3sat.cli")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate")
    validate.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    try:
        instance = parse_instance_json(args.path.read_bytes())
        components = incidence_components(instance)
        active = {v for e in instance.edges for v in e}
        summary = {"format":f"{FORMAT_VERSION}-summary","id":instance_id(instance),"n":instance.n,"m":len(instance.edges),"components_total":len(components),"components_nontrivial":sum(1 for c in components if any(v in active for v in c)),"encoded_bytes":encoded_size_bytes(instance)}
        print(json.dumps(summary,separators=(",",":"),ensure_ascii=True))
        return 0
    except (NAE3Error,OSError) as exc:
        print(f"error: {exc}",file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
