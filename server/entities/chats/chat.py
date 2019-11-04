from server.entities.datastore_object import DatastoreObject


class Chat(DatastoreObject):
    def __init__(self, id="", msg_id_list=[]):
        super().__init__(id)
        self.msg_id_list = msg_id_list

    def add_msg(self, msg_id):
        self.msg_id_list.append(msg_id)

    def delete_msg(self, msg_id):
        self.msg_id_list.remove(msg_id)
