
class User:
    event_id_list = {}
    friend_id_list = {}
    chat_id_list = {}

    def __init__(self, id, login, password, nickname, avatar_url, birthday):
        """Constructor"""
        self.id = id
        self.login = login
        self.password = password
        self.nickname = nickname
        self.avatar_url = avatar_url
        self.birthday = birthday
