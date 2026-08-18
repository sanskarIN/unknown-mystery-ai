# Testing Strategy

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The companion uses layered validation for dependency-light utilities, runnable projects, documentation, packaging, and release evidence. No single check is treated as a universal proof of production fitness.

## 1. Repository completeness

`scripts/check_repository_completeness.py` validates the durable structural baseline:

- expected top-level governance/build files,
- complete documentation baseline,
- required CI/release workflows,
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

`.github/workflows/projects.yml` validates the project catalog, all project runs, and capstone snapshots across:

- Linux,
- Windows,
- macOS,
- multiple supported Python versions.

See [`COMPATIBILITY_MATRIX.md`](COMPATIBILITY_MATRIX.md).

## 9. Documentation and policy checks

Automated checks validate:

- repository-local Markdown links,
- canonical project/Gumroad/contact links,
- durable social-link policy,
- public/commercial publication boundary,
- full-SHA GitHub Actions pins,
- release-documentation/version consistency.

## 10. Package and build checks

The Quality workflow:

1. installs the package,
2. runs tests/examples/projects,
3. builds wheel and source distributions,
4. verifies distribution contents,
5. generates SHA-256 checksum evidence,
6. uploads build evidence for inspection.

The distribution checker verifies that required package content such as `py.typed` is actually present in built artifacts.

## 11. Release-candidate invariants

For the 1.1.0 candidate:

```bash
python scripts/check_release_candidate.py
```

This validates coordinated version metadata, public API snapshot version, release files, project count, capstone fixtures, and required workflows.

## 12. Recommended full local sequence

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
python scripts/check_release_candidate.py
```

On compatible systems:

```bash
make repository-check
make test
make project-catalog
make projects
make project-snapshots
make release-check
```

## Failure policy

Do not weaken or delete a quality check merely because it detects a real mismatch. Determine whether the source, documentation, metadata, fixture, or check is wrong, fix the underlying issue, and add regression evidence when useful.

## What automation cannot prove

Passing automation does **not** automatically prove production safety, security, privacy, fairness, scalability, reliability, legal/regulatory compliance, model quality on real data, or fitness for a specific application. Those require context-specific evidence and accountable review.

Official commercial editions remain available at **https://ramsandesh.gumroad.com**.
