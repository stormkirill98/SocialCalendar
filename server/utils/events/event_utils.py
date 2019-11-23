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
    if month < 0 or month > 11:
        return abort(400, {'message': 'Month must be number between 0 and 11 inclusive'})

    events: list = event_dao.get_events(user.event_id_list)

    return json_util.dumps([e.__dict__ for e in events])
