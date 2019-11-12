from bson import ObjectId

from server.database.database import DB, id_is_valid
from server.entities.events.single_event import SingleEvent

single_event_collection = DB['group_events']


def save(single_event):
    json = single_event.to_json()
    json.pop('id')

    id = single_event_collection.insert_one(json).inserted_id
    single_event.set_id(id)
    return id


def delete(id):
    if not id_is_valid(id):
        return 0

    return single_event_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def get(id):
    if not id_is_valid(id):
        return None

    json = single_event_collection.find_one({'_id': ObjectId(id)})
    if json is None:
        return None

    return SingleEvent(json['name'],
                       json['is_private'],
                       json['datetime'],
                       json['address'],
                       json['description'],
                       json['_id'])
