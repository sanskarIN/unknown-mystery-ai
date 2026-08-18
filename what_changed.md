# What Changed

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This file records repository work that would otherwise require a long chat summary.

## 2026-08-18 — Companion project expansion

### Added ten runnable projects

1. `projects/rag_knowledge_explorer/`
   - local lexical retrieval over synthetic knowledge documents
   - scored evidence and metadata
   - JSON output and CLI query controls

2. `projects/prompt_regression_lab/`
   - required/forbidden output expectations
   - deterministic regression evidence
   - aggregate pass counts and detailed case output

3. `projects/release_gate_simulator/`
   - explicit PASS/BLOCK release gates
   - failed-gate reporting
   - optional strict CI-style exit behavior

4. `projects/edge_cloud_planner/`
   - latency/privacy/offline filtering
   - transparent synthetic placement ranking
   - edge/cloud architecture exercises

5. `projects/privacy_audit_workbench/`
   - structured record validation
   - common identifier redaction
   - deterministic pseudonymous identifiers
   - synthetic-only demonstration record

6. `projects/experiment_leaderboard/`
   - reproducible experiment records
   - stable fingerprints
   - accuracy and latency winners
   - multi-objective comparison reminder

7. `projects/model_monitoring_lab/`
   - deterministic synthetic telemetry
   - reference/current windows
   - absolute and standardized mean shift
   - no universal drift-threshold claim

8. `projects/agent_router_sandbox/`
   - explicit local tool allowlist
   - deterministic keyword routing
   - exact-name invocation
   - no provider credentials or network calls

9. `projects/evaluation_report_studio/`
   - synthetic expected/predicted labels
   - accuracy, precision, recall, F1, and support
   - JSON-friendly report evidence

10. `projects/cost_budget_planner/`
    - caller-supplied token pricing
    - per-request cost estimate
    - request capacity under a declared budget
    - explicit warning that values are not live vendor pricing

### Automation and quality

- Added `scripts/check_projects.py`.
- The checker requires the expected ten-project inventory.
- Every default project execution must exit successfully.
- Every default project output must be valid JSON.
- Integrated the project smoke checker into `.github/workflows/quality.yml`.
- Added `make projects`.

### Documentation

- Added `projects/README.md` project index.
- Reworked `docs/PROJECTS.md` into an implemented-project learning guide.
- Expanded root `README.md` with projects, commands, repository map, navigation, and quality gates.
- Updated `CHANGELOG.md` under Unreleased.

### Compatibility

- No incompatible change was made to the documented stable `umai` 1.x public API.
- Projects consume existing stable helpers instead of widening the stable public symbol surface.
- Commercial eBook/manuscript assets remain outside the Apache-2.0 software repository.

### Next repository work

Continue with additional advanced projects, project-specific fixtures/tests where useful, cross-platform project smoke validation, and backward-compatible 1.x maintenance. Repository administration settings tracked separately still require GitHub/account configuration rather than normal commits.
