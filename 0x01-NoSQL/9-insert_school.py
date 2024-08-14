#!/usr/bin/env python3
""" A module that provides a function that lists all documents
in the collection"""


def insert_school(mongo_collection, **kwargs):
    """It inserts a new document in the collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
