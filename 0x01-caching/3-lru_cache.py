#!/usr/bin/python3
"""3-lru_cache"""
BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """LRUCache Class"""

    def __init__(self):
        super().__init__()
        self.last_used = []

    def get_lru_item(self, usage_list):
        """get_lru_item"""
        seen = set()
        lru_item = None

        # Traverse the list in reverse order
        for item in reversed(usage_list):
            if item not in seen:
                seen.add(item)
                lru_item = item

        return lru_item

    def put(self, key, item):
        """put function"""
        if key is None or item is None:
            return
        all_keys = list(self.cache_data.keys())
        if len(all_keys) >= BaseCaching.MAX_ITEMS and key not in all_keys:
            to_discard = self.get_lru_item(self.last_used)

            print("DISCARD: {}".format(to_discard))
            del self.cache_data[to_discard]
            self.last_used = [i for i in self.last_used if i != to_discard]

        self.last_used.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.last_used.append(key)

        return self.cache_data[key]
