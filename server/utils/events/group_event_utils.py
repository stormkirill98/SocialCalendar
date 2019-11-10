from server.database import user_dao, chat_dao
from server.database.events import group_event_dao, event_member_dao
from server.entities.events.group_events.event_member import EventMember


def add_member(event_id, user_id,
               is_can_invite_user=False,
               is_can_delete_user=False,
               is_can_change_event=False,
               is_can_delete_event=False):
    member = EventMember(event_id, user_id, is_can_invite_user, is_can_delete_user, is_can_change_event,
                         is_can_delete_event)
    member_id = event_member_dao.save(member)
    group_event_dao.add_member(event_id, member_id)

    user_dao.add_event(user_id, event_id)
    chat_id = chat_dao.get_event_chat_by_event_id(event_id)
    user_dao.add_chat(user_id, chat_id)

    return member_id
