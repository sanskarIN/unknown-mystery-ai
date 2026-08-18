"""In-process inference request/response contract demonstration."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from umai import InferenceRequest, LocalEndpoint, to_json


def handler(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    text = payload["text"]
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return {"normalized": " ".join(text.split()), "length": len(text)}


def response_dict(response: object) -> dict[str, object]:
    return {
        "request_id": getattr(response, "request_id"),
        "model_version": getattr(response, "model_version"),
        "ok": getattr(response, "ok"),
        "output": dict(getattr(response, "output")),
        "error_code": getattr(response, "error_code"),
    }


def main() -> None:
    endpoint = LocalEndpoint(handler)
    valid = endpoint.handle(
        InferenceRequest("req-001", "local-text-v1", {"text": "  local   serving contract  "})
    )
    invalid = endpoint.handle(
        InferenceRequest("req-002", "local-text-v1", {"unexpected": "field"})
    )
    print(to_json({"valid_request": response_dict(valid), "invalid_request": response_dict(invalid)}))


if __name__ == "__main__":
    main()
