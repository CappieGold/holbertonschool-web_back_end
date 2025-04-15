#!/usr/bin/python3
""" Basic dictionary
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system that does not enforce any limit.
    """

    def put(self, key, item):
        """ Add an item in the cache
        :param key: The key for the cache entry.
        :param item: The value associated with the key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        :param key: the key to be retrieved in the cache
        :returns: The value associated to the key, None otherwise
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
