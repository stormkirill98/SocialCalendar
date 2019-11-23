import calendar
from datetime import datetime

from bson import json_util
from werkzeug.exceptions import abort

from server.database.events import event_dao
from server.entities.events.group_events.group_event import GroupEvent
from server.entities.events.single_event import SingleEvent
from server.entities.user import User
from server.enums import EventType
from server.utils import utils, user_utils


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

    if not utils.valid_event_json(event_json):
        return abort(400)

    event_type = event_json['type']

    event_name = event_json['name']
    event_is_private = True if event_json['is_private'] == "true" else False
    event_datetime = datetime.strptime(event_json['datetime'], "%d.%m.%Y %H:%M")
    event_address = event_json['address']
    event_description = event_json['description']
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
