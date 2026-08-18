"""Validate the durable stable-release automation contract.

The check is intentionally dependency-free and inspects workflow source text rather than
requiring a YAML parser. It protects the repository from silently reverting to stale,
hard-coded, or weakly chained historical release workflows.

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


def main() -> int:
    failures: list[str] = []

    project = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))["project"]
    version = str(project["version"])

    publish_path = WORKFLOWS / "publish-stable.yml"
    assets_path = WORKFLOWS / "release-assets.yml"
    if not publish_path.is_file():
        failures.append("missing .github/workflows/publish-stable.yml")
    if not assets_path.is_file():
        failures.append("missing .github/workflows/release-assets.yml")

    if failures:
        print("Release automation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    publish = publish_path.read_text(encoding="utf-8")
    assets = assets_path.read_text(encoding="utf-8")

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
    require(
        assets,
        "workflow_run:",
        "release-assets.yml",
        failures,
    )

    if failures:
        print("Release automation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Release automation: PASS")
    print(f"- package version: {version}")
    print("- publication waits for the exact-commit verification stack")
    print("- stable tag/version is resolved dynamically")
    print("- release assets are chained from stable publication workflow completion")
    print("- release assets are rebuilt from the immutable published tag")
    print("- historical hard-coded tag references are absent")
    print(f"- official store: {GUMROAD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
