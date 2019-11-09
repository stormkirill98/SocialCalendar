from server.database import chat_dao
from server.entities.chats.event_chat import EventChat


def create_event_chat(event_id):
    event_chat = EventChat(event_id)
    chat_dao.save_chat(event_chat)
    return event_chat.id
