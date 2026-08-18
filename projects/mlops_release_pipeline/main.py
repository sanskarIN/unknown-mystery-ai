"""MLOps release-pipeline capstone using stable UMAI release primitives."""

from __future__ import annotations

import json

from umai import (
    ArtifactRegistry,
    ArtifactVersion,
    EvidenceBundle,
    ReleaseManifest,
    compare_metrics,
    evaluate_release_gates,
)


def main() -> int:
    registry = ArtifactRegistry()
    candidate = ArtifactVersion("intent-model", "2.1.0", "sha256:demo-model-digest")
    registry.register(candidate)
    approved = registry.approve(candidate.name, candidate.version)

    baseline_metrics = {"accuracy": 0.82, "p95_latency_ms": 130.0}
    candidate_metrics = {"accuracy": 0.86, "p95_latency_ms": 118.0}
    comparison = compare_metrics("2.0.0", "2.1.0", baseline_metrics, candidate_metrics)

    checks = {
        "artifact_approved": approved.approved,
        "accuracy_not_regressed": candidate_metrics["accuracy"] >= baseline_metrics["accuracy"],
        "latency_not_regressed": candidate_metrics["p95_latency_ms"] <= baseline_metrics["p95_latency_ms"],
        "rollback_plan_present": True,
    }
    decision = evaluate_release_gates(checks)
    manifest = ReleaseManifest(
        project="intent-classifier-demo",
        version="2.1.0",
        model_id=approved.identity,
        data_id="synthetic-dataset-v3",
        code_revision="demo-code-revision",
        metrics=candidate_metrics,
        metadata={"environment": "local-demo"},
        created_at="2026-08-18T00:00:00+00:00",
    )
    evidence = EvidenceBundle(
        release_id="intent-classifier-demo@2.1.0",
        source_commit="demo-code-revision",
        checks=checks,
        metrics=candidate_metrics,
        notes=("Synthetic release pipeline demonstration.",),
    )

    payload = {
        "project": "MLOps Release Pipeline",
        "artifact": {"identity": approved.identity, "approved": approved.approved},
        "comparison": [
            {
                "metric": delta.name,
                "baseline": delta.baseline,
                "candidate": delta.candidate,
                "absolute_delta": delta.absolute,
            }
            for delta in comparison.deltas
        ],
        "release": {
            "passed": decision.passed,
            "failed_gates": [item.name for item in decision.failed],
            "manifest_fingerprint": manifest.fingerprint(),
            "evidence_passed": evidence.passed,
        },
        "boundary": "Real production promotion requires organization-specific approval and operational evidence.",
        "store": "https://ramsandesh.gumroad.com",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
