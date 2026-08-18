# Agent Router Sandbox

A small deterministic agent-style router with an explicit tool allowlist and no external framework.

## Run

```bash
python -m pip install -e .
python projects/agent_router_sandbox/main.py
python projects/agent_router_sandbox/main.py --message "uppercase this" --text "inspectable routing"
```

## What it demonstrates

- explicit tool registration,
- deterministic keyword routing,
- exact-name invocation,
- visible available-tool lists,
- local execution without network calls or provider credentials.

## Extension ideas

Add argument validation, audit events, explicit authorization policy, dry-run mode, structured error handling, or a human-approval gate for tools with meaningful side effects.

## Boundary

This teaching router is deliberately simple. Real agent systems need strong authorization, input validation, sandboxing, tool-specific permissions, observability, rate limits, and careful handling of external side effects.

Official book store: **https://ramsandesh.gumroad.com**
