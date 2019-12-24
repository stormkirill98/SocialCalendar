from bson import json_util

from server.database import msg_dao
from server.entities.database_object import DatabaseObject


class Chat(DatabaseObject):
    def __init__(self, id="", msg_id_list=[]):
        super().__init__(id)
        self.msg_id_list = msg_id_list

    def add_msg(self, msg_id):
        self.msg_id_list.append(msg_id)

    def delete_msg(self, msg_id):
        self.msg_id_list.remove(msg_id)

    def convert_all_msg_id_in_msg_entity(self):
        """Convert all msg id in msg entity"""
        # TODO get N msg's and after load require msg's

        msg_list = []
        for msg_id in self.msg_id_list:
            msg = msg_dao.get_msg(msg_id)
            if msg is not None:
                msg_list.append(json_util.dumps(msg.__dict__))

        self.msg_id_list = msg_list
