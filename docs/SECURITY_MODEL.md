# Companion Security Model

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

This repository is an educational companion, but it still follows explicit security boundaries.

## Default assumptions

- Core utilities do not require network access.
- Examples do not require real credentials.
- Synthetic/local data is preferred.
- Commercial manuscript files are excluded from public code paths and container contexts.

## Trust boundaries

Treat these as untrusted unless validated:

- external user input,
- files and datasets,
- model/provider responses,
- tool outputs,
- environment variables,
- network responses,
- cached data from another release identity.

## Required patterns for future integrations

Any adapter that connects to an external service should document credential handling, data flow, timeout/retry behavior, input/output validation, logging policy, failure modes, and how to disable the integration.

## Secrets

Never commit API keys, passwords, access tokens, private certificates, or user secrets. If a secret is exposed, revoke or rotate it immediately; simply deleting it from a later commit is insufficient.

## Dependency and supply-chain risk

Keep runtime dependencies minimal, review GitHub Action updates, validate package builds, and preserve source/release identity. See [`DEPENDENCIES.md`](DEPENDENCIES.md) and [`SUPPLY_CHAIN.md`](SUPPLY_CHAIN.md).

## Reporting vulnerabilities

Follow the instructions in [`../SECURITY.md`](../SECURITY.md).

Official book releases: **https://ramsandesh.gumroad.com**.
