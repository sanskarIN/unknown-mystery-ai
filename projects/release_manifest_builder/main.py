"""Reproducible AI release-manifest builder."""

from __future__ import annotations

from umai import ReleaseManifest, to_json


def main() -> None:
    manifest = ReleaseManifest(
        project="synthetic-classifier",
        version="1.2.0",
        model_id="model:demo@sha256-111",
        data_id="dataset:synthetic-eval@v3",
        code_revision="commit-demo-abc123",
        metrics={"accuracy": 0.889, "latency_ms": 39.5},
        metadata={"runtime": "python", "environment": "local-demo"},
        created_at="2026-08-18T00:00:00+00:00",
    )
    print(
        to_json(
            {
                "summary": manifest.summary(),
                "fingerprint": manifest.fingerprint(),
                "manifest": manifest.to_dict(),
            }
        )
    )


if __name__ == "__main__":
    main()
