#!/usr/bin/env python3
"""Lists all documents in a collection."""


from pymongo import MongoClient


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: pymongo collection object
    :return: list of documents in the
    collection or an empty list if no documents
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
