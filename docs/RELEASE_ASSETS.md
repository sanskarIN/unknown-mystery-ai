# Stable Release Assets

> 🛒 Official commercial publication: **https://ramsandesh.gumroad.com**

Stable GitHub software releases carry build artifacts for the Apache-2.0 companion package. They must not contain the paid eBook manuscript or separately copyrighted commercial publication assets.

## Current stable release

The current maintenance release is **v1.0.1**.

Release page: **https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.1**

The release asset workflow builds directly from the immutable version tag and uploads:

- the Python source distribution (`.tar.gz`),
- the Python wheel (`.whl`),
- `SHA256SUMS.txt` covering the built package artifacts.

## Provenance rule

Release assets are built from the immutable release tag, not from later commits on `main`. This prevents post-release documentation or maintenance commits from silently changing the bytes associated with a historical stable version.

The historical **v1.0.0** release remains available at:

**https://github.com/sanskarIN/unknown-mystery-ai/releases/tag/v1.0.0**

## Checksums

SHA-256 checksums help detect byte changes. They are integrity evidence, not by themselves proof of publisher identity. Preserve the Git tag, source commit, workflow history, and release metadata together with the checksums.

## Commercial publication boundary

Do **not** attach the complete eBook PDF/DOCX, paid chapter sources, cover package, certificate package, or other restricted commercial assets to public GitHub software releases.

Official book editions and commercial publication materials belong at:

### **https://ramsandesh.gumroad.com**
