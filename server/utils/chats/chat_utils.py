from datetime import datetime

from server.database import msg_dao, user_dao, chat_dao
from server.entities.chats.chat import Chat


def delete_all_msg(chat: Chat):
    # delete msg's
    for msg_id in chat.msg_id_list:
        msg_dao.delete_msg(msg_id)


def get_chats(user_id, count=5):
    user_chats = get_sorted_chats(user_id)
    return user_chats[:count]


def get_add_chats(user_id, start_num, end_num):
    user_chats = get_sorted_chats(user_id)
    return user_chats[start_num: end_num]


def get_sorted_chats(user_id):
    user = user_dao.get_user(user_id)

    user_chats = []
    for chat_id in user.chat_id_list:
        chat = chat_dao.get_chat(chat_id)
        if chat is not None:
            user_chats.append(chat)

    if len(user_chats) == 0:
        return []

    user_chats.sort(key=lambda x: get_datetime_last_msg(x),
                    reverse=True)

    return user_chats


def get_datetime_last_msg(chat: Chat):
    if len(chat.msg_id_list) == 0:
        return datetime(1, 1, 1)

    return msg_dao.get_msg(chat.msg_id_list[-1]).datetime
