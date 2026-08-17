"""Estimate a hypothetical request budget using caller-supplied pricing.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.budget import TokenPricing, estimate_token_cost, requests_within_budget


pricing = TokenPricing(input_per_million=1.5, output_per_million=3.0)
request_cost = estimate_token_cost(
    input_tokens=8_000,
    output_tokens=2_000,
    pricing=pricing,
)

print("hypothetical cost per request:", round(request_cost, 6))
print("requests in a 10-unit budget:", requests_within_budget(budget=10.0, cost_per_request=request_cost))
print("Use current provider pricing supplied by your own application; values here are illustrative only.")
