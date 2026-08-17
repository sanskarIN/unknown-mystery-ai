"""Compare deployment placement using explicit constraints.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.placement import PlacementOption, eligible_placements


options = [
    PlacementOption("mobile-npu", 18.0, 2.5, 0.95, True),
    PlacementOption("regional-cloud", 70.0, 1.2, 0.75, False),
    PlacementOption("central-cloud", 120.0, 0.9, 0.65, False),
]

selected = eligible_placements(
    options,
    max_latency_ms=50.0,
    min_privacy_score=0.8,
    require_offline=True,
)
print("eligible:", [item.name for item in selected])
