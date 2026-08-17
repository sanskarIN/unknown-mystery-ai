# Container Companion Guide

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

The repository includes a minimal container example for the open-source Python companion package.

## Build

```bash
docker build -t unknown-mystery-ai:local .
```

## Run

```bash
docker run --rm unknown-mystery-ai:local
```

## Design choices

- Uses a small Python base image.
- Runs as a non-root user.
- Does not copy tests, local environments, PDFs, DOCX files, or secrets into the image.
- Does not expose a network port by default.
- Does not contain the commercial manuscript.

## Production note

A real serving image needs additional environment-specific controls: pinned image digests, vulnerability scanning, resource limits, health checks, network policy, secret injection, observability, rollback evidence, and a documented patch process.

Do not bake API keys or private data into a container layer. Use the secret-management mechanism provided by your deployment environment.
