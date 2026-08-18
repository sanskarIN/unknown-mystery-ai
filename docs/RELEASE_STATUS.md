# Release Status

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

## Prepared 1.1.0 release candidate

- Package metadata: **1.1.0**
- Status: **final release candidate / exact-commit verification required before publication**
- Public API: stable 1.x symbol set unchanged
- Runtime dependency policy: no new mandatory third-party runtime dependency
- Scope: 25 runnable projects, five integrated capstones, machine-readable project catalog, stable-subset snapshots, cross-platform Project Matrix, complete documentation, repository completeness checks, and verification-gated stable publication automation

The final 1.1.0 source must pass the repository completeness, release-automation, Quality, CI, Project Matrix, Documentation Links, and Release Check stack on the **exact intended release commit** before it is promoted to `main` and published.

The prepared stable-publication workflow derives `v<version>` from package metadata, verifies the exact current `main` SHA, waits for the required workflow stack, and only then creates the immutable GitHub release. The release-asset workflow rebuilds wheel/source/checksum artifacts from that immutable tag.

## Current published stable release

Until the verification-gated 1.1.0 publication succeeds, the current published stable release remains:

- Package: **unknown-mystery-ai**
- Version: **1.0.1**
- Git tag: **v1.0.1**
- GitHub release: **UMAI Companion v1.0.1**
- Verified release commit: `3835e7031304d9bcbe0c9150ea5d4a03fbda7c74`
- Release type: stable, not a prerelease
- Release page: **https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.1**

The `v1.0.1` tag/release was created only after verification of its release source.

## Attached 1.0.1 software assets

The current published stable release contains companion software assets built from the immutable `v1.0.1` tag:

- `unknown_mystery_ai-1.0.1-py3-none-any.whl`
- `unknown_mystery_ai-1.0.1.tar.gz`
- `SHA256SUMS.txt`

These remain historical 1.0.1 artifacts and are not changed by 1.1.0 preparation work.

## Prepared 1.1.0 publication flow

The final 1.1.0 publication sequence is:

1. verify the exact release-candidate commit in PR automation,
2. promote that exact commit to `main`,
3. let main CI/Quality/Project Matrix/documentation/release checks complete,
4. let `Publish Stable` verify exact-SHA evidence and create `v1.1.0`,
5. let `Attach Stable Release Assets` check out the immutable tag,
6. rebuild/verify wheel and source distribution,
7. generate and upload `SHA256SUMS.txt`,
8. verify no commercial manuscript/publication asset is attached,
9. update this file to mark 1.1.0 as the published stable release.

See [`RELEASE_RUNBOOK.md`](RELEASE_RUNBOOK.md), [`RELEASE_ASSETS.md`](RELEASE_ASSETS.md), and [`RELEASE_1_1_0_CHECKLIST.md`](RELEASE_1_1_0_CHECKLIST.md).

## Historical stable release

The original stable release remains available for reproducibility:

- Version: **1.0.0**
- Tag: **v1.0.0**
- Verified release commit: `4d118452a21fd650e0cb1c75af30393f87a8cd37`
- Release page: **https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.0**

## Release immutability

Historical tags are the source of truth for published stable artifacts. Later `main` commits do not change the meaning or source identity of `v1.0.0`, `v1.0.1`, or any future immutable stable tag.

If a published stable release has a defect, create and verify a new patch release instead of moving the old tag.

## Commercial publication

GitHub releases cover the Apache-2.0 open-source companion. They do not contain the paid eBook manuscript or separately copyrighted commercial publication assets.

Official commercial editions: **https://ramsandesh.gumroad.com**.
