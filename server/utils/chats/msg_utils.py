from datetime import datetime

from bson import ObjectId
from werkzeug.exceptions import abort

from server.database import msg_dao, chat_dao
from server.database.database import id_is_valid
from server.entities.chats.inner_classes.message import Message
from server.entities.user import User


def send_msg(json, user: User):
    if user is None or not user.is_authenticated:
        return abort(401)

    chat_id = json.get('chat_id')
    if chat_id is None or not id_is_valid(chat_id):
        return abort(400, "Chat id is not valid")

    if not chat_dao.chat_is_exist(chat_id):
        return abort(404)

    if ObjectId(chat_id) not in user.chat_id_list:
        return abort(403)

    msg_text = json.get('text')
    if msg_text is None:
        return abort(400, "Text of message is not defined")

    msg = Message(user.id, chat_id, datetime.today(), msg_text)
    msg_id = msg_dao.save_msg(msg)
    if chat_dao.dialog_is_exist(chat_id):
        if not chat_dao.add_msg_to_dialog(chat_id, msg_id):
            return abort(500)
    if chat_dao.event_chat_is_exist(chat_id):
        if not chat_dao.add_msg_to_event_chat(chat_id, msg_id):
            return abort(500)

    return '', 204


def update_msg(json, user: User):
    if user is None or not user.is_authenticated:
        return abort(401)

    msg_id = json.get('id')
    if msg_id is None or not id_is_valid(msg_id):
        return abort(400, "Message id is not valid")

    if not msg_dao.is_exists(msg_id):
        return abort(404)

    msg_text = json.get('text')
    if msg_text is None:
        return abort(400, "Text of message is not defined")

    if not msg_dao.update_text(msg_id, msg_text):
        return abort(500)

    return '', 204


def delete_msg(msg_id):
    if msg_id is None or not id_is_valid(msg_id):
        return abort(400, "Message id is not valid")

    if not msg_dao.is_exists(msg_id):
        return abort(404)

    if not msg_dao.delete_msg(msg_id):
        return abort(500)

    return '', 204
