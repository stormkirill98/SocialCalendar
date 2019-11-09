from server.database import msg_dao
from server.entities.chats.chat import Chat


def delete_all_msg(chat: Chat):
    # delete msg's
    for msg_id in chat.msg_id_list:
        msg_dao.delete_msg(msg_id)
