"""Smoke-run every committed companion project and validate JSON output."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS = ROOT / "projects"
EXPECTED_PROJECTS = {
    "agent_router_sandbox",
    "ai_release_readiness_console",
    "artifact_registry_workflow",
    "cost_budget_planner",
    "edge_cloud_planner",
    "evaluation_report_studio",
    "evidence_bundle_builder",
    "experiment_leaderboard",
    "feature_flag_rollout_lab",
    "local_serving_contract",
    "mlops_release_pipeline",
    "model_monitoring_lab",
    "privacy_audit_workbench",
    "production_resilience_lab",
    "prompt_regression_lab",
    "prompt_template_studio",
    "rag_evaluation_capstone",
    "rag_knowledge_explorer",
    "release_comparison_dashboard",
    "release_gate_simulator",
    "release_manifest_builder",
    "resilient_request_pipeline",
    "responsible_ai_review_board",
    "retrieval_ranking_benchmark",
    "text_chunking_lab",
}


def main() -> int:
    discovered = {path.parent.name for path in PROJECTS.glob("*/main.py")}
    if discovered != EXPECTED_PROJECTS:
        missing = sorted(EXPECTED_PROJECTS - discovered)
        unexpected = sorted(discovered - EXPECTED_PROJECTS)
        print(f"project inventory mismatch: missing={missing}, unexpected={unexpected}", file=sys.stderr)
        return 1

    failures: list[str] = []
    for project in sorted(EXPECTED_PROJECTS):
        script = PROJECTS / project / "main.py"
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            failures.append(f"{project}: exit {result.returncode}: {result.stderr.strip()}")
            continue
        try:
            json.loads(result.stdout)
        except json.JSONDecodeError as exc:
            failures.append(f"{project}: output is not valid JSON: {exc}")
            continue
        print(f"PASS {project}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1

    print(f"Validated {len(EXPECTED_PROJECTS)} companion projects.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
