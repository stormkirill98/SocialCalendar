from bson import ObjectId

from server.datastore.datastore import database, id_is_valid
from server.entities.chats.dialog import Dialog
from server.entities.chats.event_chat import EventChat
from server.entities.chats.message import Message

event_chats_collection = database['event_chats']
dialogs_collection = database['dialogs']
msg_collection = database['messages']


def save_dialog(dialog):
    json = dialog.to_json()
    json.pop('id')

    id = dialogs_collection.insert_one(json).inserted_id
    dialog.set_id(id)
    return dialog


def get_dialog(id):
    json = dialogs_collection.find_one({'_id': ObjectId(id)})
    return Dialog(json['user_id_1'],
                  json['user_id_2'],
                  str(json['_id']),
                  json['msg_id_list'])


def delete_dialog(id):
    return dialogs_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def dialog_is_exist(id):
    if not id_is_valid(id):
        return False

    return dialogs_collection.find({'_id': ObjectId(id)}).count() > 0


def save_event_chat(event_chat):
    json = event_chat.to_json()
    json.pop('id')

    id = event_chats_collection.insert_one(json).inserted_id
    event_chat.set_id(id)
    return event_chat


def get_event_chat(id):
    json = event_chats_collection.find_one({'_id': ObjectId(id)})
    return EventChat(json['event_id'],
                     str(json['_id']),
                     json['msg_id_list'])


def delete_event_chat(id):
    return event_chats_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def save_msg(msg):
    json = msg.to_json()
    json.pop('id')

    id = msg_collection.insert_one(json).inserted_id
    msg.set_id(id)
    return msg


def get_msg(id):
    json = msg_collection.find_one({'_id': ObjectId(id)})
    return Message(json['user_id'],
                   json['datetime'],
                   json['test'],
                   str(json['_id']))


def delete_msg(id):
    return msg_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def add_msg_to_dialog(dialog_id, msg_id):
    result = dialogs_collection.update_one({'_id': ObjectId(dialog_id)},
                                           {'$push': {'msg_id_list': msg_id}})
    return result.modified_count


def add_msg_to_event_chat(event_chat_id, msg_id):
    result = event_chats_collection.update_one({'_id': ObjectId(event_chat_id)},
                                               {'$push': {'msg_id_list': msg_id}})
    return result.modified_count
