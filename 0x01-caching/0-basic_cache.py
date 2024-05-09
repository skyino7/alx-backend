#!/usr/bin/env python3
"""
Create a class BasicCache that inherits
from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """

    def put(self, key, item):
        """
        Assigns item to key in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in the cache linked to key
        """
        return self.cache_data.get(key, None)
