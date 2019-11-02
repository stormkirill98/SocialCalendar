from bson import ObjectId

from server.datastore.datastore import database

event_chats_collection = database['event_chats']
dialogs_collection = database['dialogs']
msg_collection = database['messages']


def save_dialog(dialog):
    json = dialog.to_json()
    json.pop('id')

    id = dialogs_collection.insert_one(json).inserted_id
    dialog.set_id(id)
    return dialog


def save_event_chat(event_chat):
    json = event_chat.to_json()
    json.pop('id')

    id = event_chats_collection.insert_one(json).inserted_id
    event_chat.set_id(id)
    return event_chat


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
