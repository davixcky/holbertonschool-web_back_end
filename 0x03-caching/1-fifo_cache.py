#!/usr/bin/env python3
"""
Implementation of a basic caching system with FIFO
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
        Child class that implements the caching with a pair
        key/value algorithm (FIFO)
    """

    def put(self, key, value):
        """Insert a value in the caching system"""
        if not key or not value:
            return

        keys = self.cache_data.keys()
        if len(keys) == BaseCaching.MAX_ITEMS:
            temp_key = list(keys)[0]
            del self.cache_data[temp_key]
            print('DISCARD: {}'.format(temp_key))

        self.cache_data[key] = value

    def get(self, key):
        """Retrieve a value from the caching system"""
        if not key:
            return None

        return self.cache_data.get(key)
