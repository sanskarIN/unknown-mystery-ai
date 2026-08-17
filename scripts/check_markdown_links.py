"""Check repository-local Markdown links without network access.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def check_file(path: Path) -> list[str]:
    failures: list[str] = []
    text = path.read_text(encoding="utf-8")
    for target in LINK.findall(text):
        target = target.strip().split(" ", 1)[0].strip("<>")
        if not target or target.startswith(SKIP_PREFIXES):
            continue
        target_path = target.split("#", 1)[0]
        if not target_path:
            continue
        resolved = (path.parent / target_path).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            failures.append(f"{path.relative_to(ROOT)} -> escapes repository: {target}")
            continue
        if not resolved.exists():
            failures.append(f"{path.relative_to(ROOT)} -> missing: {target}")
    return failures


def main() -> int:
    failures: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        failures.extend(check_file(path))
    if failures:
        print("Broken internal Markdown links:")
        for failure in failures:
            print("-", failure)
        return 1
    print("Internal Markdown links: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
