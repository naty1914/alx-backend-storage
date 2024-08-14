#!/usr/bin/env python3
""" A module that provides a function that lists all documents"""


def top_students(mongo_collection):
    """It lists all documents in the collection"""
    result = mongo_collection.aggregate(
        [
           {        
               '$project':
               {
                   '_id': 1,
                   'name': 1,
                   'averageScore':
                   {
                       '$avg':
                       {
                           '$avg': '$topics.score',
                       },
                   },
                   'topics': 1,
               },
           },
           {
               '$sort': {'averageScore': -1},
           },
        ]
    )
    return result
