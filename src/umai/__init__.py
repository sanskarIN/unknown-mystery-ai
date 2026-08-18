"""Companion utilities for *The Unknown Mystery of the AI*.

Official book store: https://ramsandesh.gumroad.com
"""

from .budget import TokenPricing, estimate_token_cost, requests_within_budget
from .cache import BoundedCache
from .compare import MetricDelta, ReleaseComparison, compare_metrics
from .config import FeatureFlags, parse_bool
from .deprecation import DeprecatedFeature, warn_deprecated
from .drift import mean_shift, standardized_mean_shift
from .evaluation import accuracy_score, classification_report
from .evidence import EvidenceBundle
from .experiments import ExperimentRecord, best_record
from .fallback import FallbackResult, run_fallback_chain
from .gates import GateResult, ReleaseDecision, evaluate_release_gates
from .links import GITHUB_REPOSITORY, GUMROAD_STORE
from .monitoring import MetricPoint, synthetic_metric_series
from .observability import MetricEvent, mean_metric
from .placement import PlacementOption, eligible_placements
from .privacy import pseudonymous_id, redact_common_identifiers
from .prompts import PromptTemplate
from .ranking import precision_at_k, recall_at_k, reciprocal_rank
from .rate_limit import FixedWindowRateLimiter
from .registry import ArtifactRegistry, ArtifactVersion
from .regression import RegressionCase, RegressionResult, evaluate_output
from .release import ReleaseManifest
from .reporting import key_value_report, to_json, to_serializable
from .reproducibility import fingerprint_json, seed_everything
from .retrieval import Document, SimpleRetriever
from .retry import retry_call
from .serving import InferenceRequest, InferenceResponse, LocalEndpoint
from .text import chunk_text, normalize_whitespace
from .validation import ValidationIssue, validate_record

__all__ = [
    "accuracy_score",
    "ArtifactRegistry",
    "ArtifactVersion",
    "best_record",
    "BoundedCache",
    "chunk_text",
    "classification_report",
    "compare_metrics",
    "DeprecatedFeature",
    "Document",
    "eligible_placements",
    "estimate_token_cost",
    "evaluate_output",
    "evaluate_release_gates",
    "EvidenceBundle",
    "ExperimentRecord",
    "FallbackResult",
    "FeatureFlags",
    "fingerprint_json",
    "FixedWindowRateLimiter",
    "GateResult",
    "GITHUB_REPOSITORY",
    "GUMROAD_STORE",
    "InferenceRequest",
    "InferenceResponse",
    "key_value_report",
    "LocalEndpoint",
    "mean_metric",
    "mean_shift",
    "MetricDelta",
    "MetricEvent",
    "MetricPoint",
    "normalize_whitespace",
    "parse_bool",
    "PlacementOption",
    "precision_at_k",
    "PromptTemplate",
    "pseudonymous_id",
    "recall_at_k",
    "reciprocal_rank",
    "redact_common_identifiers",
    "RegressionCase",
    "RegressionResult",
    "ReleaseComparison",
    "ReleaseDecision",
    "ReleaseManifest",
    "requests_within_budget",
    "retry_call",
    "run_fallback_chain",
    "seed_everything",
    "SimpleRetriever",
    "standardized_mean_shift",
    "synthetic_metric_series",
    "to_json",
    "TokenPricing",
    "to_serializable",
    "ValidationIssue",
    "validate_record",
    "warn_deprecated",
]

__version__ = "1.1.0"
