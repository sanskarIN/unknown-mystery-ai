"""Validate release notes and changelog entries for the current package version.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
GUMROAD = "https://ramsandesh.gumroad.com"


def main() -> int:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    version = str(project["version"])
    failures: list[str] = []

    notes = ROOT / "docs" / f"COMPANION_RELEASE_{version}.md"
    if not notes.is_file():
        failures.append(f"missing release notes: {notes.relative_to(ROOT)}")
    else:
        text = notes.read_text(encoding="utf-8")
        if version not in text:
            failures.append(f"release notes do not mention version {version}")
        if GUMROAD not in text:
            failures.append("release notes do not contain canonical Gumroad store")

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## [{version}]" not in changelog:
        failures.append(f"CHANGELOG.md has no [{version}] section")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if f"version-{version}-" not in readme:
        failures.append(f"README version badge is not aligned with {version}")

    if failures:
        print("Release documentation: FAIL")
        for failure in failures:
            print("-", failure)
        return 1

    print(f"Release documentation: PASS ({version})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
