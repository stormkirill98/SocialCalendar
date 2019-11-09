from server.entities.events.event import Event


class GroupEvent(Event):
    def __init__(self, name, is_private, datetime, address, description, member_id_list=[], chat_id="", id=""):
        super().__init__(name, is_private, datetime, address, description, id)
        self.chat_id = chat_id
        self.member_id_list = member_id_list

    def add_member(self, member_id):
        self.member_id_list.append(member_id)

    def delete_member(self, member_id):
        self.member_id_list.remove(member_id)

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_private': self.is_private,
            'datetime': self.datetime,
            'address': self.address,
            'description': self.description,
            'member_id_list': self.member_id_list,
            'chat_id': self.chat_id
        }
