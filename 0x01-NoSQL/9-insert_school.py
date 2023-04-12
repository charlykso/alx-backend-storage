#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection based on kwargs
"""

def insert_school(mongo_collection, **kwargs):
    """insert a document and return the new _id"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
