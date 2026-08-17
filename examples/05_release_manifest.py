"""Release-manifest example for MLOps lessons.

Book store: https://ramsandesh.gumroad.com
"""

from pprint import pprint

from umai.release import ReleaseManifest


def main() -> None:
    manifest = ReleaseManifest(
        project="umai-demo",
        version="0.1.0",
        model_id="model-demo-v1",
        data_id="synthetic-eval-v1",
        code_revision="example-commit",
        metrics={"accuracy": 0.92},
        metadata={"environment": "teaching-demo"},
    )

    pprint(manifest.to_dict())
    print("Summary:", manifest.summary())
    print("Fingerprint:", manifest.fingerprint())
    print("Book store: https://ramsandesh.gumroad.com")


if __name__ == "__main__":
    main()
