from bson import ObjectId

from server.database.database import db
from server.entities.events.group_events.group_event import GroupEvent

group_event_collection = db['group_events']


def save(group_event):
    json = group_event.to_json()
    json.pop('id')

    id = group_event_collection.insert_one(json).inserted_id
    group_event.set_id(id)
    return id


def delete(id):
    return group_event_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def get(id):
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
    result = group_event_collection.update_one({'_id': ObjectId(group_event_id)},
                                               {'$push': {'member_id_list': ObjectId(member_id)}})
    return result.modified_count


def delete_member(group_event_id, member_id):
    result = group_event_collection.update_one({'_id': ObjectId(group_event_id)},
                                               {'$pull': {'member_id_list': ObjectId(member_id)}})
    return result.modified_count


def set_chat_id(group_event_id, chat_id):
    result = group_event_collection.update_one({'_id': ObjectId(group_event_id)},
                                               {'$set': {'chat_id': ObjectId(chat_id)}})
    return result.modified_count
