"""Require external GitHub Actions to be pinned to full commit SHAs.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
USES = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)", re.MULTILINE)
SHA = re.compile(r"^[0-9a-fA-F]{40}$")


def main() -> int:
    failures: list[str] = []
    for path in sorted(WORKFLOWS.glob("*.yml")):
        text = path.read_text(encoding="utf-8")
        for reference in USES.findall(text):
            if reference.startswith("./"):
                continue
            if "@" not in reference:
                failures.append(f"{path.relative_to(ROOT)}: missing ref for {reference}")
                continue
            action, ref = reference.rsplit("@", 1)
            if not SHA.fullmatch(ref):
                failures.append(
                    f"{path.relative_to(ROOT)}: {action} must use a 40-character commit SHA, got {ref}"
                )

    if failures:
        print("Workflow action pins: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    print("Workflow action pins: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
