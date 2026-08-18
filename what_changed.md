# What Changed

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This file records repository work that would otherwise require a long chat summary.

## 2026-08-18 — Stable social link policy

- Searched the repository for `x.com` and `twitter.com` profile links; no durable X/Twitter profile link was present.
- Added `docs/SOCIAL_LINK_POLICY.md` to document the decision to avoid change-prone social profile URLs in long-lived book, release, and repository assets.
- Added `scripts/check_unstable_social_links.py` so future changes fail quality checks if an X/Twitter URL is introduced outside the policy/checker files.
- Integrated the social-link check into `.github/workflows/quality.yml`.
- Permanent destinations remain GitHub, the project repository, Gumroad, and the maintainer contact email.

## 2026-08-18 — Companion project expansion

### Added twenty runnable projects

#### Foundation and evaluation

1. `projects/evaluation_report_studio/`
   - synthetic expected/predicted labels
   - accuracy, precision, recall, F1, and support
   - JSON-friendly report evidence

2. `projects/experiment_leaderboard/`
   - reproducible experiment records
   - stable fingerprints
   - separate accuracy and latency winners

3. `projects/rag_knowledge_explorer/`
   - local lexical retrieval over synthetic knowledge documents
   - scored evidence and metadata
   - JSON output and CLI query controls

4. `projects/retrieval_ranking_benchmark/`
   - synthetic relevance judgments
   - precision@k, recall@k, and reciprocal rank

5. `projects/text_chunking_lab/`
   - deterministic whitespace normalization
   - explicit chunk size and overlap
   - ordered JSON chunk evidence

#### Prompting, agents, and serving

6. `projects/prompt_template_studio/`
   - versioned prompt identity
   - explicit variables and deterministic rendering

7. `projects/prompt_regression_lab/`
   - required/forbidden output expectations
   - deterministic regression evidence
   - aggregate pass counts and detailed case output

8. `projects/agent_router_sandbox/`
   - explicit local tool allowlist
   - deterministic keyword routing
   - exact-name invocation
   - no provider credentials or network calls

9. `projects/local_serving_contract/`
   - explicit request/model identity
   - successful and invalid-request response contracts

10. `projects/resilient_request_pipeline/`
    - bounded local cache
    - explicit recoverable fallback chain
    - visible provider attempts and cache reuse

#### Governance and release engineering

11. `projects/artifact_registry_workflow/`
    - immutable artifact version identity
    - separate registration and approval

12. `projects/release_manifest_builder/`
    - model/data/code release identity
    - deterministic demonstration timestamp
    - stable manifest fingerprint

13. `projects/evidence_bundle_builder/`
    - release/source provenance
    - named checks, metrics, and notes

14. `projects/release_comparison_dashboard/`
    - shared baseline/candidate metrics
    - explicit absolute deltas
    - metric-direction warning

15. `projects/release_gate_simulator/`
    - explicit PASS/BLOCK release gates
    - failed-gate reporting
    - optional strict CI-style exit behavior

#### Deployment, operations, privacy, and cost

16. `projects/feature_flag_rollout_lab/`
    - explicit boolean rollout flags
    - safe default handling

17. `projects/edge_cloud_planner/`
    - latency/privacy/offline filtering
    - transparent synthetic placement ranking
    - edge/cloud architecture exercises

18. `projects/model_monitoring_lab/`
    - deterministic synthetic telemetry
    - reference/current windows
    - absolute and standardized mean shift
    - no universal drift-threshold claim

19. `projects/privacy_audit_workbench/`
    - structured record validation
    - common identifier redaction
    - deterministic pseudonymous identifiers
    - synthetic-only demonstration record

20. `projects/cost_budget_planner/`
    - caller-supplied token pricing
    - per-request cost estimate
    - request capacity under a declared budget
    - explicit warning that values are not live vendor pricing

### Automation and quality

- Added `scripts/check_projects.py`.
- Expanded the required inventory from ten to twenty projects.
- Every default project execution must exit successfully.
- Every default project output must be valid JSON.
- Integrated project smoke validation into `.github/workflows/quality.yml`.
- Added `make projects`.

### Documentation

- Expanded `projects/README.md` into a twenty-project categorized index.
- Reworked `docs/PROJECTS.md` into a four-stage implemented-project learning guide.
- Expanded root `README.md` with twenty projects, commands, repository map, navigation, and quality gates.
- Updated `CHANGELOG.md` under Unreleased.

### Compatibility

- No incompatible change was made to the documented stable `umai` 1.x public API.
- Projects consume existing stable helpers instead of widening the stable public symbol surface.
- Commercial eBook/manuscript assets remain outside the Apache-2.0 software repository.

### Commit strategy

Project source, project documentation, automation, indexes, and repository documentation were committed in small focused changes rather than one oversized commit so history remains easy to inspect and revert.

### Next repository work

Continue with project-specific tests/fixtures where useful, cross-platform project smoke validation, additional integrated capstone projects, and backward-compatible 1.x maintenance. Repository administration settings tracked separately still require GitHub/account configuration rather than normal commits.
