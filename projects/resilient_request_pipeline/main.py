"""Bounded-cache and explicit fallback-chain reliability exercise."""

from __future__ import annotations

from umai import BoundedCache, run_fallback_chain, to_json


def unavailable_primary() -> str:
    raise RuntimeError("synthetic primary unavailable")


def local_fallback() -> str:
    return "local-fallback-response"


def main() -> None:
    cache: BoundedCache[str, str] = BoundedCache(max_items=2)
    key = "demo-request"
    cached = cache.get(key)

    if cached is None:
        result = run_fallback_chain(
            [("primary", unavailable_primary), ("local", local_fallback)],
            recoverable=(RuntimeError,),
        )
        cache.set(key, result.value)
        first = {
            "cache_hit": False,
            "provider": result.provider,
            "attempts": list(result.attempts),
            "value": result.value,
        }
    else:
        first = {"cache_hit": True, "provider": "cache", "attempts": [], "value": cached}

    second = cache.get(key)
    print(
        to_json(
            {
                "first_request": first,
                "second_request": {
                    "cache_hit": second is not None,
                    "provider": "cache" if second is not None else None,
                    "value": second,
                },
                "cache_size": len(cache),
            }
        )
    )


if __name__ == "__main__":
    main()
