from server.database import chat_dao
from server.entities.chats.event_chat import EventChat
from server.utils.chats import chat_utils


def create_event_chat(event_id):
    event_chat = EventChat(event_id)
    chat_dao.save_chat(event_chat)
    return event_chat.id


def delete_event_chat(event_id):
    chat = chat_dao.get_event_chat(event_id)
    chat_utils.delete_all_msg(chat)
    chat_dao.delete_event_chat(chat.id)
