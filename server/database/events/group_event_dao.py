from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.entities.events.group_events.group_event import GroupEvent

group_event_collection = DB['group_events']


def save(group_event):
    json = group_event.to_json()
    json.pop('id')

    id = group_event_collection.insert_one(json).inserted_id
    group_event.set_id(id)
    return id


def delete(id):
    if not id_is_valid(id):
        return 0

    return group_event_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def get(id):
    if not id_is_valid(id):
        return None

    json = group_event_collection.find_one({'_id': ObjectId(id)})
    if json is None:
        return None

    return GroupEvent(json['name'],
                      json['is_private'],
                      json['datetime'],
                      json['address'],
                      json['description'],
                      json['member_id_list'],
                      json['chat_id'],
                      json['_id'])


def add_member(group_event_id, member_id):
    if not id_is_valid(group_event_id) or not id_is_valid(member_id):
        return 0

    result = group_event_collection.update_one({'_id': ObjectId(group_event_id)},
                                               {'$push': {'member_id_list': ObjectId(member_id)}})
    return result.modified_count


def delete_member(group_event_id, member_id):
    if not id_is_valid(group_event_id) or not id_is_valid(member_id):
        return 0

    result = group_event_collection.update_one({'_id': ObjectId(group_event_id)},
                                               {'$pull': {'member_id_list': ObjectId(member_id)}})
    return result.modified_count


def set_chat_id(group_event_id, chat_id):
    if not id_is_valid(group_event_id) or not id_is_valid(chat_id):
        return 0

    result = group_event_collection.update_one({'_id': ObjectId(group_event_id)},
                                               {'$set': {'chat_id': ObjectId(chat_id)}})
    return result.modified_count


def is_exists(id):
    if not id_is_valid(id):
        return False

    return database.is_exist(id, group_event_collection)
