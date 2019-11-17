from bson import ObjectId

from server.database.database import DB, is_exist, id_is_valid
from server.entities.chats.dialog import Dialog
from server.entities.chats.event_chat import EventChat

event_chats_collection = DB['event_chats']
dialogs_collection = DB['dialogs']


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

    chat_id = collection.insert_one(json).inserted_id
    chat.set_id(chat_id)
    return chat_id


# getting chats
def get_chat(chat_id):


def get_dialog(dialog_id):
    if not id_is_valid(dialog_id):
        return None

    json = dialogs_collection.find_one({'_id': ObjectId(dialog_id)})
    if json is None:
        return None

    return Dialog(json['user_id_1'],
                  json['user_id_2'],
                  json['_id'],
                  json['msg_id_list'])


def get_event_chat(event_chat_id):
    if not id_is_valid(event_chat_id):
        return None

    json = event_chats_collection.find_one({'_id': ObjectId(event_chat_id)})
    return create_event_chat_from_json(json)


def get_event_chat_by_event_id(event_id):
    if not id_is_valid(event_id):
        return None

    json = event_chats_collection.find_one({'event_id': ObjectId(event_id)})
    return create_event_chat_from_json(json)


# chat deleting
def delete_dialog(dialog_id):
    if not id_is_valid(dialog_id):
        return 0

    return dialogs_collection.delete_one({'_id': ObjectId(dialog_id)}).deleted_count


def delete_event_chat(event_chat_id):
    if not id_is_valid(event_chat_id):
        return 0

    return event_chats_collection.delete_one({'_id': ObjectId(event_chat_id)}).deleted_count


# message adding
def add_msg_to_dialog(dialog_id, msg_id):
    if not id_is_valid(dialog_id) or not id_is_valid(msg_id):
        return 0

    result = dialogs_collection.update_one({'_id': ObjectId(dialog_id)},
                                           {'$push': {'msg_id_list': msg_id}})
    return result.modified_count


def add_msg_to_event_chat(event_chat_id, msg_id):
    if not id_is_valid(event_chat_id) or not id_is_valid(msg_id):
        return 0

    result = event_chats_collection.update_one({'_id': ObjectId(event_chat_id)},
                                               {'$push': {'msg_id_list': msg_id}})
    return result.modified_count


# message removing
def delete_msg_from_dialog(dialog_id, msg_id):
    if not id_is_valid(dialog_id) or not id_is_valid(msg_id):
        return 0

    result = dialogs_collection.update_one({'_id': ObjectId(dialog_id)},
                                           {'$pull': {'msg_id_list': msg_id}})
    return result.modified_count


def delete_msg_from_event_chat(event_chat_id, msg_id):
    if not id_is_valid(event_chat_id) or not id_is_valid(msg_id):
        return 0

    result = event_chats_collection.update_one({'_id': ObjectId(event_chat_id)},
                                               {'$pull': {'msg_id_list': msg_id}})
    return result.modified_count


# chats are exists to database
def dialog_is_exist(dialog_id):
    if not id_is_valid(dialog_id):
        return False

    return is_exist(dialog_id, dialogs_collection)


def event_chat_is_exist(event_chat_id):
    if not id_is_valid(event_chat_id):
        return False

    return is_exist(event_chat_id, event_chats_collection)


def create_event_chat_from_json(json):
    if json is None:
        return None

    return EventChat(json['event_id'],
                     json['_id'],
                     json['msg_id_list'])