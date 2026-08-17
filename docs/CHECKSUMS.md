# Release Checksums

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

The quality workflow generates SHA-256 checksums for open-source companion build artifacts.

## Create a local manifest

After building:

```bash
python -m pip install build
python -m build
python scripts/create_checksum_manifest.py dist/* > SHA256SUMS.txt
```

## Why checksums matter

A checksum can help detect accidental or unexpected byte changes between an artifact and a published manifest. It does **not** by itself prove who produced the artifact. For stronger release provenance, combine checksums with protected release workflows, signed attestations where available, immutable source references, and documented build inputs.

## Commercial book files

The public GitHub companion does not publish the paid eBook artifacts. Official commercial editions and publication downloads belong on **https://ramsandesh.gumroad.com**.
