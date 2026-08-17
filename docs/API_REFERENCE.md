# Companion API Reference

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

This is a compact reference for the dependency-light teaching utilities in `src/umai/`.

## Reproducibility

- `seed_everything(seed)` — seed supported standard-library randomness.
- `fingerprint_json(value)` — stable fingerprint for JSON-compatible data.

## Evaluation

- `accuracy_score(expected, predicted)` — simple classification accuracy.
- `classification_report(...)` — compact classification metrics.

## Retrieval and agents

- `Document` / `SimpleRetriever` — lexical retrieval baseline.
- agent utilities in `umai.agents` — explicit local tool registration and routing.

## Releases and observability

- `ReleaseManifest` — explicit release identity.
- `MetricEvent` / `mean_metric` — privacy-aware metric examples.

## Text and prompts

- `normalize_whitespace` / `chunk_text` — deterministic baseline text transforms.
- `PromptTemplate` — versioned explicit prompt variables.

## Operations

- `TokenPricing` / `estimate_token_cost` — caller-supplied cost estimation.
- `BoundedCache` — explicit LRU-style item bound.
- `FixedWindowRateLimiter` — deterministic request admission by supplied window ID.
- `retry_call` — bounded retries for explicitly retryable exceptions.

## Governance and data quality

- `redact_common_identifiers` / `pseudonymous_id` — privacy teaching helpers.
- `validate_record` — minimal boundary schema validation.
- `mean_shift` / `standardized_mean_shift` — lightweight numeric drift indicators.
- `ExperimentRecord` / `best_record` — experiment evidence and comparison.
- `ArtifactVersion` / `ArtifactRegistry` — version registration and approval demonstration.

These utilities are intentionally small. Production systems need application-specific requirements, threat modeling, reliability engineering, privacy review, monitoring, and validation.
