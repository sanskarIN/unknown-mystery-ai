"""Production resilience capstone combining serving, fallback, cache, and placement."""

from __future__ import annotations

import json

from umai import (
    BoundedCache,
    InferenceRequest,
    LocalEndpoint,
    PlacementOption,
    TokenPricing,
    eligible_placements,
    estimate_token_cost,
    run_fallback_chain,
)


def main() -> int:
    cache: BoundedCache[str, dict[str, str]] = BoundedCache(max_items=2)

    def primary() -> dict[str, str]:
        raise RuntimeError("synthetic primary outage")

    def fallback() -> dict[str, str]:
        return {"provider": "local-fallback", "status": "ok"}

    recovered = run_fallback_chain(
        [("primary", primary), ("fallback", fallback)],
        recoverable=(RuntimeError,),
    )
    cache.set("health", recovered.value)

    endpoint = LocalEndpoint(lambda payload: {"echo": str(payload.get("message", ""))})
    response = endpoint.handle(
        InferenceRequest(
            request_id="resilience-demo-001",
            model_version="demo-model-v1",
            payload={"message": "hello"},
        )
    )

    placements = [
        PlacementOption("device", latency_ms=25, cost_units=1.0, privacy_score=0.95, offline_capable=True),
        PlacementOption("regional-cloud", latency_ms=90, cost_units=0.6, privacy_score=0.75, offline_capable=False),
        PlacementOption("remote-cloud", latency_ms=160, cost_units=0.4, privacy_score=0.65, offline_capable=False),
    ]
    eligible = eligible_placements(
        placements,
        max_latency_ms=100,
        min_privacy_score=0.70,
        require_offline=False,
    )

    pricing = TokenPricing(input_per_million=2.0, output_per_million=4.0)
    estimated_cost = estimate_token_cost(input_tokens=1500, output_tokens=500, pricing=pricing)

    payload = {
        "project": "Production Resilience Lab",
        "fallback": {
            "selected_provider": recovered.provider,
            "attempts": list(recovered.attempts),
            "cached_health": cache.get("health"),
        },
        "serving": {
            "ok": response.ok,
            "request_id": response.request_id,
            "model_version": response.model_version,
            "output": dict(response.output),
        },
        "eligible_placements": [item.name for item in eligible],
        "estimated_demo_request_cost": estimated_cost,
        "boundary": "Synthetic failure and cost values are teaching inputs, not live production telemetry or pricing.",
        "store": "https://ramsandesh.gumroad.com",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
