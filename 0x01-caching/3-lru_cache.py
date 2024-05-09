#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from
BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class
    """
    def __init__(self):
        """
        Initialize the class
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            elif len(self.keys) >= BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))
            self.keys.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        if key and key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
        return None
