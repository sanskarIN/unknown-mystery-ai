# What Changed

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This file records repository work that would otherwise require a long chat summary.

## 2026-08-18 — Final documentation and repository integrity hardening

### Complete documentation layer

- Added `docs/README.md` as the canonical documentation map.
- Added `docs/USER_GUIDE.md` for installation, CLI, tests, examples, project execution, reproducibility, portfolio evidence, troubleshooting, security, and stable-release use.
- Added `docs/DEVELOPER_GUIDE.md` for architecture-aware development, API compatibility, validation commands, build checks, determinism, cross-platform behavior, workflow security, and release discipline.
- Added `docs/PROJECT_AUTHORING_GUIDE.md` defining the required project folder, JSON-output, catalog, snapshot, README, testing, dependency, security, and licensing contracts.
- Added `docs/PORTFOLIO_GUIDE.md` for turning project results into reproducible evidence, technical tradeoff explanations, failure analysis, and interview defense.
- Added `docs/COMPATIBILITY_MATRIX.md` documenting the Python, OS, CLI, API, project, packaging, and runtime compatibility surface.
- Added `docs/KNOWN_LIMITATIONS.md` so educational scope, non-production boundaries, privacy/security limitations, synthetic-data assumptions, and non-goals are explicit.
- Added `docs/RELEASE_RUNBOOK.md` with the exact release-preparation, verification, immutable-tag, asset-review, post-release, and patch-recovery process.

### Repository completeness gate

- Added `scripts/check_repository_completeness.py`.
- The checker validates required top-level repository paths, the durable documentation baseline, required workflows, the 25-record project catalog, documentation discoverability, and canonical Gumroad links in key files.
- Added `make repository-check` for local use.
- Integrated repository completeness as the first substantive Quality-workflow validation so structural omissions fail before deeper package/build checks.

### Root documentation and verification improvements

- Reworked the root `README.md` into a concise repository hub covering quick start, CLI, local validation commands, all 25 projects, the machine-readable catalog, complete documentation entry point, quality gates, release state, compatibility/limitation notes, licensing boundaries, support, security, and durable project links.
- Expanded `docs/TESTING_STRATEGY.md` into layered repository, API, example, catalog, project, snapshot, cross-platform, documentation/policy, package/build, and release-candidate validation.
- Expanded `docs/RELEASE_1_1_0_CHECKLIST.md` with complete documentation, repository integrity, exact-release-commit, and post-release verification requirements.
- Updated `CHANGELOG.md` so the 1.1.0 release notes reflect the final documentation and integrity work.

### Compatibility and public/commercial boundary

- No incompatible `umai` 1.x public API change was introduced by this final hardening work.
- No mandatory runtime dependency was added.
- The 25 project IDs and five capstone snapshot contracts remain intact.
- Long-lived files continue to prefer GitHub, the repository, Gumroad, and email over change-prone X/Twitter profile links.
- Paid eBook/manuscript/cover/certificate/publication assets remain outside the Apache-2.0 public software repository.

### Final validation policy

The repository is considered ready for the 1.1.0 stable tag only after the **exact final intended release commit** passes repository completeness, Quality, CI, Project Matrix, documentation/release checks when triggered, package build/distribution checks, and commercial-publication boundary review.

## 2026-08-18 — Project catalog, CI queue hardening, and 1.1.0 release preparation

### Machine-readable project catalog

- Added `projects/catalog.json` for all 25 runnable projects.
- Catalog records project ID, human title, category, learning level, entry point, and capstone snapshot status.
- Added `scripts/check_project_catalog.py` to validate catalog schema, unique IDs, allowed categories/levels, entry points, README presence, snapshot declarations, canonical Gumroad links, and parity with discovered project directories.
- Added `tests/test_project_catalog.py` for independent catalog invariants.
- Added `docs/PROJECT_CATALOG.md` describing the catalog contract.
- Added `make project-catalog`.

### GitHub Actions queue hardening

- Added workflow concurrency groups with `cancel-in-progress: true` to high-frequency CI/PR workflows.
- Added job timeout limits so a stalled run cannot consume a runner indefinitely.
- Hardened:
  - `CI`
  - `Quality`
  - `Project Matrix`
  - `Documentation Links`
  - `Example Smoke Tests`
  - `Release Check`
- Left stable tag/release-asset workflows outside this automatic cancellation policy so publishing jobs are not casually interrupted.

### 1.1.0 release candidate

- Promoted package, package `__version__`, stable API snapshot version, citation metadata, README badge, and changelog to **1.1.0** in one coordinated release metadata commit.
- Added `docs/COMPANION_RELEASE_1.1.0.md`.
- Added `docs/RELEASE_1_1_0_CHECKLIST.md`.
- Added `docs/VERSIONING_1_1_0.md`.
- Added `scripts/check_release_candidate.py` and `make release-check`.
- Updated `docs/RELEASE_STATUS.md` to keep **v1.0.1** as the currently published stable release until 1.1.0 is fully verified and tagged.
- Created release-candidate branch `release/1.1.0-rc`.
- Opened PR #6 specifically to run the complete pull-request verification stack before tagging.
- Opened Issue #5 to track release verification, tag, release notes, and software release assets.

### Release verification policy

The 1.1.0 release is not considered published stable until CI, Quality, and Project Matrix checks succeed on the intended release candidate. Paid eBook/manuscript/publication assets remain excluded from the Apache-2.0 software release.

## 2026-08-18 — Integrated capstones and project verification

### Five new integrated capstone projects

21. `projects/ai_release_readiness_console/`
   - structured input validation
   - privacy-aware contact handling
   - classification evaluation
   - explicit release gates
   - machine-readable evidence bundle

22. `projects/rag_evaluation_capstone/`
   - local lexical retrieval
   - explicit relevance judgments
   - precision@k, recall@k, and reciprocal rank
   - output-regression evidence

23. `projects/mlops_release_pipeline/`
   - artifact registration and approval
   - baseline/candidate metric comparison
   - PASS/BLOCK release gates
   - deterministic release manifest
   - structured release evidence

24. `projects/responsible_ai_review_board/`
   - intended-use and oversight documentation
   - structured review validation
   - privacy-aware display
   - governance review gates
   - explicit educational/legal boundary

25. `projects/production_resilience_lab/`
   - recoverable provider fallback
   - bounded local cache
   - local serving request/response identity
   - edge/cloud placement constraints
   - caller-supplied cost assumptions

### Snapshot fixtures and tests

- Added `expected.json` subset fixtures for all five new capstones.
- Added `scripts/check_project_snapshots.py`.
- Snapshot validation checks durable project facts without freezing incidental output fields.
- Expanded `scripts/check_projects.py` from twenty to twenty-five required projects.
- Every project must still execute successfully and emit valid JSON.

### Cross-platform automation

- Added `.github/workflows/projects.yml`.
- Project validation now runs on Linux, Windows, and macOS.
- The matrix uses multiple supported Python versions.
- The main Quality workflow also runs capstone snapshot validation.
- Added `make project-snapshots` alongside `make projects`.

### Documentation

- Expanded `projects/README.md` to twenty-five projects and a dedicated capstone section.
- Expanded `docs/PROJECTS.md` with a five-stage learning path and snapshot-contract explanation.
- Expanded the root `README.md` with the Project Matrix badge, capstones, verification commands, and durable social-link policy navigation.
- Updated `CHANGELOG.md` under Unreleased.

### Compatibility and safety

- No incompatible change was made to the stable `umai` 1.x public API.
- New capstones compose existing stable helpers rather than widening the public symbol surface.
- Projects remain local/synthetic by default and require no provider credentials or network calls.
- Paid manuscript and commercial publishing assets remain outside the Apache-2.0 repository.

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

Continue with project-specific unit tests where they add value, additional integrated portfolio capstones, stronger workflow evidence, and backward-compatible 1.x maintenance. Repository administration settings tracked separately still require GitHub/account configuration rather than normal commits.
