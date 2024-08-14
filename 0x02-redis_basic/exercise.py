#!/usr/bin/env python3
from typing import Union
import redis
import uuid
"""
This module is to store an instance of redis db and store data in it
executor is main.py
"""


class Cache:
    """
    This class is to store an instance of redis db and store data in it
    """
    _redis = redis.Redis()

    def __init__(self) -> None:
        """
        This is the initializer for the class
        _redis - redis client that connects redis db to python commands
        .flushdb() - makes each instance of the class have an empty redis db
        """
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        This method stores data in the redis db using a random key to a value
        The key is stored in the redis db and allocated the data value
        """
        key = str(uuid.uuid4())
        # sets the key to the data value in the redis db
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        """
        This function takes a key, and optional function to convert the data.
        It returns the data stored in the key, or None if the key is not found
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key):
        " This calls the get method with a predefined conversion to str"
        return self.get(key, str)

    def get_int(self, key):
        "This calls the get method with a predefined conversion to int"
        return self.get(key, int)
