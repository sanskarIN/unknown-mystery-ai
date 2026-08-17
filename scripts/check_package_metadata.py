"""Validate key package metadata and version consistency.

Requires Python 3.11+ for `tomllib`.
Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    errors: list[str] = []

    if project.get("name") != "unknown-mystery-ai":
        errors.append("unexpected project name")
    if project.get("readme") != "README.md":
        errors.append("README metadata must point to README.md")
    if project.get("urls", {}).get("Store") != "https://ramsandesh.gumroad.com":
        errors.append("official Gumroad Store URL is missing or incorrect")

    init_text = (ROOT / "src" / "umai" / "__init__.py").read_text(encoding="utf-8")
    match = re.search(r'^__version__\s*=\s*"([^"]+)"', init_text, re.MULTILINE)
    if not match:
        errors.append("package __version__ not found")
    elif match.group(1) != project.get("version"):
        errors.append(
            f"version mismatch: pyproject={project.get('version')} package={match.group(1)}"
        )

    if errors:
        print("Package metadata: FAIL")
        for error in errors:
            print("-", error)
        return 1
    print(f"Package metadata: PASS ({project['name']} {project['version']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
