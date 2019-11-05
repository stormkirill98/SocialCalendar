from server.datastore import invite_dao, user_dao
from server.enums import InviteType
from server.utils.events import group_event_utils


def accept_invite(user_id, invite_id):
    invite = invite_dao.get_invite(invite_id)

    if invite.type == InviteType.FRIEND:
        user_dao.add_friend(user_id, invite.sender_id)
        user_dao.add_friend(invite.sender_id, user_id)
    else:
        user_dao.add_chat(user_id, invite.place_id)
        group_event_utils.add_member_to_group_event(user_id, invite.place_id)

    invite_dao.delete_invite(invite_id)
