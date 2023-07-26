#!/usr/bin/env python3
"""Basic Dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Caching System"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key)
