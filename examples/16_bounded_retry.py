"""Demonstrate retrying only a known temporary failure.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.retry import retry_call


state = {"calls": 0}


def unstable_operation() -> str:
    state["calls"] += 1
    if state["calls"] < 2:
        raise RuntimeError("synthetic temporary failure")
    return "success"


print(retry_call(unstable_operation, attempts=3, retry_on=(RuntimeError,)))
print("attempts used:", state["calls"])
