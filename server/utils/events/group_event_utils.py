from server.datastore.events import group_event_dao, event_member_dao
from server.entities.events.group_events.event_member import EventMember


def add_member(user_id, event_id):
    event_member = EventMember(event_id, user_id)
    member_id = event_member_dao.save(event_member)
    group_event_dao.add_member(event_id, member_id)
