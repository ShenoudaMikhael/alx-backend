#!/usr/bin/python3
"""2-lifo_cache"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache Class"""

    def __init__(self):
        self.last_key = None
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        all_keys = list(self.cache_data.keys())
        if len(all_keys) >= BaseCaching.MAX_ITEMS and key not in all_keys:
            print("DISCARD: {}".format(self.last_key))
            del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
