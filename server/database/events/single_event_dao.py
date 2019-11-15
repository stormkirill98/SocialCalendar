from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.entities.events.single_event import SingleEvent

single_event_collection = DB['group_events']


def save(single_event: SingleEvent):
    json = single_event.to_json()
    json.pop('id')

    single_event_id = single_event_collection.insert_one(json).inserted_id
    single_event.set_id(single_event_id)
    return single_event_id


def update(single_event: SingleEvent):
    if not id_is_valid(single_event.id):
        return 0

    result = single_event_collection.update_one({'_id': ObjectId(single_event.id)},
                                               {'$set': {'name': single_event.name,
                                                         'is_private': single_event.is_private,
                                                         'datetime': single_event.datetime,
                                                         'address': single_event.address,
                                                         'description': single_event.description}})
    return result.modified_count


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
