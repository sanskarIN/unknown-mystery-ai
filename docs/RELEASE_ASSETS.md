# Stable Release Assets

> 🛒 Official commercial publication: **https://ramsandesh.gumroad.com**

The GitHub **v1.0.0** software release can carry build artifacts for the Apache-2.0 companion package. It must not contain the paid eBook manuscript or separately copyrighted commercial publication assets.

## Attached software artifacts

The release-asset workflow builds directly from the immutable `v1.0.0` Git tag and uploads:

- the Python source distribution (`.tar.gz`),
- the Python wheel (`.whl`),
- `SHA256SUMS.txt` covering the built package artifacts.

## Provenance rule

Release assets are built from `v1.0.0`, not from later commits on `main`. This prevents post-release documentation or maintenance commits from silently changing the bytes associated with the historical stable tag.

## Checksums

SHA-256 checksums help detect byte changes. They are integrity evidence, not by themselves proof of publisher identity. Preserve the Git tag, source commit, workflow history, and release metadata together with the checksums.

## Commercial publication boundary

Do **not** attach the complete eBook PDF/DOCX, paid chapter sources, cover package, certificate package, or other restricted commercial assets to the public GitHub software release.

Official book editions and commercial publication materials belong at:

### **https://ramsandesh.gumroad.com**
