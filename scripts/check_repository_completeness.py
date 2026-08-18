"""Validate the repository's durable structure and documentation baseline.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
GUMROAD = "https://ramsandesh.gumroad.com"

REQUIRED_TOP_LEVEL = {
    ".github",
    "api",
    "assets",
    "docs",
    "examples",
    "projects",
    "scripts",
    "src",
    "tests",
    ".gitignore",
    "CHANGELOG.md",
    "CITATION.cff",
    "CODE_OF_CONDUCT.md",
    "CONTRIBUTING.md",
    "Dockerfile",
    "LICENSE",
    "MAINTAINERS.md",
    "MANIFEST.in",
    "Makefile",
    "NOTICE",
    "README.md",
    "ROADMAP.md",
    "SECURITY.md",
    "SUPPORT.md",
    "pyproject.toml",
    "what_changed.md",
}

REQUIRED_DOCS = {
    "README.md",
    "ACCESSIBILITY.md",
    "API_COMPATIBILITY.md",
    "API_REFERENCE.md",
    "ARCHITECTURE.md",
    "BOOK_COMPANION.md",
    "BRANCH_PROTECTION.md",
    "CHAPTER_COMPANION_INDEX.md",
    "CHECKSUMS.md",
    "CLI.md",
    "COMPATIBILITY_MATRIX.md",
    "CONTAINER.md",
    "DEPENDABOT.md",
    "DEPENDENCIES.md",
    "DEVELOPER_GUIDE.md",
    "DEVELOPMENT.md",
    "EXAMPLE_CONTRACTS.md",
    "FAQ.md",
    "GITHUB_ACTIONS_SECURITY.md",
    "GUMROAD.md",
    "INSTALLATION.md",
    "KNOWN_LIMITATIONS.md",
    "LEARNING_PATH.md",
    "LICENSE_SCOPE.md",
    "MAINTENANCE.md",
    "OBSERVABILITY.md",
    "PORTFOLIO_GUIDE.md",
    "PRIVACY_MODEL.md",
    "PROJECTS.md",
    "PROJECT_AUTHORING_GUIDE.md",
    "PROJECT_CATALOG.md",
    "QUALITY_CHECKLIST.md",
    "RELEASE_ASSETS.md",
    "RELEASE_PROCESS.md",
    "RELEASE_RUNBOOK.md",
    "RELEASE_STATUS.md",
    "REPOSITORY_SETTINGS.md",
    "REPRODUCIBILITY.md",
    "RESPONSIBLE_AI_CHECKLIST.md",
    "SECURITY_MODEL.md",
    "SIGNING.md",
    "SOCIAL_LINK_POLICY.md",
    "STABILITY.md",
    "SUPPLY_CHAIN.md",
    "TESTING_STRATEGY.md",
    "TROUBLESHOOTING.md",
    "TYPING.md",
}

REQUIRED_WORKFLOWS = {
    "ci.yml",
    "docs-links.yml",
    "examples.yml",
    "projects.yml",
    "quality.yml",
    "release-check.yml",
}


def main() -> int:
    failures: list[str] = []

    present_top = {path.name for path in ROOT.iterdir()}
    missing_top = sorted(REQUIRED_TOP_LEVEL - present_top)
    if missing_top:
        failures.append(f"missing top-level paths: {missing_top}")

    docs_dir = ROOT / "docs"
    present_docs = {path.name for path in docs_dir.glob("*.md")} if docs_dir.is_dir() else set()
    missing_docs = sorted(REQUIRED_DOCS - present_docs)
    if missing_docs:
        failures.append(f"missing required documentation: {missing_docs}")

    workflow_dir = ROOT / ".github" / "workflows"
    present_workflows = (
        {path.name for path in workflow_dir.glob("*.yml")} if workflow_dir.is_dir() else set()
    )
    missing_workflows = sorted(REQUIRED_WORKFLOWS - present_workflows)
    if missing_workflows:
        failures.append(f"missing required workflows: {missing_workflows}")

    catalog_path = ROOT / "projects" / "catalog.json"
    if not catalog_path.is_file():
        failures.append("missing projects/catalog.json")
    else:
        try:
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            failures.append(f"invalid projects/catalog.json: {exc}")
        else:
            projects = catalog.get("projects")
            if not isinstance(projects, list) or len(projects) != 25:
                failures.append("projects/catalog.json must contain exactly 25 project records")
            if catalog.get("official_store") != GUMROAD:
                failures.append("projects/catalog.json has an unexpected official_store")

    docs_index = docs_dir / "README.md"
    if docs_index.is_file():
        text = docs_index.read_text(encoding="utf-8")
        for required_name in (
            "USER_GUIDE.md",
            "DEVELOPER_GUIDE.md",
            "PROJECT_AUTHORING_GUIDE.md",
            "PORTFOLIO_GUIDE.md",
            "RELEASE_RUNBOOK.md",
            "KNOWN_LIMITATIONS.md",
        ):
            if required_name not in text:
                failures.append(f"docs/README.md does not reference {required_name}")
        if GUMROAD not in text:
            failures.append("docs/README.md does not contain the canonical Gumroad store")

    for relative in ("README.md", "SUPPORT.md", "SECURITY.md", "docs/README.md"):
        path = ROOT / relative
        if path.is_file() and GUMROAD not in path.read_text(encoding="utf-8"):
            failures.append(f"{relative} does not contain the canonical Gumroad store")

    if failures:
        print("Repository completeness: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Repository completeness: PASS")
    print(f"- top-level contract: {len(REQUIRED_TOP_LEVEL)} paths")
    print(f"- documentation baseline: {len(REQUIRED_DOCS)} documents")
    print(f"- required workflows: {len(REQUIRED_WORKFLOWS)}")
    print("- project catalog: 25 records")
    print(f"- official store: {GUMROAD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
