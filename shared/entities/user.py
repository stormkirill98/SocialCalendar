class User:
    event_id_list = []
    friend_id_list = []
    chat_id_list = []

    def __init__(self, login, password, nickname, avatar_url, birthday, id=""):
        """Constructor"""
        self.id = id
        self.login = login
        self.password = password
        self.nickname = nickname
        self.avatar_url = avatar_url
        self.birthday = birthday

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
            'birthday': self.birthday
        }
