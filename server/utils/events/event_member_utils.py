from server.database import user_dao
from server.database.events import event_member_dao, group_event_dao


def delete_event_member(member_id):
    member = event_member_dao.get(member_id)

    event = group_event_dao.get(member.event_id)

    user_dao.delete_chat(member.user_id, event.chat_id)
    user_dao.delete_event(member.user_id, event.id)

    event_member_dao.delete(member.id)
