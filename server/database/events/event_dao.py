from bson import ObjectId

from server.database.database import id_is_valid
from server.database.events import group_event_dao, single_event_dao
from server.entities.events.event import Event


def get_event(event_id):
    if group_event_dao.is_exist(event_id):
        return group_event_dao.get(event_id)

    if single_event_dao.is_exist(event_id):
        return single_event_dao.get(event_id)

    return None


def get_events(event_ids):
    if event_ids is None or not isinstance(event_ids, list):
        return []

    event_ids = set(event_ids)

    events = []
    for event_id in event_ids:
        event = get_event(event_id)
        if event is not None:
            events.append(event)

    return events


def update(event: Event, collection):
    if not id_is_valid(event.id):
        return False

    result = collection.update_one({'_id': ObjectId(event.id)},
                                   {'$set': {'name': event.name,
                                             'is_private': event.is_private,
                                             'datetime': event.datetime,
                                             'address': event.address,
                                             'description': event.description}})
    return result.matched_count > 0
