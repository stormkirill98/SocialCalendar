from bson import ObjectId

from server.database import database
from server.database.database import db, id_is_valid
from server.entities.user import User

users_collection = db['users']


def save_user(user):
    json = user.to_json()
    json.pop('id')

    id = users_collection.insert_one(json).inserted_id
    user.set_id(id)
    return id


def get_user(id):
    json = users_collection.find_one({'_id': ObjectId(id)})
    if json is None:
        return None

    return User(json['login'],
                json['password'],
                json['nickname'],
                json['avatar_url'],
                json['birthday'],
                json['_id'],
                json['event_id_list'],
                json['friend_id_list'],
                json['chat_id_list'],
                json['invite_id_list'])


def delete_user(id):
    return users_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def is_exists(id):
    return database.is_exist(id, users_collection)


def add_event(user_id, event_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'event_id_list': ObjectId(event_id)}})
    return result.modified_count


def delete_event(user_id, event_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'event_id_list': ObjectId(event_id)}})
    return result.modified_count


def add_friend(user_id, friend_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'friend_id_list': ObjectId(friend_id)}})
    return result.modified_count


def delete_friend(user_id, friend_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'friend_id_list': ObjectId(friend_id)}})
    return result.modified_count


def add_chat(user_id, chat_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'chat_id_list': ObjectId(chat_id)}})
    return result.modified_count


def delete_chat(user_id, chat_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'chat_id_list': ObjectId(chat_id)}})
    return result.modified_count


def add_invite(user_id, invite_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'invite_id_list': ObjectId(invite_id)}})
    return result.modified_count


def delete_invite(user_id, invite_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'invite_id_list': ObjectId(invite_id)}})
    return result.modified_count
