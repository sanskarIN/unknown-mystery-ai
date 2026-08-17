# Commit and Tag Signing

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

Git commit signatures add publisher-authentication evidence that is separate from ordinary author metadata.

## Maintainer identity

Repository work should use:

```bash
git config user.name "Sanskar"
git config user.email "sanskarin@outlook.in"
```

The email identifies the requested commit identity; it does **not** by itself cryptographically sign a commit.

## Signing options

Git can sign commits and tags using supported GPG, SSH, or platform signing setups. After configuring a trusted signing key locally, maintainers can enable signing for new commits and create signed annotated tags according to their Git/GitHub setup.

## Important limitation

Existing unsigned commits are not made signed by editing later files. Rewriting public history merely to add signatures is generally undesirable after a stable release because it changes commit identities and can break references.

## Stable release

Keep the published `v1.0.0` historical tag/release intact. Apply a signing policy prospectively to future release work rather than rewriting the already-published release history.

## Verification

When signing is configured, verify GitHub displays the expected verification status and confirm the key belongs to the intended maintainer account before relying on it as provenance evidence.

Official commercial editions remain at **https://ramsandesh.gumroad.com**.
