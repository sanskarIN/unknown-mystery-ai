"""Validate the repository's coordinated 1.1.0 release-candidate invariants."""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "1.1.0"
EXPECTED_PROJECTS = 25
EXPECTED_CAPSTONE_FIXTURES = 5


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    version = str(project.get("version"))
    if version != EXPECTED_VERSION:
        fail(f"pyproject version must be {EXPECTED_VERSION}, got {version}", failures)

    init_text = (ROOT / "src" / "umai" / "__init__.py").read_text(encoding="utf-8")
    match = re.search(r'^__version__\s*=\s*"([^"]+)"', init_text, re.MULTILINE)
    if not match or match.group(1) != EXPECTED_VERSION:
        fail("package __version__ is not aligned with 1.1.0", failures)

    api_snapshot = json.loads((ROOT / "api" / "public_api_1_0.json").read_text(encoding="utf-8"))
    if api_snapshot.get("version") != EXPECTED_VERSION:
        fail("public API snapshot version is not 1.1.0", failures)

    citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    if f'version: "{EXPECTED_VERSION}"' not in citation:
        fail("CITATION.cff does not record version 1.1.0", failures)

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "version-1.1.0-brightgreen" not in readme:
        fail("README version badge is not 1.1.0", failures)

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if "## [1.1.0]" not in changelog:
        fail("CHANGELOG.md has no 1.1.0 section", failures)

    release_notes = ROOT / "docs" / "COMPANION_RELEASE_1.1.0.md"
    checklist = ROOT / "docs" / "RELEASE_1_1_0_CHECKLIST.md"
    if not release_notes.is_file():
        fail("missing 1.1.0 release notes", failures)
    if not checklist.is_file():
        fail("missing 1.1.0 release checklist", failures)

    project_mains = sorted((ROOT / "projects").glob("*/main.py"))
    if len(project_mains) != EXPECTED_PROJECTS:
        fail(f"expected {EXPECTED_PROJECTS} project entry points, found {len(project_mains)}", failures)

    fixtures = sorted((ROOT / "projects").glob("*/expected.json"))
    if len(fixtures) != EXPECTED_CAPSTONE_FIXTURES:
        fail(
            f"expected {EXPECTED_CAPSTONE_FIXTURES} capstone fixtures, found {len(fixtures)}",
            failures,
        )

    for workflow in ("ci.yml", "quality.yml", "projects.yml"):
        if not (ROOT / ".github" / "workflows" / workflow).is_file():
            fail(f"missing workflow: .github/workflows/{workflow}", failures)

    if failures:
        print("1.1.0 release candidate: FAIL")
        for message in failures:
            print(f"- {message}")
        return 1

    print("1.1.0 release candidate: PASS")
    print(f"- version: {EXPECTED_VERSION}")
    print(f"- projects: {EXPECTED_PROJECTS}")
    print(f"- capstone fixtures: {EXPECTED_CAPSTONE_FIXTURES}")
    print("- public API: stable 1.x snapshot aligned")
    print("- workflows: CI, Quality, Project Matrix present")
    print("- official store: https://ramsandesh.gumroad.com")
    return 0


if __name__ == "__main__":
    sys.exit(main())
