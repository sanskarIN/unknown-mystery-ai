"""Compare the installed public API with a committed JSON snapshot.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import umai

ROOT = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "snapshot",
        nargs="?",
        default="api/public_api_1_0.json",
        help="repository-relative API snapshot path",
    )
    parser.add_argument(
        "--require-version-match",
        action="store_true",
        help="also require the snapshot version to equal umai.__version__",
    )
    args = parser.parse_args(argv)

    path = (ROOT / args.snapshot).resolve()
    if not path.is_file():
        print("missing API snapshot:", path)
        return 2

    payload = json.loads(path.read_text(encoding="utf-8"))
    expected = set(payload["symbols"])
    actual = set(umai.__all__)

    missing = sorted(expected - actual)
    added = sorted(actual - expected)
    version_mismatch = args.require_version_match and payload.get("version") != umai.__version__
    if missing or added or version_mismatch:
        print("Public API snapshot: FAIL")
        if missing:
            print("missing symbols:", ", ".join(missing))
        if added:
            print("untracked symbols:", ", ".join(added))
        if version_mismatch:
            print(f"version mismatch: snapshot={payload.get('version')} package={umai.__version__}")
        return 1

    print(f"Public API snapshot: PASS ({len(actual)} symbols)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
