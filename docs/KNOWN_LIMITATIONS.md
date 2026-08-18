# Known Limitations and Non-Goals

> 🛒 Official book store: **https://ramsandesh.gumroad.com**

The companion repository intentionally keeps a narrow, inspectable educational scope. These boundaries are design choices, not hidden claims of production completeness.

## Educational scope

The utilities, examples, and projects demonstrate engineering concepts with small local or synthetic inputs. They are not a replacement for a full production AI platform.

## No built-in model-provider integration

The stable package does not require API credentials and does not depend on a specific hosted model provider. Real provider adapters may require authentication, network controls, retry policies, quotas, cost controls, privacy review, and provider-specific evaluation.

## No production authentication or authorization layer

Local serving examples demonstrate request/response contracts, not a complete identity, authentication, authorization, tenancy, or policy-enforcement system.

## No production database

Examples use in-memory or local structures. A real system may need durable databases, migrations, transactions, backups, access controls, encryption, retention rules, and recovery testing.

## No distributed execution framework

The repository does not implement a distributed scheduler, cluster manager, distributed training framework, or large-scale task queue.

## No universal AI quality threshold

Metrics, drift indicators, release gates, and cost assumptions are examples. A threshold that is appropriate for one system may be unsafe or meaningless for another. Production thresholds require application-specific evidence.

## No automatic fairness or safety certification

Responsible-AI checklists and review projects structure reasoning and evidence. They do not certify that a system is fair, safe, compliant, or suitable for high-stakes use.

## No legal or regulatory guarantee

The repository contains educational governance guidance, not legal advice. Applicable obligations vary by jurisdiction, domain, organization, data type, and use case.

## Privacy helpers are limited

Common identifier redaction and pseudonymous identifiers are teaching primitives. They do not guarantee anonymization or prevent re-identification in arbitrary datasets.

## Security examples are defensive baselines

Security documentation explains boundaries and safe defaults but does not turn the small companion into a complete security product. Production systems need context-specific threat modeling, access control, secure secret management, monitoring, vulnerability management, and incident response.

## Synthetic and deterministic data

Many examples deliberately use deterministic synthetic inputs. This improves reproducibility but means results should not be interpreted as evidence about a real deployment or real-world population.

## Project JSON is an educational contract

Project JSON output is designed for inspectability and automated validation. It is not a universal external API schema and may be extended compatibly as projects grow.

## Snapshot scope is selective

Capstone `expected.json` fixtures verify stable subsets of outputs rather than every field. This avoids brittle tests while still detecting meaningful regressions.

## Package version versus book edition

The open-source software companion version and the commercial book edition are separate version identities. A software release does not imply a new commercial manuscript edition.

## Commercial assets are intentionally excluded

The complete eBook, chapter manuscripts, PDF/DOCX files, cover artwork, certificates, and other commercial publication assets are not part of the Apache-2.0 repository.

## No promise of future backwards compatibility across major versions

The 1.x line follows the documented stable API policy. A future 2.x release may introduce a redesigned API with migration guidance.

## Reporting limitations or bugs

For reproducible software issues, use the repository issue templates and include:

- package version or commit,
- Python version,
- operating system,
- minimal reproduction steps,
- expected behavior,
- actual behavior,
- sanitized error output.

Do not include secrets or private user data.

## Official publication

### 🛒 **https://ramsandesh.gumroad.com**
