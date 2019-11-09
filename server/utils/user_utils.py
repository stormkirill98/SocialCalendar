from datetime import datetime

from server.database import invite_dao, user_dao, msg_dao, chat_dao
from server.entities.chats.inner_classes.message import Message
from server.entities.invite import Invite
from server.enums import InviteType, ChatType
from server.utils.events import group_event_utils


def accept_invite(invite_id):
    invite = invite_dao.get_invite(invite_id)

    if invite.type == InviteType.FRIEND:
        # invite to friend
        user_dao.add_friend(invite.receiver_id, invite.sender_id)
        user_dao.add_friend(invite.sender_id, invite.receiver_id)
    else:
        # invite to event
        user_dao.add_event(invite.receiver_id, invite.event_id)
        group_event_utils.add_member(invite.receiver_id, invite.event_id)

    invite_dao.delete_invite(invite_id)
    user_dao.delete_invite(invite.receiver_id, invite_id)


# TODO cancel_invite(invite_id)

# not test
def send_msg(user_id, chat_id, chat_type, msg_text):
    msg = Message(user_id, chat_id, datetime.today(), msg_text)
    msg_id = msg_dao.save_msg(msg)
    if chat_type == ChatType.DIALOG:
        chat_dao.add_msg_to_dialog(chat_id, msg_id)
    else:
        chat_dao.add_msg_to_event_chat(chat_id, msg_id)


def send_invite(user_id, receiver_id, invite_type, event_id=""):
    invite = Invite(user_id, receiver_id, invite_type, event_id)
    invite_id = invite_dao.save_invite(invite)
    user_dao.add_invite(receiver_id, invite_id)
    return invite_id
