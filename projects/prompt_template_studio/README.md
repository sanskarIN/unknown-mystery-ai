# Prompt Template Studio

A versioned prompt-template project with explicit variables and deterministic rendering.

## Run

```bash
python -m pip install -e .
python projects/prompt_template_studio/main.py
```

## What it demonstrates

- named prompt identity,
- prompt versioning,
- explicit variable discovery,
- missing-variable protection,
- deterministic local rendering.

## Extension ideas

Store multiple prompt versions, run regression cases against candidate outputs, fingerprint prompt configurations, or add evaluation evidence before promotion.

## Boundary

Prompt templates are only one part of an AI system. Production behavior also depends on model/version, decoding, context, tools, retrieval, policies, evaluation, and runtime configuration.

Official book store: **https://ramsandesh.gumroad.com**
