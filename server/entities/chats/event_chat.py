from server.entities.chats.chat import Chat


class EventChat(Chat):
    def __init__(self, event_id, id="", msg_id_list=[]):
        super().__init__(id, msg_id_list)
        self.event_id = event_id

    def to_json(self):
        return {
            'id': self.id,
            'event_id': self.event_id,
            'msg_id_list': self.msg_id_list
        }
