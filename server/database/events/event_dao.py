from server.database.events import group_event_dao, single_event_dao


def get_event(event_id):
    if group_event_dao.is_exists(event_id):
        return group_event_dao.get(event_id)

    if single_event_dao.is_exist(event_id):
        return single_event_dao.get(event_id)

    return None


def get_events(event_ids):
    if event_ids is None or not isinstance(event_ids, list):
        return []

    events = []
    for event_id in event_ids:
        event = get_event(event_id)
        if event is not None:
            events.append(event)

    return events
