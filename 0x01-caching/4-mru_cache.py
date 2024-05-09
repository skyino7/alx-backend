#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = self.keys.pop()
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

        self.cache_data[key] = item
        self.keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.keys.remove(key)
        self.keys.append(key)

        return self.cache_data[key]
