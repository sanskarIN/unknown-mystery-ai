"""Validate canonical repository, store, and maintainer links in key files.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
GUMROAD = "https://ramsandesh.gumroad.com"
REPOSITORY = "https://github.com/sanskarIN/unknown-mystery-ai"
CONTACT = "sanskarin@outlook.in"

REQUIRED: dict[str, tuple[str, ...]] = {
    "README.md": (GUMROAD, REPOSITORY, CONTACT),
    "NOTICE": (GUMROAD,),
    "SUPPORT.md": (GUMROAD,),
    "MAINTAINERS.md": (GUMROAD, REPOSITORY, CONTACT),
    "docs/GUMROAD.md": (GUMROAD, REPOSITORY, CONTACT),
    "docs/RELEASE_STATUS.md": (GUMROAD,),
    ".github/FUNDING.yml": (GUMROAD,),
}


def main() -> int:
    failures: list[str] = []
    for relative, required_values in REQUIRED.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing key file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for value in required_values:
            if value not in text:
                failures.append(f"{relative}: missing canonical value {value}")

    if failures:
        print("Canonical project links: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    print("Canonical project links: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
