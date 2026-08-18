# Maintainer Release Runbook

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

This runbook is the operational companion to [`RELEASE_PROCESS.md`](RELEASE_PROCESS.md). It prevents a stable release from being published from an unverified, stale, or inconsistent commit.

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

The stable publication workflow also requires `docs/COMPANION_RELEASE_<version>.md` and `docs/RELEASE_<version_with_underscores>_CHECKLIST.md` to exist before release creation.

## 4. Run repository and automation integrity checks

```bash
python scripts/check_repository_completeness.py
python scripts/check_workflow_pins.py
python scripts/check_release_automation.py
python scripts/check_public_repository_boundary.py
python scripts/check_project_links.py
python scripts/check_unstable_social_links.py
python scripts/check_markdown_links.py
python scripts/check_project_catalog.py
```

Any failure blocks the release until the underlying issue is fixed.

`check_release_automation.py` prevents the stable workflow from silently reverting to a stale hard-coded historical tag and verifies that release assets are chained from stable-publication completion and rebuilt from the immutable tag.

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

On compatible systems, the main repository-level shortcuts include:

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

## 6. Build software distributions

```bash
python -m pip install build
python -m build
python scripts/check_distribution_contents.py
python scripts/create_checksum_manifest.py dist/* > dist/SHA256SUMS.txt
```

Inspect the built artifact names and verify the intended version appears in them.

## 7. Verify the exact commit in pull-request automation

The intended release commit should pass:

- CI,
- Quality,
- Project Matrix,
- Documentation Links,
- Release Check.

For the final prepared release, use a branch/PR whose **head SHA is the exact commit that will become `main`**. Fast-forwarding `main` to that verified head preserves exact source identity.

Do not infer success from an older commit after the release candidate has changed.

## 8. Promote the exact verified commit to `main`

After all required PR checks succeed, promote the exact verified head to `main` without introducing unverified source changes.

A later push on `main` will start CI/Quality and any path-relevant Project Matrix checks again. This is expected.

## 9. Automatic stable publication gate

`.github/workflows/publish-stable.yml` runs after a successful **Quality** run on `main`.

Before it can publish, it requires:

1. the successful Quality run SHA to equal the current `main` SHA,
2. stable `x.y.z` package metadata,
3. matching release notes, release checklist, and changelog section,
4. successful exact-SHA evidence for **CI, Quality, Project Matrix, Documentation Links, and Release Check**.

If another required workflow is still queued or running, stable publication waits. If a required workflow fails, publication fails instead of releasing an unverified source state.

The workflow derives `v<version>` dynamically from package metadata rather than embedding one historical release number.

## 10. Immutable tag and GitHub release

After all publication gates pass, the workflow creates:

```text
v<version>
```

and a GitHub release targeting the exact verified commit, using the versioned release-notes document.

Do not move a published stable tag later. If a release is wrong, publish a new patch version.

## 11. Release assets from the immutable tag

`.github/workflows/release-assets.yml` is chained from completion of the stable-publication workflow and also supports release/manual triggers.

The workflow:

1. resolves the published release tag,
2. checks out that immutable tag,
3. verifies `tag == v<package version>`,
4. reruns repository, package, API, project, and boundary validation,
5. builds wheel/source distributions,
6. verifies distribution contents,
7. creates `SHA256SUMS.txt`,
8. uploads software assets to the GitHub release.

This chaining does not rely solely on a `release` event generated by `GITHUB_TOKEN`, avoiding a common workflow-recursion limitation.

Expected software assets normally include:

- wheel,
- source distribution,
- `SHA256SUMS.txt`.

## 12. Enforce the commercial-publication boundary

Do **not** attach to the public Apache-2.0 software release:

- paid eBook PDF/DOCX files,
- chapter manuscripts,
- commercial cover packages,
- book certificates,
- paid publishing bundles,
- private customer files.

Run the public-repository boundary check before release and manually review release assets.

## 13. Publish/review release notes

Release notes should state:

- version,
- major additions/fixes,
- compatibility impact,
- verification performed,
- installation/use pointer,
- limitations where relevant,
- software/book licensing boundary,
- official publication destination.

## 14. Post-release verification

After publication:

- open the GitHub release page,
- confirm tag and release version match,
- confirm release target matches the verified source commit,
- confirm expected wheel/source/checksum assets exist,
- verify checksum manifest is present,
- confirm no commercial manuscript asset is attached,
- update `docs/RELEASE_STATUS.md`,
- update the roadmap/checklist,
- close the release-tracking issue when complete.

## 15. If a release problem is found

Do not rewrite history or silently replace a published stable tag. Instead:

1. document the defect,
2. fix it on a new branch,
3. add a regression test/check,
4. publish a new patch version after verification.

## Official publication

### 🛒 **https://ramsandesh.gumroad.com**
