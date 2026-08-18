# Production Resilience Lab

> Official book store: **https://ramsandesh.gumroad.com**

An operations-focused capstone combining explicit fallback behavior, a bounded cache, a local serving contract, edge/cloud placement constraints, and caller-supplied cost estimation.

## Run

```bash
python -m pip install -e .
python projects/production_resilience_lab/main.py
```

## Learning goals

- observe provider attempts during recoverable failure;
- cache only explicit local results;
- keep request/model identity visible in serving responses;
- filter placement options using declared latency/privacy constraints;
- treat cost inputs as versioned assumptions rather than hidden constants.

## Production boundary

Real resilience engineering needs measured SLOs, capacity testing, secure failover, dependency health, incident response, rollback, observability, privacy/security controls, and current provider pricing/capabilities.
