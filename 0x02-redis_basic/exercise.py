#!/usr/bin/env python3
"""
a Cache class. In the __init__ method
"""

import redis


class Cache:
    """ Cache class stores instance of the Redic client
    """

    def __init__(self):
        """ Initalizee for Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
