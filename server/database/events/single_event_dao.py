from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.entities.events.single_event import SingleEvent

single_event_collection = DB['group_events']


def save(single_event):
    json = single_event.to_json()
    json.pop('id')

    single_event_id = single_event_collection.insert_one(json).inserted_id
    single_event.set_id(single_event_id)
    return single_event_id


def delete(single_event_id):
    if not id_is_valid(single_event_id):
        return 0

    return single_event_collection.delete_one({'_id': ObjectId(single_event_id)}).deleted_count


def get(single_event_id):
    if not id_is_valid(single_event_id):
        return None

    json = single_event_collection.find_one({'_id': ObjectId(single_event_id)})
    if json is None:
        return None

    return SingleEvent(json['name'],
                       json['is_private'],
                       json['datetime'],
                       json['address'],
                       json['description'],
                       json['_id'])


def is_exist(single_event_id):
    if not id_is_valid(single_event_id):
        return False

    return database.is_exist(single_event_id, single_event_collection)
