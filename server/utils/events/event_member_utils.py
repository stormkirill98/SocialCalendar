from bson import json_util
from werkzeug.exceptions import abort

from server.database import user_dao
from server.database.events import event_member_dao, group_event_dao


def delete_event_member(member_id):
    member = event_member_dao.get(member_id)

    event = group_event_dao.get(member.event_id)

    user_dao.delete_chat(member.user_id, event.chat_id)
    user_dao.delete_event(member.user_id, event.id)

    event_member_dao.delete(member.id)


def get_event_member(member_id):
    member = event_member_dao.get(member_id)
    if not member:
        return abort(404)

    user = user_dao.get_user(member.user_id)
    if not user:
        return abort(404)

    return json_util.dumps({
        'user_id': user.id,
        'name': user.name,
        'email': user.email,
        'profile_pic': user.profile_pic,
        'member_id': member.id,
        'is_can_invite_user': member.is_can_invite_user,
        'is_can_delete_user': member.is_can_delete_user,
        'is_can_change_event': member.is_can_change_event,
        'is_can_delete_event': member.is_can_delete_event,
        'event_id': member.event_id
    })