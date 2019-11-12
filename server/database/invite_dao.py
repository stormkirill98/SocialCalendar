from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.entities.invite import Invite

invites_collection = DB['invites']


def save_invite(invite):
    json = invite.to_json()
    json.pop('id')

    id = invites_collection.insert_one(json).inserted_id
    invite.set_id(id)
    return id


def get_invite(id):
    if not id_is_valid(id):
        return None

    json = invites_collection.find_one({'_id': ObjectId(id)})
    if json is None:
        return None

    return Invite(json['sender_id'],
                  json['receiver_id'],
                  json['type'],
                  json['event_id'],
                  json['_id'])


def is_exists(id):
    if not id_is_valid(id):
        return False

    return database.is_exist(id, invites_collection)


def delete_invite(id):
    if not id_is_valid(id):
        return 0

    return invites_collection.delete_one({'_id': ObjectId(id)}).deleted_count
