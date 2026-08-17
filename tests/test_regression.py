import unittest

from umai.regression import RegressionCase, evaluate_output


class RegressionTests(unittest.TestCase):
    def test_required_and_forbidden_terms(self) -> None:
        case = RegressionCase(
            "grounded-answer",
            required_substrings=("evidence",),
            forbidden_substrings=("guaranteed",),
        )
        self.assertTrue(evaluate_output(case, "The evidence supports this conclusion.").passed)
        self.assertFalse(evaluate_output(case, "This is guaranteed.").passed)

    def test_case_insensitive_default(self) -> None:
        case = RegressionCase("case", required_substrings=("AI",))
        self.assertTrue(evaluate_output(case, "ai system").passed)


if __name__ == "__main__":
    unittest.main()
