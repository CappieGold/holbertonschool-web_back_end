#!/usr/bin/python3
""" Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ caching system
    """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ LIFO
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed = self.order.pop()
            del self.cache_data[removed]
            print(f"DISCARD: {removed}")

    def get(self, key):
        """ get methode
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
