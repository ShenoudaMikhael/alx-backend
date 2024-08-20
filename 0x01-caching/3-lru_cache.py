#!/usr/bin/python3
"""3-lru_cache"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class"""

    def __init__(self):
        self.last_used = None
        super().__init__()

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        all_keys = list(self.cache_data.keys())

        if len(all_keys) >= BaseCaching.MAX_ITEMS and key not in all_keys:

            print("DISCARD: {}".format(self.last_used))
            del self.cache_data[self.last_used]

        self.last_used = key
        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.last_used = key

        return self.cache_data[key]
