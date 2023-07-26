#!/usr/bin/env python3
"""This module contains a class that implements the
MRU Caching Replacement Algorithm
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """This class implements the methods responsible
    for adding data to the cache and retrieving data from
    cache
    """
    def __init__(self):
        """Initializes the class with the cache dictionary"""
        super().__init__()
        self.recent_keys = []

    def put(self, key, item):
        """Adds data to cache or replaces data if cache
        is full
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                pop_key = self.recent_keys[-1]
                self.cache_data.pop(pop_key)
                print("DISCARD: {}".format(pop_key))
            self.cache_data[key] = item
            self.recent_keys.append(key)

    def get(self, key):
        """Gets an item from the cache"""
        self.recent_keys.append(key)
        return self.cache_data.get(key, None)
