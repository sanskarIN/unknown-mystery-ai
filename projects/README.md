# Companion Projects

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This directory contains complete, dependency-light projects that build on the public `umai` companion package. They use synthetic or local data by default and are designed to be inspectable, runnable, and safe for learning.

## Projects

1. [`rag_knowledge_explorer`](rag_knowledge_explorer/) — local lexical RAG/search explorer with scored evidence.
2. [`prompt_regression_lab`](prompt_regression_lab/) — deterministic prompt/output regression checks.
3. [`release_gate_simulator`](release_gate_simulator/) — transparent deployment gate decisions.
4. [`edge_cloud_planner`](edge_cloud_planner/) — edge/cloud placement filtering and ranking.
5. [`privacy_audit_workbench`](privacy_audit_workbench/) — schema validation, redaction, and pseudonymous IDs.
6. [`experiment_leaderboard`](experiment_leaderboard/) — reproducible experiment comparison and selection.
7. [`model_monitoring_lab`](model_monitoring_lab/) — deterministic synthetic telemetry and drift indicators.
8. [`agent_router_sandbox`](agent_router_sandbox/) — explicit allowlisted tool routing without external frameworks.
9. [`evaluation_report_studio`](evaluation_report_studio/) — classification metrics and JSON-friendly reports.
10. [`cost_budget_planner`](cost_budget_planner/) — caller-supplied token pricing and request-budget planning.

## Run a project

From the repository root:

```bash
python -m pip install -e .
python projects/rag_knowledge_explorer/main.py
```

Each project has its own README with goals, commands, extension ideas, and safety/production-boundary notes.

## Design rules

- Standard library + the local `umai` package only.
- Synthetic/local examples by default.
- No provider credentials or network calls required.
- Explicit inputs, outputs, assumptions, and failure boundaries.
- Educational utilities are not presented as complete production systems.
- Paid manuscript and commercial publication assets stay outside this Apache-2.0 software repository.

## Official publication

### **https://ramsandesh.gumroad.com**
