#!/usr/bin/python3
"""0-basic_cache"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache Class"""

    def put(self, key, item):
        """put function"""
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
