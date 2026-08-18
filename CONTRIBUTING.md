# Contributing

> 🛒 **Official Gumroad store:** **https://ramsandesh.gumroad.com**

Thank you for helping improve the open-source companion repository for **_The Unknown Mystery of the AI_** by Ram Sandesh.

Start with [`docs/README.md`](docs/README.md) for the complete documentation map and [`docs/DEVELOPER_GUIDE.md`](docs/DEVELOPER_GUIDE.md) for the maintainer/developer workflow.

## Good contributions

Useful contributions include:

- reproducible bug fixes with regression tests,
- focused unit/integration tests,
- clearer or more accessible examples,
- documentation corrections,
- reproducibility improvements,
- dependency-light project improvements,
- project fixtures and diagnostics,
- safe and transparent AI engineering patterns,
- cross-platform fixes,
- security/privacy hardening that can be demonstrated safely.

## Keep commercial book content out of the repository

Do not submit the complete paid manuscript, chapter dumps, commercial PDF/DOCX files, cover source artwork, certificates, customer packages, or other All-Rights-Reserved publishing assets.

## Development setup

```bash
git clone https://github.com/sanskarIN/unknown-mystery-ai.git
cd unknown-mystery-ai
python -m venv .venv
python -m pip install -e .
python -m unittest discover -s tests -v
```

See [`docs/INSTALLATION.md`](docs/INSTALLATION.md) for platform-specific virtual-environment activation.

## Commit identity for local Git

The project maintainer uses:

```bash
git config user.name "Sanskar"
git config user.email "sanskarin@outlook.in"
```

Contributors should use their own valid Git identity unless they are the maintainer.

## Commit style

Prefer small, focused, independently understandable commits. Examples:

- `feat: add evaluation helper`
- `test: cover retrieval ranking`
- `docs: explain release manifests`
- `fix: reject invalid project metadata`
- `ci: add repository integrity gate`
- `chore: update build validation`

Do not split a single inseparable code change into artificial commits solely to increase commit count.

## Stable API compatibility

The documented 1.x public API is intentionally stable. Before exporting a new public symbol or changing existing public behavior, review:

- [`docs/API_COMPATIBILITY.md`](docs/API_COMPATIBILITY.md)
- [`docs/STABILITY.md`](docs/STABILITY.md)

Run:

```bash
python scripts/check_public_api.py --require-version-match
```

## Project contributions

Before adding or substantially changing a project, read [`docs/PROJECT_AUTHORING_GUIDE.md`](docs/PROJECT_AUTHORING_GUIDE.md).

Every default project run must remain non-interactive, credential-free, and valid JSON unless the repository contract is deliberately revised. New projects must be represented in `projects/catalog.json`.

## Required validation

Run the checks relevant to your change. For a broad repository change, use the full local sequence:

```bash
python scripts/check_repository_completeness.py
python scripts/check_package_metadata.py
python scripts/check_release_documentation.py
python scripts/check_workflow_pins.py
python scripts/check_public_repository_boundary.py
python scripts/check_project_links.py
python scripts/check_unstable_social_links.py
python scripts/check_markdown_links.py
python scripts/check_public_api.py --require-version-match
python scripts/check_project_catalog.py
python -m unittest discover -s tests -v
python scripts/check_projects.py
python scripts/check_project_snapshots.py
```

The 1.1.0 release-candidate path additionally uses:

```bash
python scripts/check_release_candidate.py
```

On compatible systems, equivalent convenience targets are available in the Makefile.

## Pull requests

A pull request should explain:

1. what changed,
2. why the change is needed,
3. compatibility impact,
4. validation performed,
5. limitations or follow-up work,
6. security/privacy considerations when relevant.

Use the repository pull-request template and do not mark checkboxes complete unless the corresponding check actually applies and has been performed.

## Security and privacy

Never include passwords, access tokens, API keys, private datasets, confidential logs, personal information, or sensitive user payloads in commits, tests, screenshots, issues, or pull requests.

For security-sensitive reports, follow [`SECURITY.md`](SECURITY.md) rather than publishing exploitable details publicly.

## Documentation

User-visible behavior or contracts should be documented. New major docs should be discoverable from [`docs/README.md`](docs/README.md), while project-specific details belong in the project README or project guides.

Long-lived project files should follow [`docs/SOCIAL_LINK_POLICY.md`](docs/SOCIAL_LINK_POLICY.md) and avoid change-prone X/Twitter profile URLs by default.

## Licensing

Source-code contributions are expected to be compatible with the repository's Apache License 2.0. See [`NOTICE`](NOTICE) and [`docs/LICENSE_SCOPE.md`](docs/LICENSE_SCOPE.md).

## Book and official releases

### **https://ramsandesh.gumroad.com**
