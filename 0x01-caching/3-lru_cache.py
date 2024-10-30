#!/usr/bin/python3
"""LRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache class"""

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            discard = self.order.pop(0)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
