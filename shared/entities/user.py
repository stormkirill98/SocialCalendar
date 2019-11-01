class User:
    def __init__(self, login, password, nickname, avatar_url, birthday, id="",
                 event_id_list=[], friend_id_list=[], chat_id_list=[]):
        """Constructor"""
        self.id = id
        self.login = login
        self.password = password
        self.nickname = nickname
        self.avatar_url = avatar_url
        self.birthday = birthday

        self.event_id_list = event_id_list
        self.friend_id_list = friend_id_list
        self.chat_id_list = chat_id_list

    def set_id(self, id):
        self.id = id

    def add_event(self, id):
        self.event_id_list.__add__(id)

    def add_friend(self, id):
        self.friend_id_list.__add__(id)

    def add_chat(self, id):
        self.chat_id_list.__add__(id)

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
            'chat_id_list': self.chat_id_list
        }
