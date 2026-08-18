"""Structured release-evidence bundle builder."""

from __future__ import annotations

from umai import EvidenceBundle


def main() -> None:
    bundle = EvidenceBundle(
        release_id="candidate-2026-08",
        source_commit="synthetic-demo-commit",
        checks={
            "unit_tests": True,
            "evaluation": True,
            "privacy_review": True,
            "rollback_plan": True,
        },
        metrics={"accuracy": 0.889, "latency_ms": 39.5},
        notes=(
            "Synthetic educational evidence only.",
            "Production evidence should preserve real provenance and reviewer ownership.",
        ),
    )
    print(bundle.to_json())


if __name__ == "__main__":
    main()
