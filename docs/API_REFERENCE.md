# Companion API Reference

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

This is the compact reference for the dependency-light public utilities exported by `umai`.

## Reproducibility

- `seed_everything(seed)` — seed supported standard-library randomness.
- `fingerprint_json(value)` — stable fingerprint for JSON-compatible data.

## Classification and ranking evaluation

- `accuracy_score(expected, predicted)` — simple classification accuracy.
- `classification_report(...)` — compact classification metrics.
- `precision_at_k(...)` — precision in the first `k` retrieved identifiers.
- `recall_at_k(...)` — recall in the first `k` results.
- `reciprocal_rank(...)` — reciprocal rank of the first relevant result.

## Retrieval and agents

- `Document` / `SimpleRetriever` — lexical retrieval baseline.
- agent utilities in `umai.agents` — explicit local tool registration and routing.

## Text and prompts

- `normalize_whitespace` / `chunk_text` — deterministic baseline text transforms.
- `PromptTemplate` — versioned explicit prompt variables.
- `RegressionCase` / `RegressionResult` / `evaluate_output` — transparent output regression expectations.

## Experiments, releases, and governance

- `ExperimentRecord` / `best_record` — compact experiment evidence and selection.
- `ArtifactVersion` / `ArtifactRegistry` — version registration and approval demonstration.
- `ReleaseManifest` — explicit release identity.
- `compare_metrics` / `MetricDelta` / `ReleaseComparison` — metric deltas between named releases.
- `evaluate_release_gates` / `GateResult` / `ReleaseDecision` — transparent PASS/BLOCK release checks.
- `EvidenceBundle` — structured source/check/metric evidence with deterministic JSON export.

## Serving and placement

- `InferenceRequest` / `InferenceResponse` / `LocalEndpoint` — in-process serving contract baseline.
- `PlacementOption` / `eligible_placements` — filter edge/cloud options by declared constraints.
- `FeatureFlags` / `parse_bool` — explicit boolean configuration.

## Monitoring and data quality

- `MetricEvent` / `mean_metric` — privacy-aware metric examples.
- `MetricPoint` / `synthetic_metric_series` — deterministic synthetic dashboard data.
- `mean_shift` / `standardized_mean_shift` — lightweight numeric drift indicators.
- `validate_record` / `ValidationIssue` — minimal boundary schema validation.

## Privacy and operations

- `redact_common_identifiers` / `pseudonymous_id` — privacy teaching helpers.
- `TokenPricing` / `estimate_token_cost` / `requests_within_budget` — caller-supplied cost estimation.
- `BoundedCache` — explicit LRU-style item bound.
- `FixedWindowRateLimiter` — deterministic request admission by supplied window ID.
- `retry_call` — bounded retries for explicitly retryable exceptions.
- `run_fallback_chain` / `FallbackResult` — declared ordered fallback path for recoverable failures.

## Reporting and compatibility

- `to_serializable(value)` — convert supported companion evidence values to JSON-compatible structures.
- `to_json(value, indent=2)` — deterministic sorted JSON rendering.
- `key_value_report(values)` — stable CLI-friendly text output.
- `DeprecatedFeature` / `warn_deprecated` — actionable public API deprecation messaging.

## Command line

After installation, `umai-companion` exposes project metadata without network access:

```bash
umai-companion version
umai-companion store
umai-companion repository
umai-companion info
umai-companion info --json
```

See [`CLI.md`](CLI.md) and [`API_COMPATIBILITY.md`](API_COMPATIBILITY.md).

These utilities are intentionally small. Production systems still need application-specific requirements, threat modeling, security, privacy review, capacity planning, monitoring, incident response, governance, and validation.

### Official book store: **https://ramsandesh.gumroad.com**
