"""Reject change-prone X/Twitter profile URLs in durable repository files.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", "build", "dist", "__pycache__"}
TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".toml", ".yml", ".yaml", ".json", ".csv", ".ini", ".cfg", ".svg"
}
PATTERN = re.compile(r"https?://(?:www\.)?(?:x\.com|twitter\.com)/", re.IGNORECASE)
ALLOW_SELF = {Path("docs/SOCIAL_LINK_POLICY.md"), Path("scripts/check_unstable_social_links.py")}


def main() -> int:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        relative = path.relative_to(ROOT)
        if relative in ALLOW_SELF or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if PATTERN.search(text):
            failures.append(str(relative))

    if failures:
        print("Unstable social link policy: FAIL")
        for failure in failures:
            print(f"- X/Twitter URL detected: {failure}")
        return 1

    print("Unstable social link policy: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
