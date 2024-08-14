#!/usr/bin/env python3
""" A module that provides a function that lists all documents
in the collection """


def list_all(mongo_collection):
    """It lists all documents in the collection"""
    return list(mongo_collection.find())
