from bson import ObjectId

from server.datastore.datastore import database
from shared.entities.user import User

users_collection = database['users']


def insert_user(user):
    id = users_collection.insert_one(user.to_json()).inserted_id
    user.set_id(str(id))
    return user


def get_user(id):
    user_json = users_collection.find_one({'_id': ObjectId(id)})
    user = User(user_json['login'],
                user_json['password'],
                user_json['nickname'],
                user_json['avatar_url'],
                user_json['birthday'],
                str(user_json['_id']),
                user_json['event_id_list'],
                user_json['friend_id_list'],
                user_json['chat_id_list'])
    return user


def delete_user(id):
    return users_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def add_event(user_id, event_id):
    users_collection.update_one({'_id': ObjectId(user_id)}, {'$push': {'event_id_list': event_id}})
