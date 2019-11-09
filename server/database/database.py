import bson
from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@socialcalendar-kjwvs.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.database


# TODO check all id on validate in dao classes
def id_is_valid(id):
    return bson.objectid.ObjectId.is_valid(id)
