#!/usr/bin/emv python3
""" LFU Caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU Caching """

    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.cache_data = {}
        self.lfu = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lfu.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_key = self.lfu.pop(0)
                    del self.cache_data[lfu_key]
                    print("DISCARD: {}".format(lfu_key))
                self.cache_data[key] = item
            self.lfu.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.cache_data:
            self.lfu.remove(key)
            self.lfu.append(key)
            return self.cache_data[key]
        return None
