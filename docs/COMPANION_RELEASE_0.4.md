# Companion Release 0.4

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

Version 0.4 expands evaluation and reliability examples.

## Added

- retrieval ranking metrics: precision@k, recall@k, reciprocal rank,
- transparent prompt/output regression fixtures,
- release metric comparison and explicit deltas,
- ordered fallback chains for explicitly recoverable failures.

## Evaluation rule

Metrics are evidence, not automatic proof of quality. Choose metrics before comparing candidates, document their direction and thresholds, preserve the evaluation dataset identity, and inspect regressions instead of hiding them behind one aggregate number.

## Reliability rule

Fallbacks should be explicit, observable, bounded, and used only for failures that are genuinely recoverable. Validation, authorization, policy, and data-quality failures should not be silently retried or bypassed.

Official commercial book editions remain available from **https://ramsandesh.gumroad.com**.
