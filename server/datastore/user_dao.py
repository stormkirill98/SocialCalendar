from bson import ObjectId

from server.datastore.datastore import database
from shared.entities.user import User

users_collection = database['users']


def save_user(user):
    id = users_collection.insert_one(user.__dict__).inserted_id
    user.set_id(str(id))
    return user


def get_user(user_id):
    user_json = users_collection.find_one({'_id': ObjectId(user_id)})
    user = User(user_json['login'],
                user_json['password'],
                user_json['nickname'],
                user_json['avatar_url'],
                user_json['birthday'],
                str(user_json['_id']))
    return user
