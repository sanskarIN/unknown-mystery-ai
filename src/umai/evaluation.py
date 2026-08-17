"""Dependency-free evaluation helpers for small teaching examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from collections import Counter
from typing import Hashable, Iterable

Label = Hashable


def _materialize_pairs(
    y_true: Iterable[Label], y_pred: Iterable[Label]
) -> tuple[list[Label], list[Label]]:
    true_values = list(y_true)
    pred_values = list(y_pred)
    if len(true_values) != len(pred_values):
        raise ValueError("y_true and y_pred must have the same length")
    if not true_values:
        raise ValueError("evaluation inputs must not be empty")
    return true_values, pred_values


def accuracy_score(y_true: Iterable[Label], y_pred: Iterable[Label]) -> float:
    """Return the fraction of exactly matching labels."""
    true_values, pred_values = _materialize_pairs(y_true, y_pred)
    matches = sum(actual == predicted for actual, predicted in zip(true_values, pred_values))
    return matches / len(true_values)


def classification_report(
    y_true: Iterable[Label], y_pred: Iterable[Label]
) -> dict[str, dict[str, float | int]]:
    """Return per-label precision, recall, F1, and support.

    Labels are represented as strings in the returned mapping so the report can be
    serialized easily for small release/evaluation artifacts.
    """
    true_values, pred_values = _materialize_pairs(y_true, y_pred)
    labels = sorted(set(true_values) | set(pred_values), key=lambda value: str(value))
    supports = Counter(true_values)

    report: dict[str, dict[str, float | int]] = {}
    for label in labels:
        tp = sum(a == label and p == label for a, p in zip(true_values, pred_values))
        fp = sum(a != label and p == label for a, p in zip(true_values, pred_values))
        fn = sum(a == label and p != label for a, p in zip(true_values, pred_values))

        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall = tp / (tp + fn) if (tp + fn) else 0.0
        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall)
            else 0.0
        )

        report[str(label)] = {
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "support": supports[label],
        }

    report["__overall__"] = {
        "accuracy": accuracy_score(true_values, pred_values),
        "samples": len(true_values),
    }
    return report
