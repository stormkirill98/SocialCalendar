import bson
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@socialcalendar-kjwvs.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.database


# TODO check all id on validate in dao classes
# TODO check all json in getters in dao classes
def id_is_valid(id):
    return bson.objectid.ObjectId.is_valid(id)


def is_exist(id, collection):
    if not id_is_valid(id):
        return False

    return collection.count_documents({'_id': ObjectId(id)}) > 0