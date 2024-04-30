#!/usr/bin/env python3
"""
    lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    mango_list = []

    for document in mongo_collection.find():
        mango_list.append(document)

    return mango_list
