#!/usr/bin/python3
"""LFU Caching module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that inherits from
    BaseCaching and implements a caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.frequency = {}
        self.lru = {}
        self.time = 0

    def put(self, key, item):
        """
        Add an item in the cache.
        If the key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        self.time += 1

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.lru[key] = self.time
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict_least_frequently_used()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.lru[key] = self.time

    def get(self, key):
        """
        Get an item by key from the cache.
        If the key is None or doesn't exist, return None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.time += 1
        self.lru[key] = self.time
        return self.cache_data[key]

    def _evict_least_frequently_used(self):
        """Evict the least frequently used item"""
        min_freq = min(self.frequency.values())
        least_used_keys = [
                k for k, v in self.frequency.items() if v == min_freq
                ]

        if len(least_used_keys) == 1:
            key_to_evict = least_used_keys[0]
        else:
            least_recently_used = {k: self.lru[k] for k in least_used_keys}
            key_to_evict = min(least_recently_used,
                               key=least_recently_used.get)

        del self.cache_data[key_to_evict]
        del self.frequency[key_to_evict]
        del self.lru[key_to_evict]
        print(f"DISCARD: {key_to_evict}")
