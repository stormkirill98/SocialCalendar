from bson import ObjectId

from server.database.database import db, id_is_valid
from server.entities.chats.dialog import Dialog
from server.entities.chats.event_chat import EventChat

event_chats_collection = db['event_chats']
dialogs_collection = db['dialogs']


def save_chat(chat):
    """Define type of chat and save it to suitable collection"""
    if isinstance(chat, Dialog):
        return save_chat_in_suitable_collection(chat, dialogs_collection)
    if isinstance(chat, EventChat):
        return save_chat_in_suitable_collection(chat, event_chats_collection)
    return None


def save_chat_in_suitable_collection(chat, collection):
    """Save chat to collection
    :return id"""

    json = chat.to_json()
    json.pop('id')

    id = collection.insert_one(json).inserted_id
    chat.set_id(id)
    return id


# getting chats
def get_dialog(id):
    json = dialogs_collection.find_one({'_id': ObjectId(id)})
    return Dialog(json['user_id_1'],
                  json['user_id_2'],
                  json['_id'],
                  json['msg_id_list'])


def get_event_chat(id):
    json = event_chats_collection.find_one({'_id': ObjectId(id)})
    return EventChat(json['event_id'],
                     json['_id'],
                     json['msg_id_list'])


# chat deleting
def delete_dialog(id):
    return dialogs_collection.delete_one({'_id': ObjectId(id)}).deleted_count


def delete_event_chat(id):
    return event_chats_collection.delete_one({'_id': ObjectId(id)}).deleted_count


# message adding
def add_msg_to_dialog(dialog_id, msg_id):
    result = dialogs_collection.update_one({'_id': ObjectId(dialog_id)},
                                           {'$push': {'msg_id_list': msg_id}})
    return result.modified_count


def add_msg_to_event_chat(event_chat_id, msg_id):
    result = event_chats_collection.update_one({'_id': ObjectId(event_chat_id)},
                                               {'$push': {'msg_id_list': msg_id}})
    return result.modified_count


# chats are exists to database
def dialog_is_exist(id):
    if not id_is_valid(id):
        return False

    return dialogs_collection.find({'_id': ObjectId(id)}).count() > 0


def event_chat_is_exist(id):
    if not id_is_valid(id):
        return False

    return event_chats_collection.find({'_id': ObjectId(id)}).count() > 0
