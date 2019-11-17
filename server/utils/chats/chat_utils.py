from server.database import msg_dao, user_dao
from server.entities.chats.chat import Chat


def delete_all_msg(chat: Chat):
    # delete msg's
    for msg_id in chat.msg_id_list:
        msg_dao.delete_msg(msg_id)


def get_chats(user_id, count: int):
    user = user_dao.get_user(user_id)

    user_chats = []
    for chat_id in user.chat_id_list:
        pass
