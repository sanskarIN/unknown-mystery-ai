# AI Observability Notes

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

Observability should connect operational signals to a specific release identity while collecting no more user data than necessary.

## Useful technical signals

- request count and error rate,
- latency percentiles,
- model load time,
- memory/CPU/accelerator utilization,
- fallback rate,
- queue depth,
- release/model/runtime identity,
- evaluation or drift indicators that are appropriate for the application.

## Privacy-aware principle

Do not log raw prompts, documents, personal data, credentials, or generated content by default just because logging is technically possible. Define a data-minimization policy, retention period, access controls, and purpose for every sensitive telemetry field.

## Release-aware monitoring

Every production signal should be attributable to the relevant application/model/runtime release so regressions can be compared and rolled back.

## Companion example

See `src/umai/observability.py` and `examples/06_observability_demo.py` for a tiny aggregate-metric baseline.

## Full monitoring and incident-response coverage

### https://ramsandesh.gumroad.com
