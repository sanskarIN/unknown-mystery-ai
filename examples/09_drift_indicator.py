"""Demonstrate a small numeric drift indicator.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.drift import mean_shift, standardized_mean_shift


reference = [100.0, 101.0, 99.0, 100.5, 100.2]
current = [104.0, 105.0, 103.5, 104.2, 104.7]

print("absolute mean shift:", round(mean_shift(reference, current), 3))
print("standardized mean shift:", round(standardized_mean_shift(reference, current), 3))
print("Interpret this only with application-specific thresholds and context.")
