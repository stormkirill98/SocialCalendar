from bson import ObjectId

from server.datastore.datastore import database
from server.entities.chats.dialog import Dialog
from server.entities.chats.event_chat import EventChat

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


def save_msg(msg):
    json = msg.to_json()
    json.pop('id')

    id = msg_collection.insert_one(json).inserted_id
    msg.set_id(id)
    return msg


def add_msg_to_dialog(dialog_id, msg_id):
    result = dialogs_collection.update_one({'_id': ObjectId(dialog_id)},
                                           {'$push': {'msg_id_list': msg_id}})
    return result.modified_count


def add_msg_to_event_chat(event_chat_id, msg_id):
    result = event_chats_collection.update_one({'_id': ObjectId(event_chat_id)},
                                               {'$push': {'msg_id_list': msg_id}})
    return result.modified_count
