# Stable Release Assets

> 🛒 Official commercial publication: **https://ramsandesh.gumroad.com**

Stable GitHub software releases carry build artifacts for the Apache-2.0 companion package. They must never contain the paid eBook manuscript or separately copyrighted commercial publication assets.

## Current release state

The latest published stable software release remains **v1.0.1** until the prepared **1.1.0** source is verified and the stable publication workflow creates the new immutable release.

Current published stable release:

**https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.1**

The prepared 1.1.0 release notes live in [`COMPANION_RELEASE_1.1.0.md`](COMPANION_RELEASE_1.1.0.md).

## Stable publication pipeline

`.github/workflows/publish-stable.yml` runs only after a successful Quality run on `main`. Before publishing, it requires:

1. the Quality run SHA to match the current `main` SHA,
2. a stable semantic version in `pyproject.toml`,
3. matching versioned release notes and release checklist,
4. a matching changelog section,
5. successful exact-commit workflow evidence for CI, Quality, Project Matrix, Documentation Links, and Release Check.

Only then may it create `v<version>` and the GitHub release targeting that exact verified commit.

The workflow is version-aware and intentionally avoids hard-coding one historical release number.

## Immutable asset build

`.github/workflows/release-assets.yml` runs from the **published release tag**, not from the later moving `main` branch.

It verifies that the tag equals `v<pyproject version>`, reruns repository/package/project validation, builds the package, verifies distribution contents, generates checksums, and uploads:

- Python source distribution (`.tar.gz`),
- Python wheel (`.whl`),
- `SHA256SUMS.txt` covering the built package artifacts.

## Provenance rule

Release assets are built from the immutable release tag. This prevents post-release documentation or maintenance commits from silently changing the source identity associated with a historical stable version.

Historical stable releases remain available for reproducibility, including:

- **v1.0.0** — `https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.0`
- **v1.0.1** — `https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.1`

## Checksums

SHA-256 checksums help detect byte changes. They are integrity evidence, not by themselves proof of publisher identity. Preserve together:

- release tag,
- exact source commit,
- workflow history,
- release metadata,
- checksum manifest.

## Manual verification

After a stable release is published, verify:

```text
release tag == v<package version>
release target == verified commit
wheel version == package version
source archive version == package version
SHA256SUMS.txt exists
commercial book assets are absent
```

## Commercial publication boundary

Do **not** attach the complete eBook PDF/DOCX, paid chapter sources, cover package, certificate package, customer delivery bundles, or other restricted commercial assets to public GitHub software releases.

Official book editions and commercial publication materials belong at:

### **https://ramsandesh.gumroad.com**
