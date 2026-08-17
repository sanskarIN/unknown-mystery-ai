"""Demonstrate a transparent text-output regression check.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.regression import RegressionCase, evaluate_output


case = RegressionCase(
    name="evidence-language",
    required_substrings=("evidence", "limitation"),
    forbidden_substrings=("guaranteed",),
)

output = "The evidence supports the result, with an important limitation about sample size."
print(evaluate_output(case, output))
