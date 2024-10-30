#!/usr/bin/env python3
""" LIFO caching """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """

    def __init__(self):
        """init method"""
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """put method"""
        if item is not None and key is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                removed = self.key_indexes.pop()
                del self.cache_data[removed]
                print("DISCARD: {}".format(removed))

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
