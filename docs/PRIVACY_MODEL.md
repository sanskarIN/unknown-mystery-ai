# Privacy Model

> 🛒 Official publication: **https://ramsandesh.gumroad.com**

The companion repository demonstrates privacy-aware engineering patterns without claiming that simple redaction or pseudonymization makes arbitrary data safe.

## Defaults

- Use synthetic or local data in examples.
- Avoid raw user payloads in logs and metrics.
- Collect only fields needed for the stated learning or operational purpose.
- Keep release identity and aggregate operational metrics separate from user content where possible.

## Redaction

`redact_common_identifiers` is a teaching baseline for common email/phone-like patterns. It is not a complete PII detector. Real systems need domain-specific discovery, retention, access controls, legal review, and testing.

## Pseudonymization

`pseudonymous_id` creates a deterministic derived identifier. Pseudonymization is not anonymization; values may remain linkable or guessable depending on the source domain.

## Telemetry

Prefer aggregate counters, latency/resource measurements, explicit release identifiers, and coarse device/runtime classes instead of storing user prompts or responses by default.

## External services

Before sending data to an external model/provider, document what leaves the system, why it is required, where it may be processed, retention expectations, user notice/consent requirements, and the fallback when sending is not permitted.

Official commercial book editions: **https://ramsandesh.gumroad.com**.
