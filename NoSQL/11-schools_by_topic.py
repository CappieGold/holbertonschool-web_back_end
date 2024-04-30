#!/usr/bin/env python3
"""
    returns the list of school having a specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
        mongo_collection will be the pymongo collection object
        topic (string) will be topic searched
    """
    results = []

    for result in mongo_collection.find({"topics": topic}):
        results.append(result)
    return results
