#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

# cache2 = Cache()

# TEST_CASES = {
#     b"foo": None,
#     123: int,
#     "bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASES.items():
#     key = cache2.store(value)
#     if (cache2.get(key, fn=fn) == value):
#         print("true")
#     else:
#         print("false")


# cache3= Cache()

# cache3.store(b"first")
# print(cache3.get(cache3.store.__qualname__))

# cache3.store(b"second")
# cache3.store(b"third")
# print(cache3.get(cache3.store.__qualname__))