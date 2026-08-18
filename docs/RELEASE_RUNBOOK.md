# Maintainer Release Runbook

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This runbook is the operational companion to [`RELEASE_PROCESS.md`](RELEASE_PROCESS.md). It is intended to prevent a release from being published from an unverified or inconsistent commit.

## 1. Define the release scope

Before changing version metadata, write down:

- target version,
- compatibility level,
- intended user-visible changes,
- whether the stable public API changes,
- whether project/output contracts change,
- whether any migration note is required.

For 1.x releases, preserve the stable public API unless the change is explicitly reviewed under the compatibility policy.

## 2. Verify the working branch

Confirm the release branch starts from the intended `main` commit and contains only reviewed changes.

Do not mix unrelated experimental work into a release candidate merely to increase commit count.

## 3. Coordinate version metadata

Version-bearing files must agree. Depending on the release, this includes:

- `pyproject.toml`,
- `src/umai/__init__.py`,
- `api/public_api_1_0.json`,
- `CITATION.cff`,
- README version badge/text,
- `CHANGELOG.md`,
- versioned release notes,
- versioned release checklist.

Run:

```bash
python scripts/check_package_metadata.py
python scripts/check_release_documentation.py
python scripts/check_public_api.py --require-version-match
```

## 4. Run repository integrity checks

```bash
python scripts/check_repository_completeness.py
python scripts/check_workflow_pins.py
python scripts/check_public_repository_boundary.py
python scripts/check_project_links.py
python scripts/check_unstable_social_links.py
python scripts/check_markdown_links.py
python scripts/check_project_catalog.py
```

Any failure blocks the release until the underlying issue is fixed.

## 5. Run tests and projects

```bash
python -m unittest discover -s tests -v
python scripts/check_projects.py
python scripts/check_project_snapshots.py
```

For the current 1.1.0 candidate:

```bash
python scripts/check_release_candidate.py
```

## 6. Build software distributions

```bash
python -m pip install build
python -m build
python scripts/check_distribution_contents.py
python scripts/create_checksum_manifest.py dist/* > dist/SHA256SUMS.txt
```

Inspect the built artifact names and verify the intended version appears in them.

## 7. Verify pull-request automation

The intended release commit should pass the required verification stack, including:

- CI,
- Quality,
- Project Matrix,
- Documentation Links when relevant,
- Release Check when relevant.

Do not infer success from an older commit after the release candidate has changed.

## 8. Freeze the release commit

After the exact intended commit passes the required checks, stop adding unrelated changes to it. Record the commit SHA in the release checklist/status documentation.

## 9. Create the immutable tag

Create `v<version>` from the exact verified release commit.

Do not move a published stable tag to a different commit later. If a release is wrong, publish a new patch version instead.

## 10. Build/publish from the tag

Release assets should be produced from the immutable tag rather than a later moving `main` branch.

Expected companion software assets normally include:

- wheel,
- source distribution,
- `SHA256SUMS.txt`.

## 11. Enforce the commercial-publication boundary

Do **not** attach to the public Apache-2.0 software release:

- paid eBook PDF/DOCX files,
- chapter manuscripts,
- commercial cover packages,
- book certificates,
- paid publishing bundles,
- private customer files.

Run the public-repository boundary check before release and manually review release assets.

## 12. Publish release notes

Release notes should state:

- version,
- major additions/fixes,
- compatibility impact,
- verification performed,
- installation/use pointer,
- limitations where relevant,
- software/book licensing boundary,
- official publication destination.

## 13. Post-release verification

After publication:

- open the GitHub release page,
- confirm tag and release version match,
- confirm expected software assets exist,
- verify checksum manifest is present,
- confirm no commercial manuscript asset is attached,
- update `docs/RELEASE_STATUS.md`,
- update the roadmap/checklist,
- close the release-tracking issue when complete.

## 14. If a release problem is found

Do not rewrite history or silently replace a published stable tag. Instead:

1. document the defect,
2. fix it on a new branch,
3. add a regression test/check,
4. publish a new patch version after verification.

## Official publication

### 🛒 **https://ramsandesh.gumroad.com**
