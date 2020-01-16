from bson import ObjectId

from server.database import database, user_dao
from server.database.database import DB, id_is_valid
from server.database.events import event_dao
from server.entities.invite import Invite
from server.enums import InviteType

invites_collection = DB['invites']


def save_invite(invite: Invite):
    json = invite.to_json()
    json.pop('id')

    invite_id = invites_collection.insert_one(json).inserted_id
    invite.set_id(invite_id)
    return invite_id


def get_invite(invite_id):
    if not id_is_valid(invite_id):
        return None

    json = invites_collection.find_one({'_id': ObjectId(invite_id)})
    if json is None:
        return None

    invite = Invite(json['sender_id'],
                    json['receiver_id'],
                    json['type'],
                    json['event_id'],
                    json['_id'])

    if invite.type == InviteType.FRIEND:
        user = user_dao.get_user(invite.sender_id)
        invite.sender_name = user.name

    if invite.type == InviteType.EVENT:
        event = event_dao.get_event(invite.event_id)
        invite.event_name = event.name

    return invite


def is_exists(invite_id):
    if not id_is_valid(invite_id):
        return False

    return database.is_exist(invite_id, invites_collection)


def delete_invite(invite_id):
    if not id_is_valid(invite_id):
        return 0

    return invites_collection.delete_one({'_id': ObjectId(invite_id)}).deleted_count
