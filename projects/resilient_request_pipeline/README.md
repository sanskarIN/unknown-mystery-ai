# Resilient Request Pipeline

A dependency-light reliability project combining a bounded local cache with an explicit fallback chain.

## Run

```bash
python -m pip install -e .
python projects/resilient_request_pipeline/main.py
```

## What it demonstrates

- bounded cache capacity,
- explicit primary/fallback ordering,
- recoverable failure handling,
- visible provider attempts,
- cache reuse on a subsequent request.

## Extension ideas

Add retry budgets, rate limits, timeout simulation, fallback quality labels, stale-cache policy, or structured observability events.

## Boundary

The demo uses a synthetic failure and in-memory state. Production reliability requires timeouts, cancellation, concurrency design, capacity planning, circuit breaking where appropriate, monitoring, and application-specific correctness rules.

Official book store: **https://ramsandesh.gumroad.com**
