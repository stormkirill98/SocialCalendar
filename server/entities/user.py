from flask_login import UserMixin

from server.database.database import id_is_valid
from server.entities.database_object import DatabaseObject


class User(DatabaseObject, UserMixin):
    def __init__(self, google_id, name, email, profile_pic, birthday, id="",
                 event_id_list=[], friend_id_list=[], chat_id_list=[], invite_id_list=[]):
        super().__init__(id)
        self.google_id = google_id
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.birthday = birthday

        self.event_id_list = event_id_list
        self.friend_id_list = friend_id_list
        self.chat_id_list = chat_id_list
        self.invite_id_list = invite_id_list

    def add_event(self, id):
        if not id_is_valid(id):
            return
        self.event_id_list.append(id)

    def delete_event(self, id):
        if not id_is_valid(id):
            return
        self.event_id_list.remove(id)

    def add_friend(self, id):
        if not id_is_valid(id):
            return
        self.friend_id_list.append(id)

    def delete_friend(self, id):
        if not id_is_valid(id):
            return
        self.friend_id_list.remove(id)

    def add_chat(self, id):
        if not id_is_valid(id):
            return
        self.chat_id_list.append(id)

    def delete_chat(self, id):
        if not id_is_valid(id):
            return
        self.chat_id_list.remove(id)

    def add_invite(self, id):
        if not id_is_valid(id):
            return
        self.invite_id_list.append(id)

    def delete_invite(self, id):
        if not id_is_valid(id):
            return
        self.invite_id_list.remove(id)

    def to_json(self):
        return {
            'id': self.id,
            'google_id': self.google_id,
            'name': self.name,
            'email': self.email,
            'profile_pic': self.profile_pic,
            'birthday': self.birthday,
            'event_id_list': self.event_id_list,
            'friend_id_list': self.friend_id_list,
            'chat_id_list': self.chat_id_list,
            'invite_id_list': self.invite_id_list
        }
