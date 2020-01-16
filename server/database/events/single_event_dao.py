from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.database.events import event_dao
from server.entities.events.single_event import SingleEvent

single_event_collection = DB['single_events']


def save(single_event: SingleEvent):
    json = single_event.to_json()
    json.pop('id')

    single_event_id = single_event_collection.insert_one(json).inserted_id
    single_event.set_id(single_event_id)
    return single_event_id


def update(single_event: SingleEvent):
    return event_dao.update(single_event, single_event_collection)


def delete(single_event_id):
    if not id_is_valid(single_event_id):
        return False

    return single_event_collection.delete_one({'_id': ObjectId(single_event_id)}).deleted_count > 0


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
                       json['icon'],
                       json['_id'])


def is_exist(single_event_id):
    if not id_is_valid(single_event_id):
        return False

    return database.is_exist(single_event_id, single_event_collection)
