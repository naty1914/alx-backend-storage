#!/usr/bin/env python3
""" A module that provides a class that implements a caching system"""
import redis
import requests
from functools import wraps
from typing import Callable
r = redis.Redis()


def web_cache(method: Callable) -> Callable:
    """It caches web requests"""
    @wraps(method)
    def wrapper(url):
        """It wraps the method"""
        cached_web = "catched:" + url
        result = r.get(cached_web)
        if result:
            return result.decode('utf-8')
        key = "count:" + url
        data = method(url)
        r.incr(key)
        r.setex(cached_web, 10, data)
        return data
    return wrapper


@web_cache
def get_page(url: str) -> str:
    """It gets a web page"""
    resp = requests.get(url)
    return resp.text
