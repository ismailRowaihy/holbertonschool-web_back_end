""""""
import pymongo


def list_all(mongo_collection):
    data = list(mongo_collection.find())
    if len(data) == 0:
        return []
    return data

