"""Companion utilities for *The Unknown Mystery of the AI*.

Official book store: https://ramsandesh.gumroad.com
"""

from .budget import TokenPricing, estimate_token_cost, requests_within_budget
from .cache import BoundedCache
from .config import FeatureFlags, parse_bool
from .drift import mean_shift, standardized_mean_shift
from .evaluation import accuracy_score, classification_report
from .experiments import ExperimentRecord, best_record
from .gates import GateResult, ReleaseDecision, evaluate_release_gates
from .links import GITHUB_REPOSITORY, GUMROAD_STORE
from .monitoring import MetricPoint, synthetic_metric_series
from .observability import MetricEvent, mean_metric
from .placement import PlacementOption, eligible_placements
from .privacy import pseudonymous_id, redact_common_identifiers
from .prompts import PromptTemplate
from .rate_limit import FixedWindowRateLimiter
from .registry import ArtifactRegistry, ArtifactVersion
from .release import ReleaseManifest
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
    "Document",
    "eligible_placements",
    "estimate_token_cost",
    "evaluate_release_gates",
    "ExperimentRecord",
    "FeatureFlags",
    "fingerprint_json",
    "FixedWindowRateLimiter",
    "GateResult",
    "GITHUB_REPOSITORY",
    "GUMROAD_STORE",
    "InferenceRequest",
    "InferenceResponse",
    "LocalEndpoint",
    "mean_metric",
    "mean_shift",
    "MetricEvent",
    "MetricPoint",
    "normalize_whitespace",
    "parse_bool",
    "PlacementOption",
    "PromptTemplate",
    "pseudonymous_id",
    "redact_common_identifiers",
    "ReleaseDecision",
    "ReleaseManifest",
    "requests_within_budget",
    "retry_call",
    "seed_everything",
    "SimpleRetriever",
    "standardized_mean_shift",
    "synthetic_metric_series",
    "TokenPricing",
    "ValidationIssue",
    "validate_record",
]

__version__ = "0.3.0"
