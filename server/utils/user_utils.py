import re
from datetime import datetime

from server.database import invite_dao, user_dao, msg_dao, chat_dao
from server.database.events import group_event_dao, event_member_dao, single_event_dao
from server.entities.chats.inner_classes.message import Message
from server.entities.events.group_events.event_member import EventMember
from server.entities.events.group_events.group_event import GroupEvent
from server.entities.events.single_event import SingleEvent
from server.entities.invite import Invite
from server.enums import InviteType, ChatType
from server.utils.chats import event_chat_utils
from server.utils.events import group_event_utils, event_member_utils


def send_invite(user_id, receiver_id, invite_type, event_id=""):
    invite = Invite(user_id, receiver_id, invite_type, event_id)
    invite_id = invite_dao.save_invite(invite)
    user_dao.add_invite(receiver_id, invite_id)
    return invite_id


def accept_invite(invite_id):
    invite = invite_dao.get_invite(invite_id)

    if invite.type == InviteType.FRIEND:
        # invite to friend
        user_dao.add_friend(invite.receiver_id, invite.sender_id)
        user_dao.add_friend(invite.sender_id, invite.receiver_id)
    else:
        # invite to event
        user_dao.add_event(invite.receiver_id, invite.event_id)
        group_event_utils.add_member(invite.event_id, invite.receiver_id)

    invite_dao.delete_invite(invite_id)
    user_dao.delete_invite(invite.receiver_id, invite_id)


def decline_invite(invite_id):
    invite = invite_dao.get_invite(invite_id)
    invite_dao.delete_invite(invite_id)
    user_dao.delete_invite(invite.receiver_id, invite_id)


def create_group_event(user_id, group_event: GroupEvent):
    group_event_dao.save(group_event)

    # add user which create this event to event
    member = EventMember(group_event.id, user_id, True, True, True, True)
    event_member_dao.save(member)

    group_event.add_member(member.id)
    group_event_dao.add_member(group_event.id, member.id)

    # create chat for this event
    chat_id = event_chat_utils.create_event_chat(group_event.id)
    group_event_dao.set_chat_id(group_event.id, chat_id)

    user_dao.add_event(user_id, group_event.id)
    user_dao.add_chat(user_id, chat_id)

    return group_event.id


def delete_group_event(removing_member_id, group_event_id):
    """delete event by id
    :return True if event was delete
    :return False if event wasn't delete
    """
    # check that member can delete this event
    removing_member = event_member_dao.get(removing_member_id)
    if not removing_member.is_can_delete_event:
        return False

    group_event = group_event_dao.get(group_event_id)

    # delete members
    for member_id in group_event.member_id_list:
        event_member_utils.delete_event_member(member_id)

    # delete chat
    event_chat_utils.delete_event_chat(group_event.chat_id)

    group_event_dao.delete(group_event_id)
    return True


def leave_group_event(leaving_member_id, group_event_id):
    group_event = group_event_dao.get(group_event_id)

    # delete event if this member is last
    if len(group_event.member_id_list) == 1:
        delete_group_event(leaving_member_id, group_event_id)
        return

    leaving_member = event_member_dao.get(leaving_member_id)

    group_event_dao.delete_member(group_event_id, leaving_member_id)

    user_dao.delete_chat(leaving_member.user_id, group_event.chat_id)
    user_dao.delete_event(leaving_member.user_id, group_event.id)

    event_member_dao.delete(leaving_member.id)


def create_single_event(user_id, single_event: SingleEvent):
    single_event_dao.save(single_event)
    user_dao.add_event(user_id, single_event.id)

    return single_event.id


def delete_single_event(user_id, single_event_id):
    user_dao.delete_event(user_id, single_event_id)
    single_event_dao.delete(single_event_id)


# not tested
def send_msg(user_id, chat_id, chat_type, msg_text):
    msg = Message(user_id, chat_id, datetime.today(), msg_text)
    msg_id = msg_dao.save_msg(msg)
    if chat_type == ChatType.DIALOG:
        chat_dao.add_msg_to_dialog(chat_id, msg_id)
    else:
        chat_dao.add_msg_to_event_chat(chat_id, msg_id)


# not tested
def search_users(filtered_str: str):
    """Does search by searched field which contain name and email"""

    regx = re.compile('.*' + filtered_str + '.*', re.IGNORECASE)

    users = user_dao.get_filtered_users(regx)
    if users is None:
        return list()
    else:
        return list(users)
