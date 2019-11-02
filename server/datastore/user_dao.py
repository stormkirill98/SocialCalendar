from bson import ObjectId

from server.datastore.datastore import database
from server.entities.user import User

users_collection = database['users']


def save_user(user):
    json = user.to_json()
    json.pop('id')
    id = users_collection.insert_one(json).inserted_id
    user.set_id(str(id))
    return user


def get_user(id):
    saved_user = users_collection.find_one({'_id': ObjectId(id)})
    return User(saved_user['login'],
                saved_user['password'],
                saved_user['nickname'],
                saved_user['avatar_url'],
                saved_user['birthday'],
                str(saved_user['_id']),
                saved_user['event_id_list'],
                saved_user['friend_id_list'],
                saved_user['chat_id_list'])


def delete_user(id):
    return users_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def is_exists(id):
    return users_collection.find({'_id': ObjectId(id)}).count() > 0


def add_event(user_id, event_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'event_id_list': event_id}})
    return result.modified_count


def delete_event(user_id, event_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'event_id_list': event_id}})
    return result.modified_count


def add_friend(user_id, friend_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'friend_id_list': friend_id}})
    return result.modified_count


def delete_friend(user_id, friend_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'friend_id_list': friend_id}})
    return result.modified_count


def add_chat(user_id, chat_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'chat_id_list': chat_id}})
    return result.modified_count


def delete_chat(user_id, chat_id):
    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'chat_id_list': chat_id}})
    return result.modified_count
