#!/usr/bin/python3
"""LIFOCache implementation with correct behavior"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add or update cache, discard the last added item if over capacity.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed = self.order.pop(-2)
            del self.cache_data[removed]
            print(f"DISCARD: {removed}")

    def get(self, key):
        """Get cache item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
