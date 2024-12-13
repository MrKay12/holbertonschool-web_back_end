#!/usr/bin/env python3
"""Returns the list of schools having a specific topic."""


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    :param mongo_collection: pymongo collection object
    :param topic: topic searched
    :return: list of schools with the specific topic
    """
    return list(mongo_collection.find({"topics": topic}))
