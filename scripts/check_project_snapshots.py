"""Validate selected stable JSON expectations for integrated companion projects."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"


def assert_subset(expected: Any, actual: Any, path: str = "$") -> list[str]:
    failures: list[str] = []
    if isinstance(expected, dict):
        if not isinstance(actual, dict):
            return [f"{path}: expected object, got {type(actual).__name__}"]
        for key, value in expected.items():
            if key not in actual:
                failures.append(f"{path}.{key}: missing key")
                continue
            failures.extend(assert_subset(value, actual[key], f"{path}.{key}"))
        return failures
    if isinstance(expected, list):
        if not isinstance(actual, list):
            return [f"{path}: expected list, got {type(actual).__name__}"]
        if expected != actual:
            failures.append(f"{path}: expected {expected!r}, got {actual!r}")
        return failures
    if expected != actual:
        failures.append(f"{path}: expected {expected!r}, got {actual!r}")
    return failures


def main() -> int:
    fixtures = sorted(PROJECTS.glob("*/expected.json"))
    if not fixtures:
        print("No project snapshots found.", file=sys.stderr)
        return 1

    failures: list[str] = []
    for fixture in fixtures:
        project_dir = fixture.parent
        script = project_dir / "main.py"
        if not script.exists():
            failures.append(f"{project_dir.name}: missing main.py")
            continue

        expected = json.loads(fixture.read_text(encoding="utf-8"))
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            failures.append(f"{project_dir.name}: exit {result.returncode}: {result.stderr.strip()}")
            continue
        try:
            actual = json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            failures.append(f"{project_dir.name}: invalid JSON output: {exc}")
            continue

        mismatches = assert_subset(expected, actual)
        if mismatches:
            failures.extend(f"{project_dir.name}: {message}" for message in mismatches)
        else:
            print(f"PASS snapshot {project_dir.name}")

    if failures:
        print("Project snapshot validation: FAIL", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Validated {len(fixtures)} project snapshot fixtures.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
