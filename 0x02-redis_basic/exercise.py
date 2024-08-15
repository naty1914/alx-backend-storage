#!/usr/bin/env python3
"""A module that provides a class that implements a caching system"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """It counts the number of times a method is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """It wraps the method"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """It records call history of a method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """It wraps the method"""
        input_key = '{}:inputs'.format(method.__qualname__)
        output_Key = '{}:outputs'.format(method.__qualname__)

        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_Key, str(result))
        return result
    return wrapper


def replay(method: Callable) -> None:
    """It replays the call history of a method"""
    catch_instance = method.__self__
    meth_name = method.__qualname__
    input_key = f'{meth_name}:inputs'
    output_Key = f'{meth_name}:outputs'
    inputs = catch_instance._redis.lrange(input_key, 0, -1)
    outputs = catch_instance._redis.lrange(output_Key, 0, -1)
    print(f"{meth_name} was called {len(inputs)} times:")
    for input, output in zip(inputs, outputs):
        d_output = output.decode('utf-8')
        print('{}(*{}) -> {}'.format(meth_name,
                                     input.decode('utf-8'), d_output))


class Cache:
    """A class that implements a caching system"""
    def __init__(self):
        """It initializes the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """It stores data in the cache and returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,  fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float, None]:
        """It gets data from the cache and returns it"""
        data = self._redis.get(key)
        if data is not None and fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """It gets data from the cache and returns it"""
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: int) -> int:
        """It gets data from the cache and returns it"""
        return self.get(key, lambda data: int(data))
