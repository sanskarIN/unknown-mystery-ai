"""Feature-flag rollout configuration exercise."""

from __future__ import annotations

import argparse

from umai import FeatureFlags, to_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate explicit rollout feature flags.")
    parser.add_argument("--new-retriever", default="enabled")
    parser.add_argument("--shadow-mode", default="true")
    parser.add_argument("--edge-fallback", default="yes")
    args = parser.parse_args()

    flags = FeatureFlags(
        {
            "new_retriever": args.new_retriever,
            "shadow_mode": args.shadow_mode,
            "edge_fallback": args.edge_fallback,
        }
    )
    payload = {
        "new_retriever": flags.enabled("new_retriever"),
        "shadow_mode": flags.enabled("shadow_mode"),
        "edge_fallback": flags.enabled("edge_fallback"),
        "unconfigured_debug_mode": flags.enabled("debug_mode", default=False),
    }
    print(to_json(payload))


if __name__ == "__main__":
    main()
