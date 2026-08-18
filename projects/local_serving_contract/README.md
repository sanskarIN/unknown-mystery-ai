# Local Serving Contract

A local in-process serving project that makes request identity, model version, output, and validation failures explicit.

## Run

```bash
python -m pip install -e .
python projects/local_serving_contract/main.py
```

## What it demonstrates

- explicit request IDs,
- model-version identity,
- typed payload expectations,
- successful response contracts,
- structured invalid-request responses.

## Extension ideas

Add latency timing, schema validation, request budgets, release manifests, trace identifiers, or a minimal local HTTP adapter while preserving the same request/response semantics.

## Boundary

`LocalEndpoint` is an in-process teaching abstraction. Network services need authentication, authorization, transport security, concurrency controls, timeouts, resource limits, and operational monitoring.

Official book store: **https://ramsandesh.gumroad.com**
