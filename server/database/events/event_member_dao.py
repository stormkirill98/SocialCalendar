from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.entities.events.group_events.event_member import EventMember

event_member_collection = DB['event_members']


def save(event_member: EventMember):
    json = event_member.to_json()
    json.pop('id')

    event_member_id = event_member_collection.insert_one(json).inserted_id
    event_member.set_id(event_member_id)
    return event_member_id


def delete(event_member_id):
    if not id_is_valid(event_member_id):
        return False

    return event_member_collection.delete_one({'_id': ObjectId(event_member_id)}).deleted_count > 0


def get(event_member_id):
    json = event_member_collection.find_one({'_id': ObjectId(event_member_id)})

    return create_event_from_json(json)


def get_by_user_event(user_id, event_id):
    if not id_is_valid(user_id) or not id_is_valid(event_id):
        return None

    json = event_member_collection.find_one({'user_id': ObjectId(user_id),
                                             'event_id': ObjectId(event_id)})

    return create_event_from_json(json)


def set_can_invite_user(group_event_id, is_can_invite_user):
    if not id_is_valid(group_event_id):
        return 0

    result = event_member_collection.update_one({'_id': ObjectId(group_event_id)},
                                                {'$set': {'is_can_invite_user': is_can_invite_user}})
    return result.matched_count


def set_can_delete_user(group_event_id, is_can_delete_user):
    if not id_is_valid(group_event_id):
        return 0

    result = event_member_collection.update_one({'_id': ObjectId(group_event_id)},
                                                {'$set': {'is_can_delete_user': is_can_delete_user}})
    return result.matched_count


def set_can_change_event(group_event_id, is_can_change_event):
    if not id_is_valid(group_event_id):
        return 0

    result = event_member_collection.update_one({'_id': ObjectId(group_event_id)},
                                                {'$set': {'is_can_change_event': is_can_change_event}})
    return result.matched_count


def set_can_delete_event(group_event_id, is_can_delete_event):
    if not id_is_valid(group_event_id):
        return 0

    result = event_member_collection.update_one({'_id': ObjectId(group_event_id)},
                                                {'$set': {'is_can_delete_event': is_can_delete_event}})
    return result.matched_count


def create_event_from_json(json):
    if json is None:
        return None

    return EventMember(json['event_id'],
                       json['user_id'],
                       json['is_can_invite_user'],
                       json['is_can_delete_user'],
                       json['is_can_change_event'],
                       json['is_can_delete_event'],
                       json['_id'])


def is_exists(event_member_id):
    return database.is_exist(event_member_id, event_member_collection)
