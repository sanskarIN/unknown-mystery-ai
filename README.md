# The Unknown Mystery of the AI - Companion Repository

<p align="center">
  <strong>Learn • Build • Deploy • Audit • Master AI</strong>
</p>

<p align="center">
  <a href="https://ramsandesh.gumroad.com"><img src="assets/gumroad-store-badge.svg" alt="Get The Unknown Mystery of the AI on Gumroad" width="420"></a>
</p>

<p align="center">
  <a href="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/quality.yml"><img alt="Quality" src="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/quality.yml/badge.svg"></a>
  <a href="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/projects.yml"><img alt="Project Matrix" src="https://github.com/sanskarIN/unknown-mystery-ai/actions/workflows/projects.yml/badge.svg"></a>
  <img alt="Version 1.1.0" src="https://img.shields.io/badge/version-1.1.0-brightgreen">
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
  <a href="https://ramsandesh.gumroad.com"><img alt="Gumroad" src="https://img.shields.io/badge/Gumroad-Official%20Store-ff90e8"></a>
</p>

> ## 🛒 Official store: **https://ramsandesh.gumroad.com**

This is the official open-source companion repository for **_The Unknown Mystery of the AI_** by **Ram Sandesh**. Main-branch version **1.1.0** is a backward-compatible project-expansion release candidate with dependency-light Python utilities, examples, tests, **25 runnable portfolio projects**, five integrated capstones, release evidence, cross-platform validation, security/privacy guidance, packaging checks, and complete maintainer/user documentation.

The repository is intentionally **inspectable, testable, local/synthetic by default, and safe for learning**. It does not present small teaching utilities as automatic substitutes for production security, privacy, scalability, governance, reliability, or legal review.

## What is included

- Evaluation and reproducibility helpers
- Text normalization and deterministic chunking
- Prompt templates and output-regression fixtures
- Local lexical RAG and retrieval ranking metrics
- Transparent allowlisted agent/tool routing patterns
- Experiment records, artifact registries, release manifests, evidence bundles, and release gates
- Serving contracts, monitoring data, edge/cloud placement, feature flags, caching, retry, fallback, and rate limiting
- Privacy redaction, validation, cost budgeting, and responsible-AI review patterns
- Stable 1.x public API snapshot checks
- PEP 561 inline typing support
- 25 complete JSON-emitting companion projects
- Five integrated capstones with stable-subset snapshots
- Linux/Windows/macOS project verification
- Wheel/source-distribution build and checksum evidence
- Documentation for users, developers, project authors, maintainers, releases, security, privacy, and portfolio work

## Quick start

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
python -m pip install -e .
python -m unittest discover -s tests -v
```

See [`docs/INSTALLATION.md`](docs/INSTALLATION.md) for platform-specific virtual-environment activation and stable-release installation guidance.

Use the companion CLI:

```bash
umai-companion version
umai-companion info
umai-companion info --json
umai-companion store
python -m umai info
```

## Validation commands

Run the repository's main local checks:

```bash
python scripts/check_repository_completeness.py
python scripts/check_project_catalog.py
python scripts/check_projects.py
python scripts/check_project_snapshots.py
python scripts/check_public_api.py --require-version-match
python -m unittest discover -s tests -v
```

For the 1.1.0 release candidate:

```bash
python scripts/check_release_candidate.py
```

On compatible systems, Makefile shortcuts include:

```bash
make install
make test
make examples
make repository-check
make project-catalog
make projects
make project-snapshots
make release-check
make build
```

## Examples

The numbered example suite covers reproducibility, evaluation, RAG, agents, release identity, observability, prompts, drift, budgets, privacy, caching, validation, experiments, artifact approvals, retry/rate limits, serving, release gates, monitoring, edge/cloud placement, feature flags, ranking metrics, regression checks, release comparison, fallback, deprecation, and structured evidence.

See [`examples/README.md`](examples/README.md).

## Companion projects

The repository contains **25 runnable projects** grouped into five learning stages.

### Foundation and evaluation

1. Evaluation Report Studio
2. Experiment Leaderboard
3. RAG Knowledge Explorer
4. Retrieval Ranking Benchmark
5. Text Chunking Lab

### Prompting, agents, and serving

6. Prompt Template Studio
7. Prompt Regression Lab
8. Agent Router Sandbox
9. Local Serving Contract
10. Resilient Request Pipeline

### Governance and release engineering

11. Artifact Registry Workflow
12. Release Manifest Builder
13. Evidence Bundle Builder
14. Release Comparison Dashboard
15. Release Gate Simulator

### Operations, privacy, and cost

16. Feature Flag Rollout Lab
17. Edge Cloud Planner
18. Model Monitoring Lab
19. Privacy Audit Workbench
20. Cost Budget Planner

### Integrated capstones

21. AI Release Readiness Console
22. RAG Evaluation Capstone
23. MLOps Release Pipeline
24. Responsible AI Review Board
25. Production Resilience Lab

The canonical machine-readable inventory is [`projects/catalog.json`](projects/catalog.json). See [`projects/README.md`](projects/README.md), [`docs/PROJECTS.md`](docs/PROJECTS.md), and [`docs/PROJECT_CATALOG.md`](docs/PROJECT_CATALOG.md).

## Complete documentation

**Start with [`docs/README.md`](docs/README.md)** for the complete documentation map.

Important guides include:

- [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md) - end-to-end user workflow
- [`docs/LEARNING_PATH.md`](docs/LEARNING_PATH.md) - recommended learning sequence
- [`docs/BOOK_COMPANION.md`](docs/BOOK_COMPANION.md) - book/repository relationship
- [`docs/CHAPTER_COMPANION_INDEX.md`](docs/CHAPTER_COMPANION_INDEX.md) - 120-chapter companion mapping
- [`docs/API_REFERENCE.md`](docs/API_REFERENCE.md) - public API reference
- [`docs/API_COMPATIBILITY.md`](docs/API_COMPATIBILITY.md) - compatibility/versioning policy
- [`docs/DEVELOPER_GUIDE.md`](docs/DEVELOPER_GUIDE.md) - complete developer workflow
- [`docs/PROJECT_AUTHORING_GUIDE.md`](docs/PROJECT_AUTHORING_GUIDE.md) - project contribution contract
- [`docs/PORTFOLIO_GUIDE.md`](docs/PORTFOLIO_GUIDE.md) - reproducible portfolio evidence
- [`docs/COMPATIBILITY_MATRIX.md`](docs/COMPATIBILITY_MATRIX.md) - validated platforms/Python versions
- [`docs/KNOWN_LIMITATIONS.md`](docs/KNOWN_LIMITATIONS.md) - intentional limitations and non-goals
- [`docs/TESTING_STRATEGY.md`](docs/TESTING_STRATEGY.md) - validation layers
- [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) - common failures and fixes
- [`docs/SECURITY_MODEL.md`](docs/SECURITY_MODEL.md) - security assumptions
- [`docs/PRIVACY_MODEL.md`](docs/PRIVACY_MODEL.md) - privacy boundaries
- [`docs/RESPONSIBLE_AI_CHECKLIST.md`](docs/RESPONSIBLE_AI_CHECKLIST.md) - responsible-AI review
- [`docs/SUPPLY_CHAIN.md`](docs/SUPPLY_CHAIN.md) - supply-chain controls
- [`docs/SOCIAL_LINK_POLICY.md`](docs/SOCIAL_LINK_POLICY.md) - durable-link policy
- [`docs/RELEASE_RUNBOOK.md`](docs/RELEASE_RUNBOOK.md) - maintainer release procedure
- [`docs/RELEASE_STATUS.md`](docs/RELEASE_STATUS.md) - current release identity
- [`docs/RELEASE_1_1_0_CHECKLIST.md`](docs/RELEASE_1_1_0_CHECKLIST.md) - 1.1.0 verification checklist
- [`docs/COMPANION_RELEASE_1.1.0.md`](docs/COMPANION_RELEASE_1.1.0.md) - prepared 1.1.0 release notes

## Repository map

```text
unknown-mystery-ai/
├── api/                       # stable public API snapshots
├── assets/                    # repository visual assets and Gumroad badge
├── docs/                      # complete user/developer/maintainer documentation
├── examples/                  # focused runnable teaching examples
├── projects/                  # 25 runnable projects + machine-readable catalog
├── scripts/                   # quality/release/catalog/boundary validators
├── src/umai/                  # stable dependency-light typed package
├── tests/                     # standard-library unit/integration tests
├── .github/                   # CI, project matrix, quality, release automation
├── Dockerfile                 # non-root educational container example
├── LICENSE                    # Apache License 2.0 for source code
├── NOTICE                     # publication-rights boundary notice
├── Makefile                   # local validation shortcuts
└── README.md
```

## Quality gates

The automated quality stack validates:

- repository/documentation structural completeness,
- package and release metadata consistency,
- stable public API consistency,
- Python unit tests,
- numbered example smoke runs,
- exact 25-project catalog parity,
- valid JSON from all 25 default project runs,
- five capstone stable-subset snapshots,
- Linux/Windows/macOS project execution,
- full-SHA GitHub Action pins,
- public/commercial publication boundaries,
- canonical long-lived links,
- rejection of durable X/Twitter profile URLs outside policy exceptions,
- repository-local Markdown links,
- wheel/source distribution contents,
- SHA-256 build manifests,
- release-candidate invariants.

Passing these checks is strong repository evidence but is not a universal production-safety, security, fairness, privacy, or legal certification.

## Stable software release

The latest **published stable GitHub software release remains v1.0.1 until the 1.1.0 release candidate is fully verified and tagged**.

Current published stable release:

`https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.1`

Prepared 1.1.0 notes: [`docs/COMPANION_RELEASE_1.1.0.md`](docs/COMPANION_RELEASE_1.1.0.md).

## Licensing boundary

The **source code** in this repository is licensed under the **Apache License 2.0** unless a file states otherwise.

The complete eBook, chapter text, PDF/DOCX editions, cover artwork, certificate artwork, book-specific illustrations, and commercial publication packages are **© 2026 Ram Sandesh. All Rights Reserved.** They are intentionally not distributed under Apache-2.0 or included in the public software release.

See [`NOTICE`](NOTICE) and [`docs/LICENSE_SCOPE.md`](docs/LICENSE_SCOPE.md).

## Author and durable project links

- Author: **Ram Sandesh**
- GitHub: **https://github.com/sanskarIN**
- Repository: **https://github.com/sanskarIN/unknown-mystery-ai**
- Official Gumroad store: **https://ramsandesh.gumroad.com**
- Contact: **sanskarin@outlook.in**

Long-lived project/publication files intentionally avoid depending on a change-prone X/Twitter profile URL. See [`docs/SOCIAL_LINK_POLICY.md`](docs/SOCIAL_LINK_POLICY.md).

## Contributing, support, and security

- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- [`SUPPORT.md`](SUPPORT.md)
- [`SECURITY.md`](SECURITY.md)
- [`MAINTAINERS.md`](MAINTAINERS.md)

Do not publish secrets, credentials, private datasets, personal information, or sensitive user payloads in issues, tests, examples, fixtures, or pull requests.

---

<p align="center">
  <strong>Support the complete AI learning journey:</strong><br>
  <a href="https://ramsandesh.gumroad.com"><strong>🛒 https://ramsandesh.gumroad.com</strong></a>
</p>
