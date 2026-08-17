"""Dependency-free request/response contracts for serving demonstrations.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class InferenceRequest:
    request_id: str
    model_version: str
    payload: Mapping[str, Any]

    def __post_init__(self) -> None:
        if not self.request_id.strip():
            raise ValueError("request_id must not be empty")
        if not self.model_version.strip():
            raise ValueError("model_version must not be empty")


@dataclass(frozen=True)
class InferenceResponse:
    request_id: str
    model_version: str
    ok: bool
    output: Mapping[str, Any] = field(default_factory=dict)
    error_code: str | None = None


class LocalEndpoint:
    """Execute an in-process handler behind an explicit serving contract."""

    def __init__(self, handler: Callable[[Mapping[str, Any]], Mapping[str, Any]]) -> None:
        self._handler = handler

    def handle(self, request: InferenceRequest) -> InferenceResponse:
        try:
            output = self._handler(request.payload)
        except (ValueError, TypeError, KeyError):
            return InferenceResponse(
                request_id=request.request_id,
                model_version=request.model_version,
                ok=False,
                error_code="INVALID_REQUEST",
            )
        return InferenceResponse(
            request_id=request.request_id,
            model_version=request.model_version,
            ok=True,
            output=dict(output),
        )
