#!/usr/bin/env python3
from typing import Union
import redis
import uuid
from functools import wraps
"""
This module is to store an instance of redis db and store data in it
executor is main.py
"""

def count_calls(method):
    @wraps(method)
    # Method is the decorated function.
        # The args and kwargs is for the method to be called,
        # it consists of arguments
    def wrapper(self, *args, **kwargs):
        # This creates a unique name all instance of a class -- a GLOBAL KEY 
        # "that calls this method share."
        # NT: it doesnt use self as "self" creates instance attibutes
        # and we need a local variable all instances of same class, same method
        # can relate to -- It is also more striaghtforward.
        key = method.__qualname__ 
        # This uses self to access the _redis connection specific to that 
        # Cache class instance, and since "key" is same for all instances, 
        # incrementaion occurs globally. 
        self._redis.incr(key)
        # Returns or applies the actual method passed.
        return method(self, *args, **kwargs)
    return wrapper

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
    @count_calls # This decorates the store function with count_calls decorators.
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
