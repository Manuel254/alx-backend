#!/usr/bin/env python3
"""Basic Dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching System"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        return self.cache_data.get(key, None)
