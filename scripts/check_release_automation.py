"""Validate the durable stable-release automation contract.

The check is intentionally dependency-free and inspects workflow source text rather than
requiring a YAML parser. It protects the repository from silently reverting to stale,
hard-coded, weakly chained, or PR-only release verification workflows.

Official publication: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from pathlib import Path
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS = ROOT / ".github" / "workflows"
GUMROAD = "https://ramsandesh.gumroad.com"


def require(text: str, needle: str, label: str, failures: list[str]) -> None:
    if needle not in text:
        failures.append(f"{label}: missing required contract text: {needle}")


def read_workflow(name: str, failures: list[str]) -> str:
    path = WORKFLOWS / name
    if not path.is_file():
        failures.append(f"missing .github/workflows/{name}")
        return ""
    return path.read_text(encoding="utf-8")


def require_main_push(text: str, label: str, failures: list[str]) -> None:
    """Require the workflow to be capable of producing exact-SHA evidence on main."""
    require(text, "push:", label, failures)
    require(text, "branches: [main]", label, failures)


def main() -> int:
    failures: list[str] = []

    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    version = str(project["version"])

    publish = read_workflow("publish-stable.yml", failures)
    assets = read_workflow("release-assets.yml", failures)
    ci = read_workflow("ci.yml", failures)
    quality = read_workflow("quality.yml", failures)
    projects = read_workflow("projects.yml", failures)
    docs_links = read_workflow("docs-links.yml", failures)
    release_check = read_workflow("release-check.yml", failures)

    if failures:
        print("Release automation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    publish_requirements = (
        "name: Publish Stable",
        'workflows: ["Quality"]',
        "actions: read",
        "contents: write",
        "Require the verified Quality run to match current main",
        'REQUIRED="CI|Quality|Project Matrix|Documentation Links|Release Check"',
        "Exact-commit verification stack: PASS",
        "gh run list",
        'gh release create "$TAG"',
        '--target "$RELEASE_SHA"',
        'docs/COMPANION_RELEASE_${VERSION}.md',
        'docs/RELEASE_${VERSION_KEY}_CHECKLIST.md',
        GUMROAD,
    )
    for needle in publish_requirements:
        require(publish, needle, "publish-stable.yml", failures)

    asset_requirements = (
        "name: Attach Stable Release Assets",
        'workflows: ["Publish Stable"]',
        "types: [published]",
        "github.event.workflow_run.conclusion == 'success'",
        "contents: write",
        'ref: ${{ steps.release.outputs.tag }}',
        'test "$TAG" = "v$VERSION"',
        "python scripts/check_repository_completeness.py",
        "python scripts/check_release_automation.py",
        "python scripts/check_public_repository_boundary.py",
        "python scripts/check_projects.py",
        "python scripts/check_project_snapshots.py",
        'gh release upload "$TAG" dist/* --clobber',
        GUMROAD,
    )
    for needle in asset_requirements:
        require(assets, needle, "release-assets.yml", failures)

    # Every workflow required by the publication gate must be able to generate evidence for
    # the exact commit after it reaches main. PR-only checks are useful, but they are not a
    # substitute for exact main-SHA verification because merge/update mechanics can differ.
    for label, text in (
        ("ci.yml", ci),
        ("quality.yml", quality),
        ("projects.yml", projects),
        ("docs-links.yml", docs_links),
        ("release-check.yml", release_check),
    ):
        require_main_push(text, label, failures)

    # Stable publication must remain version-aware. Historical hard-coded tags were useful
    # for one release but are unsafe as a permanent workflow contract.
    for workflow_name, text in (("publish-stable.yml", publish), ("release-assets.yml", assets)):
        for stale in ("v1.0.0", "v1.0.1"):
            if stale in text:
                failures.append(f"{workflow_name}: stale hard-coded release reference {stale}")

    if f"v{version}" in publish or f"v{version}" in assets:
        failures.append(
            "stable-release workflows must derive the current tag dynamically instead of "
            f"hard-coding v{version}"
        )

    # The asset workflow intentionally listens to workflow_run in addition to release events.
    # A release created with GITHUB_TOKEN may not recursively trigger another normal workflow
    # from its release event, while workflow_run provides a dependable internal hand-off.
    require(assets, "workflow_run:", "release-assets.yml", failures)

    if failures:
        print("Release automation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Release automation: PASS")
    print(f"- package version: {version}")
    print("- publication waits for the exact-commit verification stack")
    print("- all required verification workflows can run for the exact main SHA")
    print("- stable tag/version is resolved dynamically")
    print("- release assets are chained from stable publication workflow completion")
    print("- release assets are rebuilt from the immutable published tag")
    print("- historical hard-coded tag references are absent")
    print(f"- official store: {GUMROAD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
