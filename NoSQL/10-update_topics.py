#!/usr/bin/env python3
"""Changes all topics of a school document based on the name"""


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    :param mongo_collection: pymongo collection object
    :param name: school name to update
    :param topics: list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
