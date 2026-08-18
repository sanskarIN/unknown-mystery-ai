"""Caller-supplied token-pricing and request-budget planner."""

from __future__ import annotations

import argparse

from umai import TokenPricing, estimate_token_cost, requests_within_budget, to_json


def main() -> None:
    parser = argparse.ArgumentParser(description="Estimate AI request cost from caller-supplied pricing.")
    parser.add_argument("--input-tokens", type=int, default=1800)
    parser.add_argument("--output-tokens", type=int, default=600)
    parser.add_argument("--input-price", type=float, default=150.0, help="Price per 1M input tokens in your chosen currency.")
    parser.add_argument("--output-price", type=float, default=450.0, help="Price per 1M output tokens in your chosen currency.")
    parser.add_argument("--budget", type=float, default=1000.0)
    parser.add_argument("--currency", default="INR")
    args = parser.parse_args()

    pricing = TokenPricing(
        input_per_million=args.input_price,
        output_per_million=args.output_price,
    )
    request_cost = estimate_token_cost(
        input_tokens=args.input_tokens,
        output_tokens=args.output_tokens,
        pricing=pricing,
    )
    capacity = requests_within_budget(budget=args.budget, cost_per_request=request_cost)

    print(
        to_json(
            {
                "currency": args.currency,
                "pricing_source": "caller supplied; not live vendor pricing",
                "input_tokens": args.input_tokens,
                "output_tokens": args.output_tokens,
                "estimated_cost_per_request": round(request_cost, 6),
                "budget": args.budget,
                "whole_requests_within_budget": capacity,
            }
        )
    )


if __name__ == "__main__":
    main()
