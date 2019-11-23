from datetime import datetime

from server.enums import EventType


def valid_event_json(event_json):
    event_type = event_json['type']
    if event_type is None:
        return False

    if event_type != EventType.SINGLE and event_type != EventType.GROUP:
        return False

    name = event_json['name']
    is_private = event_json['is_private']
    event_datetime = event_json['datetime']
    address = event_json['address']
    # description can be None

    if (name is None
            or is_private is None
            or event_datetime is None
            or address is None):
        return False

    if len(name) == 0:
        return False

    if is_private != "true" and is_private != "false":
        return False

    if datetime.strptime(event_json['datetime'], "%d.%m.%Y %H:%M") is None:
        return False

    if len(address) == 0:
        return False

    return True
