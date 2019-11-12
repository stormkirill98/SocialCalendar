from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.entities.events.group_events.event_member import EventMember

event_member_collection = DB['event_members']


def save(event_member):
    json = event_member.to_json()
    json.pop('id')

    id = event_member_collection.insert_one(json).inserted_id
    event_member.set_id(id)
    return id


def delete(id):
    if not id_is_valid(id):
        return 0

    return event_member_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def get(id):
    json = event_member_collection.find_one({'_id': ObjectId(id)})

    return create_event_from_json(json)


def get_by_user_event(user_id, event_id):
    json = event_member_collection.find_one({'user_id': ObjectId(user_id),
                                             'event_id': ObjectId(event_id)})

    return create_event_from_json(json)


# TODO create setters for permissions

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


def is_exists(id):
    return database.is_exist(id, event_member_collection)
