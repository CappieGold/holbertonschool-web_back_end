#!/usr/bin/python3
""" Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ caching system
    """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the item value for the key.

        If key or item is None, this method does nothing.
        If the number of items in self.cache_data is higher
        than BaseCaching.MAX_ITEMS, discard the first item put in cache
        (FIFO algorithm) and print DISCARD: <key>
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed = self.order.pop(0)
            del self.cache_data[removed]
            print(f"DISCARD: {removed}")

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get[key]
