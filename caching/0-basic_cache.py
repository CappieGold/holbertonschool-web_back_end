#!/usr/bin/python3
""" Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system that does not enforce any limit.
    """

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
