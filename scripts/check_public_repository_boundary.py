"""Guard the public repository against accidental paid-manuscript commits.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
BLOCKED_SUFFIXES = {".pdf", ".doc", ".docx", ".epub", ".mobi"}
BLOCKED_NAMES = {
    "the_unknown_mystery_of_the_ai_complete_ebook",
    "the_unknown_mystery_of_the_ai_final_release_package",
    "the_unknown_mystery_of_the_ai_source_docx_archive",
}
SKIP_PARTS = {".git", ".venv", "build", "dist", "__pycache__"}


def main() -> int:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        relative = path.relative_to(ROOT)
        if path.suffix.lower() in BLOCKED_SUFFIXES:
            failures.append(f"blocked publication format tracked: {relative}")
        stem = path.stem.lower()
        if any(blocked in stem for blocked in BLOCKED_NAMES):
            failures.append(f"commercial manuscript/package name detected: {relative}")

    if failures:
        print("Public repository publication boundary: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    print("Public repository publication boundary: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
