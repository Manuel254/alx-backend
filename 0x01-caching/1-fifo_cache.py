#!/usr/bin/env python3
"""Fifo caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Implements Fifo Caching"""
    def __init__(self):
        """Initializes class"""
        super().__init__()

    def put(self, key, item):
        """Puts item in dictionary"""
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from cache"""
        return self.cache_data(key)
