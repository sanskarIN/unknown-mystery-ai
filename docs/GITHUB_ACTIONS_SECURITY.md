# GitHub Actions Security

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

Repository workflows pin external GitHub Actions to full commit SHAs rather than relying only on movable major-version tags.

## Current policy

- External `uses:` references must use a 40-character commit SHA.
- A human-readable version comment is kept beside the SHA for reviewability.
- `scripts/check_workflow_pins.py` enforces the rule in the Quality and release-candidate workflows.
- Dependabot monitors GitHub Actions updates so newer releases can be reviewed and repinned deliberately.

## Why pin commits

A full commit SHA makes the exact action source used by a workflow explicit. This reduces the risk that a mutable tag changes unexpectedly between otherwise identical workflow runs.

## Updating a pin

Before changing an action SHA:

1. Review the official action release and changelog.
2. Confirm the SHA belongs to the intended release tag in the official GitHub repository.
3. Update the SHA and nearby version comment together.
4. Let CI/Quality verify the workflow after the change.
5. Review requested permissions and behavior changes, especially across major versions.

## Permissions

Workflows should use the narrowest practical `permissions:` block. Read-only workflows use `contents: read`; publishing workflows request `contents: write` only when they need to create or upload release assets.

Official commercial publication remains at **https://ramsandesh.gumroad.com**.
