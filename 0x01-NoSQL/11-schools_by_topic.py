#!/usr/bin/env python3
""" A module that lists all documents in the collection """


def schools_by_topic(mongo_collection, topic):
    """It lists all documents in the collection"""
    filter = {"topics": {'$elemMatch': {'$eq': topic}}}
    return [document for document in mongo_collection.find(filter)]
