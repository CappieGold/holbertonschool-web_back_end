#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.key_order = []
    
    def put(self, key, item):
        """ Add an item to the cache using LRU policy """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.key_order.remove(key)
        self.cache_data[key] = item
        self.key_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_use = self.key_order.pop(0)
            del self.cache_data[last_use]
            print(f"DISCARD: {last_use}")
    
    def get(self, key):
        """ Retrieve an item from the cache """
        return self.cache_data.get(key, None)
