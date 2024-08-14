#!/usr/bin/env python3
""" A module that provides a function that lists all documents
in the collection """


def update_topics(mongo_collection, name, topics):
    """It updates a document in the collection"""
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
