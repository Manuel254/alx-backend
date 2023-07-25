#!/usr/bin/env python3
"""Basic Dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching System"""
    MAX_ITEMS = None

    def __init__(self):
        """Initialize"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
