class Chat:
    def __init__(self, id="", msg_id_list=[]):
        self.id = id
        self.msg_id_list = msg_id_list

    def set_id(self, id):
        self.id = id

    def add_msg(self, msg_id):
        self.msg_id_list.append(msg_id)

    def delete_msg(self, msg_id):
        self.msg_id_list.remove(msg_id)
