import calendar
from datetime import datetime

from bson import json_util
from werkzeug.exceptions import abort

from server.database.events import event_dao, event_member_dao, group_event_dao, single_event_dao
from server.entities.events.event import Event
from server.entities.events.group_events.group_event import GroupEvent
from server.entities.events.single_event import SingleEvent
from server.entities.user import User
from server.enums import EventType
from server.utils import user_utils


def get_event(event_id):
    if event_id is None:
        return abort(400)

    event = event_dao.get_event(event_id)
    if event is None:
        return abort(404)

    return json_util.dumps(event.__dict__)


def get_events(month, year, user: User):
    if user is None or not user.is_authenticated:
        return abort(401)

    if month is None or year is None:
        return abort(400)

    if not month.isdigit() or not year.isdigit():
        return abort(400, {'message': 'Month and year must be number'})

    month = int(month)
    year = int(year)
    if month < 1 or month > 12:
        return abort(400, {'message': 'Month must be number between 1 and 12 inclusive'})

    events: list = event_dao.get_events(user.event_id_list)

    # filter events which contains in require month
    start_date = datetime(year, month, 1)
    end_date = datetime(year,
                        month,
                        calendar.monthrange(year, month)[1],
                        23, 59, 59)
    events = [x for x in events if start_date <= x.datetime <= end_date]

    return json_util.dumps([e.__dict__ for e in events])


def create_event(event_json, user: User):
    if user is None or not user.is_authenticated:
        return abort(401)

    if not valid_event_json(event_json):
        return abort(400)

    event_type = event_json.get('type')

    event_name = event_json.get('name')
    event_is_private = True if event_json.get('is_private') == "true" else False
    event_datetime = datetime.strptime(event_json.get('datetime'), "%d.%m.%Y %H:%M")
    event_address = event_json.get('address')
    event_description = event_json.get('description')
    if event_description is None:
        event_description = ""

    if event_type == EventType.GROUP:
        event = GroupEvent(event_name, event_is_private, event_datetime, event_address, event_description)
        event_id = user_utils.create_group_event(user.id, event)
        return json_util.dumps(event_id)

    if event_type == EventType.SINGLE:
        event = SingleEvent(event_name, event_is_private, event_datetime, event_address, event_description)
        event_id = user_utils.create_single_event(user.id, event)
        return json_util.dumps(event_id)

    return abort(400)


def update_event(event_json, user: User):
    if user is None or not user.is_authenticated:
        return abort(401)

    event_id = event_json.get('id')
    if event_id is None:
        return abort(400)

    event_type = event_json.get('type')
    if not valid_type(event_type):
        return abort(400, "Event type is not valid")

    if event_type == EventType.GROUP:
        # check that user can change event
        event_member = event_member_dao.get_by_user_event(user.id, event_id)
        if event_member is None:
            return abort(404)

        if not event_member.is_can_change_event:
            return abort(403, "User can not change this event")

        # update group event
        event = group_event_dao.get(event_id)
        if event is None:
            # mb wrong type
            return abort(404)

        update_event_fields(event_json, event)

        if not group_event_dao.update(event):
            return abort(500)

    if event_type == EventType.SINGLE:
        event = single_event_dao.get(event_id)
        if event is None:
            # mb wrong type
            return abort(404)

        update_event_fields(event_json, event)

        if not single_event_dao.update(event):
            return abort(500)

    return '', 204


def delete_event(event_id, user):
    if user is None or not user.is_authenticated:
        return abort(401)

    if event_id is None:
        return abort(400)

    if group_event_dao.is_exist(event_id):
        event_member = event_member_dao.get_by_user_event(user.id, event_id)
        if event_member is None:
            return abort(404)

        if not event_member.is_can_delete_event:
            return abort(403, "User can not delete this event")

        if not user_utils.delete_group_event(event_id):
            return abort(500)
    else:
        if single_event_dao.is_exist(event_id):
            if not user_utils.delete_single_event(user.id, event_id):
                return abort(500)
        else:
            # event with this id is not exists in database
            return abort(404)

    return '', 205


def update_event_fields(event_json, event: Event):
    event_name = event_json.get('name')
    event_is_private = event_json.get('is_private')
    event_datetime = event_json.get('datetime')
    event_address = event_json.get('address')
    event_description = event_json.get('description')

    if valid_name(event_name):
        event.name = event_name

    if valid_is_private(event_is_private):
        event.is_private = event_is_private

    if valid_datetime(event_datetime):
        event.datetime = event_datetime

    if valid_address(event_address):
        event.address = event_address

    if event_description is not None:
        event.description = event_description


def valid_event_json(event_json):
    event_type = event_json.get('type')
    if not valid_type(event_type):
        return False

    name = event_json.get('name')
    is_private = event_json.get('is_private')
    event_datetime = event_json.get('datetime')
    address = event_json.get('address')
    # description can be None

    if (not valid_name(name)
            or not valid_is_private(is_private)
            or not valid_datetime(event_datetime)
            or not valid_address(address)):
        return False

    return True


def valid_type(event_type):
    if event_type is None:
        return False

    if event_type != EventType.SINGLE and event_type != EventType.GROUP:
        return False

    return True


def valid_is_private(is_private: str):
    if is_private is None:
        return False

    if is_private != "true" and is_private != "false":
        return False

    return True


def valid_name(name: str):
    return name is not None and len(name) != 0


def valid_address(address: str):
    return address is not None and len(address) != 0


def valid_datetime(event_datetime: datetime):
    if event_datetime is None:
        return False

    return datetime.strptime(event_datetime, "%d.%m.%Y %H:%M") is not None
