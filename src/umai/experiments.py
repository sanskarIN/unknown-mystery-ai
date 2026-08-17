"""Minimal experiment records for reproducible comparisons.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping

from .reproducibility import fingerprint_json


@dataclass(frozen=True)
class ExperimentRecord:
    """Capture a compact experiment identity and numeric metrics."""

    name: str
    parameters: Mapping[str, object]
    metrics: Mapping[str, float] = field(default_factory=dict)

    @property
    def fingerprint(self) -> str:
        return fingerprint_json({"name": self.name, "parameters": dict(self.parameters)})

    def metric(self, name: str) -> float:
        if name not in self.metrics:
            raise KeyError(f"unknown metric: {name}")
        return float(self.metrics[name])


def best_record(records: list[ExperimentRecord], metric: str, *, higher_is_better: bool = True) -> ExperimentRecord:
    """Select a record using one explicitly named metric."""

    if not records:
        raise ValueError("records must be non-empty")
    key = lambda record: record.metric(metric)
    return max(records, key=key) if higher_is_better else min(records, key=key)
