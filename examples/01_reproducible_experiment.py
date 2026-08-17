"""Reproducibility example for The Unknown Mystery of the AI companion repo.

Book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

import random

from umai.reproducibility import fingerprint_json, seed_everything


def main() -> None:
    seed = seed_everything(42)
    sample = [round(random.random(), 6) for _ in range(5)]
    experiment = {
        "seed": seed,
        "sample": sample,
        "note": "A seed improves repeatability but does not guarantee universal determinism.",
    }

    print("Experiment:", experiment)
    print("Fingerprint:", fingerprint_json(experiment))
    print("Book store: https://ramsandesh.gumroad.com")


if __name__ == "__main__":
    main()
