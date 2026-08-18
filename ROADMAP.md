# Repository Roadmap

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

The companion repository grows through small, reviewable additions rather than copying the commercial manuscript.

## v0.1 — Foundation

- [x] Repository documentation
- [x] Apache-2.0 source license and book rights notice
- [x] Reproducibility utilities
- [x] Evaluation helpers
- [x] Minimal retrieval/RAG baseline
- [x] Transparent agent-tool routing baseline
- [x] Release manifest utility
- [x] Unit tests
- [x] CI workflow

## v0.2 — Engineering companion

- [x] Model-card and dataset-card templates
- [x] Responsible-AI review checklist
- [x] Privacy-aware observability example
- [x] Text chunking and prompt versioning
- [x] Drift and cost-budget examples
- [x] Privacy redaction and structured validation
- [x] Experiment and artifact governance helpers
- [x] Bounded cache, retry, and rate-limit helpers
- [x] Expanded tests and runnable examples
- [x] Architecture, API, release, troubleshooting, and FAQ documentation
- [x] Dependabot, CODEOWNERS, funding, and release-check automation

## v0.3 — Deployment companion

- [x] Local serving contract reference
- [x] Non-root container example
- [x] Release-gate policy example
- [x] Synthetic monitoring dashboard data generator
- [x] Edge/cloud release comparison constraints
- [x] Configuration and feature-flag reference pattern

## v0.4 — Evaluation expansion

- [x] Retrieval ranking metrics baseline
- [x] Prompt regression fixtures
- [x] Release comparison report primitives
- [x] Reliability fallback simulation
- [x] Examples and unit tests for expanded evaluation utilities

## v0.5 — Quality and packaging

- [x] Public API compatibility checks
- [x] Cross-platform example smoke workflow
- [x] Documentation link validation
- [x] Package metadata/version validation
- [x] Release artifact checksum manifest generator
- [x] Maintainer quality checklist
- [x] Comprehensive quality workflow and build evidence

## v0.6 — Stable API preparation

- [x] Formal public API compatibility policy
- [x] Deprecation helper and policy example
- [x] Structured JSON export for experiment/release evidence
- [x] CLI-friendly project reporting
- [x] Public API snapshot checker
- [x] Stable release candidate checklist and workflow

## v1.0.0 — Mature companion release

- [x] Final stable public API snapshot
- [x] Versioned example contracts
- [x] Stable architecture and support guarantees
- [x] 1.0 maintainer release checklist
- [x] Package and citation metadata promoted to 1.0.0
- [x] `v1.0.0` Git tag and GitHub release created after successful final Quality verification

## v1.0.1 — Packaging, supply-chain, and maintenance hardening

- [x] PEP 561 `py.typed` package marker
- [x] `python -m umai` entry point
- [x] Source/wheel distribution content validation
- [x] Full-SHA external GitHub Action pinning
- [x] Official latest Action releases reviewed and pinned
- [x] Automated commercial-manuscript boundary check
- [x] Canonical Gumroad/repository/contact link validation
- [x] Release-documentation/version consistency validation
- [x] Expanded security, privacy, dependency, accessibility, installation, signing, and repository-settings documentation
- [x] `v1.0.1` released from a Quality-verified commit
- [x] Wheel, source archive, and SHA-256 manifest attached from the immutable `v1.0.1` tag

## v1.1.0 — Portfolio projects, capstones, complete docs, and stable release hardening

- [x] 25 complete runnable companion projects
- [x] Five project groups covering evaluation, prompting/agents, release engineering, operations/privacy/cost, and integrated mastery
- [x] Five integrated capstone projects
- [x] Machine-readable 25-project catalog and catalog validator
- [x] Exact project-inventory smoke validation
- [x] Stable-subset JSON snapshot fixtures for capstones
- [x] Focused project tests in the standard unit-test suite
- [x] Cross-platform Project Matrix on Linux, Windows, and macOS
- [x] Durable social-link policy for long-lived repository/publication assets
- [x] Package/citation/API snapshot/README/changelog metadata promoted to 1.1.0 without changing stable public symbols
- [x] Canonical `docs/README.md` documentation hub
- [x] Complete user, developer, project-authoring, portfolio, compatibility, limitations, testing, release-process, release-asset, and release-runbook documentation
- [x] Repository completeness validator and `make repository-check`
- [x] Quality workflow integration for repository completeness, documentation, project, API, build, and release-candidate gates
- [x] Version-aware stable publication derived from package metadata
- [x] Exact-commit publication gate requiring CI, Quality, Project Matrix, Documentation Links, and Release Check
- [x] Immutable-tag release asset workflow for wheel/source/checksum artifacts
- [x] `scripts/check_release_automation.py` regression-protects stable publication and asset workflow contracts
- [x] Release Check and manual Release Candidate workflow validate release automation and repository integrity
- [x] Project Matrix is triggered by release-workflow changes and validates repository completeness across platforms
- [x] `make release-automation` and aggregate `make verify`
- [x] Expanded testing strategy and exact-release-commit checklist
- [x] 1.1.0 release notes prepared
- [ ] Verify all required checks on the exact final release-automation commit
- [ ] Promote that exact verified commit to `main`
- [ ] Let the verification-gated stable publication workflow create immutable `v1.1.0` and its GitHub release
- [ ] Verify immutable-tag wheel/source/checksum assets are attached
- [ ] Update release status/checklist/README after publication and close the release-tracking issue

## After 1.1.0

Future 1.x work should remain backward-compatible and maintenance-focused: regression-backed bug fixes, optional project additions, accessibility improvements, documentation corrections, dependency/action security updates, and maintenance of release automation. Major public-API redesigns should wait for a future major version.

## Complete book roadmap

The full 120-chapter learning progression and official commercial editions are available at:

### https://ramsandesh.gumroad.com
