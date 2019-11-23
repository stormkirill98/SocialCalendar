import calendar

from datetime import datetime

from bson import json_util
from werkzeug.exceptions import abort

from server.database.events import event_dao
from server.entities.user import User


def get_events(month, year, user: User):
    if user is None or not user.is_authenticated:
        return abort(401)

    if month is None or year is None:
        return abort(400)

    if not month.isdigit() or not year.isdigit():
        return abort(400, {'message': 'Month and must be number'})

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
