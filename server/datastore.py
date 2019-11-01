from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@socialcalendar-kjwvs.gcp.mongodb.net/test?retryWrites=true&w=majority")
database = client.database

users_collection = database['users']


def save_user(user):
    id = users_collection.insert_one(user.__dict__).inserted_id
    user.set_id(str(id))
    return user
