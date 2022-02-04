#!/usr/bin/env python3
"""
Implementation of a basic caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        Child class that implements the caching with a pair key/value algorithm
    """

    def put(self, key, value):
        """Insert a value in the caching system"""
        if not key or not value:
            return

        self.cache_data[key] = value

    def get(self, key):
        """Retrieve a value from the caching system"""
        if not key:
            return None

        return self.cache_data.get(key)
