import unittest

from umai.budget import TokenPricing, estimate_token_cost, requests_within_budget


class BudgetTests(unittest.TestCase):
    def test_estimated_cost(self) -> None:
        pricing = TokenPricing(input_per_million=2.0, output_per_million=4.0)
        value = estimate_token_cost(input_tokens=500_000, output_tokens=250_000, pricing=pricing)
        self.assertEqual(value, 2.0)

    def test_requests_within_budget(self) -> None:
        self.assertEqual(requests_within_budget(budget=10.0, cost_per_request=2.5), 4)

    def test_negative_tokens_rejected(self) -> None:
        pricing = TokenPricing(1.0, 1.0)
        with self.assertRaises(ValueError):
            estimate_token_cost(input_tokens=-1, output_tokens=0, pricing=pricing)


if __name__ == "__main__":
    unittest.main()
