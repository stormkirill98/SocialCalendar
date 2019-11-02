from server.entities.chats.chat import Chat


class Dialog(Chat):
    def __init__(self, user_id_1, user_id_2, id="", msg_id_list=[]):
        super().__init__(id, msg_id_list)
        self.user_id_1 = user_id_1
        self.user_id_2 = user_id_2

    def set_id(self, id):
        self.id = id

    def to_json(self):
        return {
            'id': self.id,
            'msg_id_list': self.msg_id_list,
            'user_id_1': self.user_id_1,
            'user_id_2': self.user_id_2
        }
