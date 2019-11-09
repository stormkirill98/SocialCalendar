from bson import ObjectId

from server.database.database import db, id_is_valid
from server.entities.invite import Invite

invites_collection = db['invites']


def save_invite(invite):
    json = invite.to_json()
    json.pop('id')

    id = invites_collection.insert_one(json).inserted_id
    invite.set_id(id)
    return id


def get_invite(id):
    json = invites_collection.find_one({'_id': ObjectId(id)})
    return Invite(json['sender_id'],
                  json['receiver_id'],
                  json['type'],
                  json['place_id'],
                  str(json['_id']))


def is_exists(id):
    if not id_is_valid(id):
        return False

    return invites_collection.find({'_id': ObjectId(id)}).count() > 0


def delete_invite(id):
    return invites_collection.delete_one({'_id': ObjectId(id)}).deleted_count
