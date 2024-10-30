#!/usr/bin/env python3
""" FIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """init method"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """put method"""
        if item is not None and key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
