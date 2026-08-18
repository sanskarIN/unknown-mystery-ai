"""Artifact registration and explicit approval workflow demo."""

from __future__ import annotations

from umai import ArtifactRegistry, ArtifactVersion, to_json


def main() -> None:
    registry = ArtifactRegistry()
    registry.register(ArtifactVersion("classifier", "1.0.0", "sha256:aaa111"))
    registry.register(ArtifactVersion("classifier", "1.1.0", "sha256:bbb222"))
    registry.register(ArtifactVersion("retriever", "2.0.0", "sha256:ccc333"))

    approved = registry.approve("classifier", "1.1.0")
    print(
        to_json(
            {
                "approved_now": approved.identity,
                "classifier_approved_versions": [
                    {"identity": item.identity, "approved": item.approved}
                    for item in registry.approved_versions("classifier")
                ],
                "retriever_approved_versions": [
                    item.identity for item in registry.approved_versions("retriever")
                ],
            }
        )
    )


if __name__ == "__main__":
    main()
