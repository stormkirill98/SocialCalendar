from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.entities.user import User

users_collection = DB['users']


def save_user(user: User):
    json = user.to_json()
    json.pop('id')

    user_id = users_collection.insert_one(json).inserted_id
    user.set_id(user_id)
    return user_id


def update_user(user: User):
    if not id_is_valid(user.id):
        return 0

    # result = users_collection.update_one({'_id': ObjectId(user.id)},
    #                                      {'$set': {'nickname': user.nickname,
    #                                                'avatar_url': user.avatar_url}})
    # return result.modified_count


def get_user(user_id):
    if not id_is_valid(user_id):
        return None

    json = users_collection.find_one({'_id': ObjectId(user_id)})
    return create_user_from_json(json)


def get_user_by_google_id(google_id):
    if google_id is None:
        return None

    json = users_collection.find_one({'google_id': google_id})
    return create_user_from_json(json)


def create_user_from_json(json):
    if json is None:
        return None

    return User(json['google_id'],
                json['name'],
                json['email'],
                json['profile_pic'],
                json['birthday'],
                json['_id'],
                json['event_id_list'],
                json['friend_id_list'],
                json['chat_id_list'],
                json['invite_id_list'])


def delete_user(user_id):
    if not id_is_valid(user_id):
        return 0

    return users_collection.delete_one({'_id': ObjectId(user_id)}).deleted_count


def is_exist_by_id(user_id):
    if not id_is_valid(user_id):
        return False

    return database.is_exist(user_id, users_collection)


def is_exist_by_google_id(google_id):
    return users_collection.count_documents({'google_id': google_id}) > 0


def add_event(user_id, event_id):
    if not id_is_valid(user_id) or not id_is_valid(event_id):
        return 0

    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'event_id_list': ObjectId(event_id)}})
    return result.modified_count


def delete_event(user_id, event_id):
    if not id_is_valid(user_id) or not id_is_valid(event_id):
        return 0

    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'event_id_list': ObjectId(event_id)}})
    return result.modified_count


def add_friend(user_id, friend_id):
    if not id_is_valid(user_id) or not id_is_valid(friend_id):
        return 0

    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'friend_id_list': ObjectId(friend_id)}})
    return result.modified_count


def delete_friend(user_id, friend_id):
    if not id_is_valid(user_id) or not id_is_valid(friend_id):
        return 0

    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'friend_id_list': ObjectId(friend_id)}})
    return result.modified_count


def add_chat(user_id, chat_id):
    if not id_is_valid(user_id) or not id_is_valid(chat_id):
        return 0

    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'chat_id_list': ObjectId(chat_id)}})
    return result.modified_count


def delete_chat(user_id, chat_id):
    if not id_is_valid(user_id) or not id_is_valid(chat_id):
        return 0

    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'chat_id_list': ObjectId(chat_id)}})
    return result.modified_count


def add_invite(user_id, invite_id):
    if not id_is_valid(user_id) or not id_is_valid(invite_id):
        return 0

    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$push': {'invite_id_list': ObjectId(invite_id)}})
    return result.modified_count


def delete_invite(user_id, invite_id):
    if not id_is_valid(user_id) or not id_is_valid(invite_id):
        return 0

    result = users_collection.update_one({'_id': ObjectId(user_id)},
                                         {'$pull': {'invite_id_list': ObjectId(invite_id)}})
    return result.modified_count
