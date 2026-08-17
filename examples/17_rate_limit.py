"""Demonstrate deterministic request admission with a fixed window.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.rate_limit import FixedWindowRateLimiter


limiter = FixedWindowRateLimiter(limit=3)
for request_number in range(1, 6):
    print(request_number, "allowed=" + str(limiter.allow(window_id=100)))

print("next window allowed:", limiter.allow(window_id=101))
