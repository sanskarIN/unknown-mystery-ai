# Testing Strategy

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The companion uses layered validation for dependency-light utilities, runnable projects, documentation, packaging, release automation, and release evidence. No single check is treated as a universal proof of production fitness.

## 1. Repository completeness

`scripts/check_repository_completeness.py` validates the durable structural baseline:

- expected top-level governance/build files,
- complete documentation baseline,
- required CI/release workflows,
- required quality/release scripts,
- 25-record machine-readable project catalog,
- documentation-index discoverability,
- canonical Gumroad link in key durable files.

This catches accidental deletion or omission of repository-critical material before deeper tests run.

## 2. Unit tests

The standard-library test suite covers normal behavior, meaningful boundaries, explicit failure behavior, and determinism where determinism is part of the contract.

Run:

```bash
python -m unittest discover -s tests -v
```

The five integrated capstones also have focused tests that execute the same public command path used by learners and assert durable result facts.

## 3. Stable public API validation

`tests/test_public_api.py` verifies basic export invariants. `scripts/check_public_api.py` compares the actual public exports to the committed stable 1.x API snapshot.

Run:

```bash
python scripts/check_public_api.py --require-version-match
```

New projects should normally compose existing stable helpers instead of widening the public API without compatibility review.

## 4. Numbered example smoke tests

Numbered examples use local/synthetic input and require no interactive input. Cross-platform automation exercises them on supported operating systems/Python versions.

A smoke test primarily answers: "Can the documented example execute successfully in a clean supported environment?"

## 5. Project catalog validation

`projects/catalog.json` is the machine-readable source for project identity, title, category, learning level, entry point, and snapshot status.

`scripts/check_project_catalog.py` verifies:

- schema assumptions,
- unique IDs,
- valid categories/levels,
- entry-point existence,
- README presence,
- snapshot declarations,
- catalog/directory parity,
- canonical publication link.

## 6. Project inventory smoke tests

`scripts/check_projects.py` requires the exact committed project inventory. Every default project run must:

- exit successfully,
- emit valid JSON,
- remain non-interactive,
- require no provider credentials or network calls by default.

This catches missing projects, unexpected entry points, import errors, runtime failures, and malformed default output.

## 7. Capstone snapshot tests

The five integrated capstones contain `expected.json` subset fixtures. `scripts/check_project_snapshots.py` executes each capstone and compares only durable selected fields.

Subset snapshots avoid converting incidental display details into permanent compatibility promises while still catching meaningful regressions.

## 8. Cross-platform Project Matrix

`.github/workflows/projects.yml` validates repository completeness, the project catalog, all project runs, and capstone snapshots across:

- Linux,
- Windows,
- macOS,
- multiple supported Python versions.

The matrix is also triggered by stable-release automation changes so a final release candidate does not bypass cross-platform project evidence merely because the last code change was in a release workflow.

See [`COMPATIBILITY_MATRIX.md`](COMPATIBILITY_MATRIX.md).

## 9. Documentation and policy checks

Automated checks validate:

- repository-local Markdown links,
- canonical project/Gumroad/contact links,
- durable social-link policy,
- public/commercial publication boundary,
- full-SHA GitHub Actions pins,
- release-documentation/version consistency.

## 10. Stable release automation contract

`scripts/check_release_automation.py` validates the durable publication workflow contract. It verifies that:

- stable publication is chained from successful Quality completion on `main`,
- the exact current `main` SHA must match the verified Quality SHA,
- CI, Quality, Project Matrix, Documentation Links, and Release Check are required for the same commit,
- the version/tag is derived from package metadata,
- versioned release notes/checklists are required,
- release assets are chained from stable-publication completion,
- assets are rebuilt from the immutable published tag,
- historical version-specific tags are not hard-coded back into the current release workflows.

Run:

```bash
python scripts/check_release_automation.py
```

This is a structural contract check. The actual GitHub workflow run remains the authoritative evidence that the automation executed successfully.

## 11. Package and build checks

The Quality workflow:

1. validates repository/release automation structure,
2. installs the package,
3. runs tests/examples/projects,
4. builds wheel and source distributions,
5. verifies distribution contents,
6. generates SHA-256 checksum evidence,
7. uploads build evidence for inspection.

The distribution checker verifies that required package content such as `py.typed` is actually present in built artifacts.

## 12. Release-candidate invariants

For the 1.1.0 candidate:

```bash
python scripts/check_release_candidate.py
```

This validates coordinated version metadata, public API snapshot version, release files, project count, capstone fixtures, and required workflows.

## 13. Exact-commit publication evidence

The stable publication workflow runs only after a successful Quality run on `main`. It then waits for successful exact-SHA evidence for:

- CI,
- Quality,
- Project Matrix,
- Documentation Links,
- Release Check.

A missing or still-running workflow keeps publication pending; a failed required workflow blocks publication.

## 14. Immutable release-asset validation

After stable publication, the asset workflow checks out the immutable tag and reruns repository, package, API, project, snapshot, and boundary checks before creating and uploading wheel/source/checksum assets.

This separates pre-release evidence from post-tag artifact provenance.

## 15. Recommended full local sequence

```bash
python scripts/check_repository_completeness.py
python scripts/check_package_metadata.py
python scripts/check_release_documentation.py
python scripts/check_workflow_pins.py
python scripts/check_release_automation.py
python scripts/check_public_repository_boundary.py
python scripts/check_project_links.py
python scripts/check_unstable_social_links.py
python scripts/check_markdown_links.py
python scripts/check_public_api.py --require-version-match
python scripts/check_project_catalog.py
python -m unittest discover -s tests -v
python scripts/check_projects.py
python scripts/check_project_snapshots.py
python scripts/check_release_candidate.py
```

On compatible systems:

```bash
make repository-check
make release-automation
make test
make project-catalog
make projects
make project-snapshots
make release-check
make verify
```

## Failure policy

Do not weaken or delete a quality check merely because it detects a real mismatch. Determine whether the source, documentation, metadata, fixture, workflow, or check is wrong, fix the underlying issue, and add regression evidence when useful.

## What automation cannot prove

Passing automation does **not** automatically prove production safety, security, privacy, fairness, scalability, reliability, legal/regulatory compliance, model quality on real data, or fitness for a specific application. Those require context-specific evidence and accountable review.

Official commercial editions remain available at **https://ramsandesh.gumroad.com**.
