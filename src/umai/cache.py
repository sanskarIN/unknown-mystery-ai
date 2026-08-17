"""A tiny bounded in-memory cache for deterministic teaching examples.

Official book store: https://ramsandesh.gumroad.com
"""

from __future__ import annotations

from collections import OrderedDict
from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class BoundedCache(Generic[K, V]):
    """Least-recently-used cache with an explicit maximum item count."""

    def __init__(self, max_items: int = 128) -> None:
        if max_items <= 0:
            raise ValueError("max_items must be greater than zero")
        self.max_items = max_items
        self._items: OrderedDict[K, V] = OrderedDict()

    def get(self, key: K, default: V | None = None) -> V | None:
        if key not in self._items:
            return default
        value = self._items.pop(key)
        self._items[key] = value
        return value

    def set(self, key: K, value: V) -> None:
        if key in self._items:
            self._items.pop(key)
        self._items[key] = value
        while len(self._items) > self.max_items:
            self._items.popitem(last=False)

    def clear(self) -> None:
        self._items.clear()

    def __len__(self) -> int:
        return len(self._items)
