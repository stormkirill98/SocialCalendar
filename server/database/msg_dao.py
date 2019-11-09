from bson import ObjectId

from server.database.database import db
from server.entities.chats.inner_classes.message import Message

msg_collection = db['messages']


def save_msg(msg):
    json = msg.to_json()
    json.pop('id')

    id = msg_collection.insert_one(json).inserted_id
    msg.set_id(id)
    return id


def get_msg(id):
    json = msg_collection.find_one({'_id': ObjectId(id)})
    return Message(json['user_id'],
                   json['datetime'],
                   json['test'],
                   json['_id'])


def delete_msg(id):
    return msg_collection.delete_one({'_id': ObjectId(id)}).deleted_count
