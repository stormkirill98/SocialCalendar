from bson import ObjectId

from server.database import database
from server.database.database import DB, id_is_valid
from server.entities.chats.inner_classes.message import Message

msg_collection = DB['messages']


def save_msg(msg: Message):
    json = msg.to_json()
    json.pop('id')

    msg_id = msg_collection.insert_one(json).inserted_id
    msg.set_id(msg_id)
    return msg_id


def update_text(msg_id, text):
    if not id_is_valid(msg_id):
        return False

    result = msg_collection.update_one({'_id': ObjectId(msg_id)},
                                       {'$set': {'text': text}})
    return result.matched_count > 0


def get_msg(msg_id):
    if not id_is_valid(msg_id):
        return None

    json = msg_collection.find_one({'_id': ObjectId(msg_id)})
    if json is None:
        return None

    return Message(json['user_id'],
                   json['chat_id'],
                   json['datetime'],
                   json['text'],
                   json['_id'])


def delete_msg(msg_id):
    if not id_is_valid(msg_id):
        return 0

    return msg_collection.delete_one({'_id': ObjectId(msg_id)}).deleted_count


def is_exists(msg_id):
    if not id_is_valid(msg_id):
        return False

    return database.is_exist(msg_id, msg_collection)
