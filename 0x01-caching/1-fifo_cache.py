#!/usr/bin/env python3
"""FIFO cache implementation"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key not in self.queue:
            self.queue.append(key)
        if len(self.queue) > BaseCaching.MAX_ITEMS:
            discard = self.queue.pop(0)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """Retrieves an item from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
