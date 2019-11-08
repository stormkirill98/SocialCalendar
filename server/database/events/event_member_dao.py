from bson import ObjectId

from server.database.database import database
from server.entities.events.group_events.event_member import EventMember

event_member_collection = database['event_members']


def save(event_member):
    json = event_member.to_json()
    json.pop('id')

    id = event_member_collection.insert_one(json).inserted_id
    event_member.set_id(id)
    return id


def delete(id):
    return event_member_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def get(id):
    json = event_member_collection.find_one({'_id': ObjectId(id)})
    return EventMember(json['chat_id'],
                       json['user_id'],
                       json['is_can_invite_user'],
                       json['is_can_delete_user'],
                       json['is_can_change_event'],
                       json['id'])
