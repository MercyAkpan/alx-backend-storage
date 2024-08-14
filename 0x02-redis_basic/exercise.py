#!/usr/bin/env/python3
from typing import Union
import redis
import uuid
"""
This module is to store an instance of redis db and store data in it
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
