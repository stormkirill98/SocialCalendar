from server.entities.datastore_object import DatabaseObject


class User(DatabaseObject):
    def __init__(self, login, password, nickname, avatar_url, birthday, id="",
                 event_id_list=[], friend_id_list=[], chat_id_list=[], invite_id_list=[]):
        super().__init__(id)
        self.login = login
        self.password = password
        self.nickname = nickname
        self.avatar_url = avatar_url
        self.birthday = birthday

        self.event_id_list = event_id_list
        self.friend_id_list = friend_id_list
        self.chat_id_list = chat_id_list
        self.invite_id_list = invite_id_list

    def add_event(self, id):
        self.event_id_list.append(id)

    def delete_event(self, id):
        self.event_id_list.remove(id)

    def add_friend(self, id):
        self.friend_id_list.append(id)

    def delete_friend(self, id):
        self.friend_id_list.remove(id)

    def add_chat(self, id):
        self.chat_id_list.append(id)

    def delete_chat(self, id):
        self.chat_id_list.remove(id)

    def add_invite(self, id):
        self.invite_id_list.append(id)

    def delete_invite(self, id):
        self.invite_id_list.remove(id)

    def to_json(self):
        return {
            'id': self.id,
            'login': self.login,
            'password': self.password,
            'nickname': self.nickname,
            'avatar_url': self.avatar_url,
            'birthday': self.birthday,
            'event_id_list': self.event_id_list,
            'friend_id_list': self.friend_id_list,
            'chat_id_list': self.chat_id_list,
            'invite_id_list': self.invite_id_list
        }
