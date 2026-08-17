"""Demonstrate explicit cache bounds and LRU eviction.

Official publication: https://ramsandesh.gumroad.com
"""

from umai.cache import BoundedCache


cache: BoundedCache[str, str] = BoundedCache(max_items=2)
cache.set("prompt:v1", "first response")
cache.set("prompt:v2", "second response")
print("v1:", cache.get("prompt:v1"))
cache.set("prompt:v3", "third response")
print("v2 after eviction:", cache.get("prompt:v2"))
print("cache size:", len(cache))
