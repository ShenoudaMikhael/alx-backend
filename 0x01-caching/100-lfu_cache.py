#!/usr/bin/python3
"""100-lfu_cache"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """LFUCache Class"""

    def __init__(self):
        super().__init__()

        self.frequent_use = {}

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        all_keys = list(self.cache_data.keys())
        if len(all_keys) >= BaseCaching.MAX_ITEMS and key not in all_keys:
            print("DISCARD: {}".format(all_keys[0]))
            del self.cache_data[all_keys[0]]

        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
