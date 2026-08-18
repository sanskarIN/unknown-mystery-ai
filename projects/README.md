# Companion Projects

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This directory contains complete, dependency-light projects that build on the public `umai` companion package. They use synthetic or local data by default and are designed to be inspectable, runnable, and safe for learning.

## Foundation and evaluation

1. [`evaluation_report_studio`](evaluation_report_studio/) — classification metrics and JSON-friendly reports.
2. [`experiment_leaderboard`](experiment_leaderboard/) — reproducible experiment comparison and selection.
3. [`rag_knowledge_explorer`](rag_knowledge_explorer/) — local lexical RAG/search explorer with scored evidence.
4. [`retrieval_ranking_benchmark`](retrieval_ranking_benchmark/) — precision@k, recall@k, and reciprocal-rank benchmark.
5. [`text_chunking_lab`](text_chunking_lab/) — deterministic normalization and overlapping chunk windows.

## Prompting, agents, and serving

6. [`prompt_template_studio`](prompt_template_studio/) — versioned prompt variables and deterministic rendering.
7. [`prompt_regression_lab`](prompt_regression_lab/) — deterministic prompt/output regression checks.
8. [`agent_router_sandbox`](agent_router_sandbox/) — explicit allowlisted tool routing without external frameworks.
9. [`local_serving_contract`](local_serving_contract/) — in-process request/response contract and validation failures.
10. [`resilient_request_pipeline`](resilient_request_pipeline/) — bounded cache and explicit fallback behavior.

## Governance and releases

11. [`artifact_registry_workflow`](artifact_registry_workflow/) — artifact registration, immutable identity, and explicit approval.
12. [`release_manifest_builder`](release_manifest_builder/) — model/data/code release identity and stable fingerprint.
13. [`evidence_bundle_builder`](evidence_bundle_builder/) — structured source/check/metric release evidence.
14. [`release_comparison_dashboard`](release_comparison_dashboard/) — shared-metric baseline/candidate deltas.
15. [`release_gate_simulator`](release_gate_simulator/) — transparent deployment gate decisions.

## Deployment, operations, privacy, and cost

16. [`feature_flag_rollout_lab`](feature_flag_rollout_lab/) — explicit rollout configuration and safe defaults.
17. [`edge_cloud_planner`](edge_cloud_planner/) — edge/cloud placement filtering and ranking.
18. [`model_monitoring_lab`](model_monitoring_lab/) — deterministic synthetic telemetry and drift indicators.
19. [`privacy_audit_workbench`](privacy_audit_workbench/) — schema validation, redaction, and pseudonymous IDs.
20. [`cost_budget_planner`](cost_budget_planner/) — caller-supplied token pricing and request-budget planning.

## Run projects

From the repository root:

```bash
python -m pip install -e .
python projects/rag_knowledge_explorer/main.py
python scripts/check_projects.py
```

On compatible systems:

```bash
make projects
```

Each project has its own README with goals, commands, extension ideas, and safety/production-boundary notes.

## Design rules

- Standard library + the local `umai` package only.
- Synthetic/local examples by default.
- No provider credentials or network calls required.
- Default execution must produce valid JSON for automated smoke validation.
- Explicit inputs, outputs, assumptions, and failure boundaries.
- Educational utilities are not presented as complete production systems.
- Paid manuscript and commercial publication assets stay outside this Apache-2.0 software repository.

## Official publication

### **https://ramsandesh.gumroad.com**
