"""Privacy-aware technical telemetry example.

Book store: https://ramsandesh.gumroad.com
"""

from umai.observability import MetricEvent, mean_metric


def main() -> None:
    events = [
        MetricEvent("release-2026-08", "latency_ms", 34.0, {"device": "desktop"}),
        MetricEvent("release-2026-08", "latency_ms", 42.0, {"device": "desktop"}),
        MetricEvent("release-2026-08", "latency_ms", 38.0, {"device": "desktop"}),
    ]

    print(f"Mean latency: {mean_metric(events, 'latency_ms'):.1f} ms")
    print("This demo records technical metrics, not raw user prompts or private payloads.")
    print("Book store: https://ramsandesh.gumroad.com")


if __name__ == "__main__":
    main()
