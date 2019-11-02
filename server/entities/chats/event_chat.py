from server.entities.chats.chat import Chat


class EventChat(Chat):
    def __init__(self, event_id, id="", msg_id_list=[]):
        super().__init__(id, msg_id_list)
        self.event_id = event_id
