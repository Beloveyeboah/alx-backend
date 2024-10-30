#!/usr/bin/python3

"""
Create a class BasicCache that inherits from BaseCaching
"""


class BaseCaching:
    """BaseCaching class"""
    def __init__(self):
        self.cache_data = {}

    def print_cache(self):
        """Print the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data[key]))


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, do nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key from the cache.
        If the key is None or doesn't exist, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
