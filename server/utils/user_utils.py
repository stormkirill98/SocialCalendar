import re

from bson import json_util
from werkzeug.exceptions import abort

from server.database import invite_dao, user_dao
from server.database.database import id_is_valid
from server.database.events import group_event_dao, event_member_dao, single_event_dao
from server.entities.events.group_events.event_member import EventMember
from server.entities.events.group_events.group_event import GroupEvent
from server.entities.events.single_event import SingleEvent
from server.entities.invite import Invite
from server.entities.user import User
from server.enums import InviteType
from server.utils.chats import event_chat_utils, dialog_utils
from server.utils.events import group_event_utils, event_member_utils


def send_invite(request_json, user: User):
    # TODO check that this invite not exist

    if request_json is None:
        return abort(400)

    invite_type = request_json.get('type')

    receiver_id = request_json.get('receiver_id')
    if receiver_id == str(user.id):
        return abort(400)

    event_id = request_json.get('event_id')
    if event_id is None:
        if invite_type == InviteType.EVENT:
            return abort(400)

        event_id = ""

    if not valid_invite_type(invite_type):
        return abort(400)

    if receiver_id is None or not id_is_valid(receiver_id):
        return abort(400)

    if event_id != "":
        if event_id is None or not id_is_valid(event_id):
            return abort(400)

        # check that user can send invite to this event
        event_member = event_member_dao.get_by_user_event(user.id, event_id)
        if event_member is None:
            return abort(404)

        if not event_member.is_can_invite_user:
            return abort(403)

    invite = Invite(user.id, receiver_id, invite_type, event_id)
    invite_id = invite_dao.save_invite(invite)
    user_dao.add_invite(receiver_id, invite_id)
    return '', 204


def handle_invite(invite_id, action, user: User):
    if not id_is_valid(invite_id):
        return abort(400)

    if action != "accept" and action != "decline":
        return abort(400)

    invite = invite_dao.get_invite(invite_id)
    if invite is None:
        return abort(404)

    # this invite send not this user
    if str(user.id) != str(invite.receiver_id):
        return abort(403)

    if action == "accept":
        accept_invite(invite)
    else:
        decline_invite(invite)

    return '', 204


def accept_invite(invite):
    if invite.type == InviteType.FRIEND:
        # invite to friend
        user_dao.add_friend(invite.receiver_id, invite.sender_id)
        user_dao.add_friend(invite.sender_id, invite.receiver_id)
        dialog_utils.create_dialog(invite.receiver_id, invite.sender_id)
    else:
        # invite to event
        user_dao.add_event(invite.receiver_id, invite.event_id)
        group_event_utils.add_member(invite.event_id, invite.receiver_id)

    invite_dao.delete_invite(invite.id)
    user_dao.delete_invite(invite.receiver_id, invite.id)


def decline_invite(invite):
    invite_dao.delete_invite(invite.id)
    user_dao.delete_invite(invite.receiver_id, invite.id)


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


def delete_group_event(group_event_id):
    """delete event by id
    :return True if event was delete
    :return False if event wasn't delete
    """
    group_event = group_event_dao.get(group_event_id)
    if group_event is None:
        return False

    # delete members
    for member_id in group_event.member_id_list:
        event_member_utils.delete_event_member(member_id)

    # delete chat
    event_chat_utils.delete_event_chat(group_event.chat_id)

    return group_event_dao.delete(group_event_id)


def leave_group_event(group_event_id, user: User):
    if group_event_id is None or not id_is_valid(group_event_id):
        return abort(400)

    group_event = group_event_dao.get(group_event_id)
    if group_event is None:
        return abort(404, "Group event is not found")

    event_member = event_member_dao.get_by_user_event(user.id, group_event_id)
    if event_member is None:
        return abort(404, "Event member is not found")

    # delete event if this member is last
    if len(group_event.member_id_list) == 1:
        if delete_group_event(group_event_id):
            return '', 204
        else:
            return abort(500, "Group event was not delete")

    if not group_event_dao.delete_member(group_event_id, event_member.id):
        return abort(500, "Event member was not delete from event")

    if not user_dao.delete_chat(event_member.user_id, group_event.chat_id):
        return abort(500, "Chat was not delete from user")
    if not user_dao.delete_event(event_member.user_id, group_event.id):
        return abort(500, "Event was not delete from user")

    event_member_dao.delete(event_member.id)
    return '', 204


def create_single_event(user_id, single_event: SingleEvent):
    single_event_dao.save(single_event)
    user_dao.add_event(user_id, single_event.id)

    return single_event.id


def delete_single_event(user_id, single_event_id):
    user_dao.delete_event(user_id, single_event_id)
    return single_event_dao.delete(single_event_id)


def search_users(filtered_str: str):
    """Search by searched field which contain name and email"""

    if filtered_str is None or len(filtered_str) == 0:
        return abort(400)

    regx = re.compile('.*' + filtered_str + '.*', re.IGNORECASE)

    users = user_dao.get_filtered_users(regx)
    users = list(users)

    if users is None:
        return '', 204

    return json_util.dumps(users), 200


def get_friends(user: User):
    friend_list = []

    for friend_id in user.friend_id_list:
        friend = user_dao.get_user(friend_id)
        if friend is None:
            continue

        friend_list.append(friend.to_overview_friend_json())

    if len(friend_list) == 0:
        return '', 204

    return json_util.dumps(friend_list), 200


def remove_friend(friend_id, user: User):
    if friend_id is None or not id_is_valid(friend_id):
        return abort(400)

    friend = user_dao.get_user(friend_id)
    if friend is None:
        return abort(404)

    success_delete_friends = user_dao.delete_friend(user.id, friend_id)
    if not user_dao.delete_friend(friend_id, user.id):
        success_delete_friends = False

    if not success_delete_friends:
        return abort(500)

    return '', 204


def get_friend(friend_id):
    if friend_id is None or not id_is_valid(friend_id):
        return abort(400)

    friend = user_dao.get_user(friend_id)
    if friend is None:
        return abort(404)

    return json_util.dumps(friend.to_friend_json()), 200


def get_invites(user: User):
    invite_list = []

    for invite_id in user.invite_id_list:
        invite = invite_dao.get_invite(invite_id)
        if invite is None:
            continue

        invite_list.append(invite.__dict__)

    if len(invite_list) == 0:
        return '', 204

    return json_util.dumps(invite_list), 200


def get_current_user(user: User):
    return json_util.dumps(user.to_json())


def valid_invite_type(invite_type):
    if invite_type is None:
        return False

    if invite_type != InviteType.EVENT and invite_type != InviteType.FRIEND:
        return False

    return True
