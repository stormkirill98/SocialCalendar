
class User:

    def __init__(self, id, login, password, nickname, url, birth_date):
        """Constructor"""
        self.id = id
        self.login = login
        self.password = password
        self.nickname = nickname
        self.avatar = url
        self.birth_date = birth_date
