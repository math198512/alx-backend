#!/usr/bin/env python3
""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """

    def put(self, key, item):
        """put method"""
        if item is not None and key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get method"""
        return self.cache_data[key]
