"""Validate the machine-readable companion project catalog."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "projects" / "catalog.json"
EXPECTED_STORE = "https://ramsandesh.gumroad.com"
EXPECTED_COUNT = 25
EXPECTED_CAPSTONES = 5
ALLOWED_LEVELS = {"foundation", "intermediate", "advanced", "capstone"}
ALLOWED_CATEGORIES = {
    "foundation-evaluation",
    "prompting-agents-serving",
    "governance-release",
    "operations-privacy-cost",
    "integrated-capstone",
}


def main() -> int:
    failures: list[str] = []
    data = json.loads(CATALOG.read_text(encoding="utf-8"))

    if data.get("schema_version") != 1:
        failures.append("catalog schema_version must be 1")
    if data.get("official_store") != EXPECTED_STORE:
        failures.append("catalog official_store is not canonical Gumroad URL")

    projects = data.get("projects")
    if not isinstance(projects, list):
        failures.append("catalog projects must be a list")
        projects = []
    if len(projects) != EXPECTED_COUNT:
        failures.append(f"expected {EXPECTED_COUNT} catalog projects, found {len(projects)}")

    ids: list[str] = []
    snapshot_count = 0
    for index, item in enumerate(projects, start=1):
        if not isinstance(item, dict):
            failures.append(f"project #{index} must be an object")
            continue
        project_id = item.get("id")
        if not isinstance(project_id, str) or not project_id:
            failures.append(f"project #{index} has invalid id")
            continue
        ids.append(project_id)

        if item.get("level") not in ALLOWED_LEVELS:
            failures.append(f"{project_id}: invalid level {item.get('level')!r}")
        if item.get("category") not in ALLOWED_CATEGORIES:
            failures.append(f"{project_id}: invalid category {item.get('category')!r}")
        if not isinstance(item.get("title"), str) or not item["title"].strip():
            failures.append(f"{project_id}: title must be non-empty")

        expected_entrypoint = f"projects/{project_id}/main.py"
        if item.get("entrypoint") != expected_entrypoint:
            failures.append(f"{project_id}: entrypoint must be {expected_entrypoint}")
        if not (ROOT / expected_entrypoint).is_file():
            failures.append(f"{project_id}: missing main.py")
        if not (ROOT / "projects" / project_id / "README.md").is_file():
            failures.append(f"{project_id}: missing README.md")

        snapshot = item.get("snapshot")
        if not isinstance(snapshot, bool):
            failures.append(f"{project_id}: snapshot must be boolean")
        expected_fixture = ROOT / "projects" / project_id / "expected.json"
        if snapshot:
            snapshot_count += 1
            if not expected_fixture.is_file():
                failures.append(f"{project_id}: snapshot=true but expected.json is missing")
        elif expected_fixture.exists():
            failures.append(f"{project_id}: expected.json exists but snapshot=false")

        readme = ROOT / "projects" / project_id / "README.md"
        if readme.is_file() and EXPECTED_STORE not in readme.read_text(encoding="utf-8"):
            failures.append(f"{project_id}: README does not contain canonical Gumroad store")

    if len(ids) != len(set(ids)):
        failures.append("catalog project ids must be unique")

    discovered = {path.parent.name for path in (ROOT / "projects").glob("*/main.py")}
    catalog_ids = set(ids)
    if catalog_ids != discovered:
        failures.append(
            f"catalog/runtime inventory mismatch: missing={sorted(discovered - catalog_ids)}, "
            f"unexpected={sorted(catalog_ids - discovered)}"
        )

    if snapshot_count != EXPECTED_CAPSTONES:
        failures.append(f"expected {EXPECTED_CAPSTONES} snapshot projects, found {snapshot_count}")

    if failures:
        print("Project catalog: FAIL", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("Project catalog: PASS")
    print(f"- projects: {len(projects)}")
    print(f"- snapshot capstones: {snapshot_count}")
    print(f"- categories: {len(ALLOWED_CATEGORIES)}")
    print(f"- official store: {EXPECTED_STORE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
