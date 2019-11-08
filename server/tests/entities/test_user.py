from datetime import datetime
from unittest import TestCase

from server.entities.user import User


class TestUser(TestCase):
    def setUp(self):
        self.user = User("login", "password", "nickname", "avatar_url", datetime(1998, 5, 7), "id")

    def test_add_event(self):
        self.assertEqual(len(self.user.event_id_list), 0)
        self.user.add_event("event_id_1")
        self.assertEqual(len(self.user.event_id_list), 1)
        self.user.add_event("event_id_2")
        self.assertEqual(len(self.user.event_id_list), 2)

    def test_delete_event(self):
        self.assertEqual(len(self.user.event_id_list), 2)
        self.user.delete_event("event_id_1")
        self.assertEqual(len(self.user.event_id_list), 1)
        self.user.delete_event("event_id_2")
        self.assertEqual(len(self.user.event_id_list), 0)

    def test_add_friend(self):
        self.assertEqual(len(self.user.friend_id_list), 0)
        self.user.add_friend("friend_id_1")
        self.assertEqual(len(self.user.friend_id_list), 1)
        self.user.add_friend("friend_id_2")
        self.assertEqual(len(self.user.friend_id_list), 2)

    def test_delete_friend(self):
        self.assertEqual(len(self.user.friend_id_list), 2)
        self.user.delete_friend("friend_id_1")
        self.assertEqual(len(self.user.friend_id_list), 1)
        self.user.delete_friend("friend_id_2")
        self.assertEqual(len(self.user.friend_id_list), 0)

    def test_add_chat(self):
        self.assertEqual(len(self.user.chat_id_list), 0)
        self.user.add_chat("chat_id_1")
        self.assertEqual(len(self.user.chat_id_list), 1)
        self.user.add_chat("chat_id_2")
        self.assertEqual(len(self.user.chat_id_list), 2)

    def test_delete_chat(self):
        self.assertEqual(len(self.user.chat_id_list), 2)
        self.user.delete_chat("chat_id_1")
        self.assertEqual(len(self.user.chat_id_list), 1)
        self.user.delete_chat("chat_id_2")
        self.assertEqual(len(self.user.chat_id_list), 0)

    def test_to_json(self):
        self.user.add_chat("chat_id_1")
        self.user.add_friend("friend_id_1")
        self.user.add_event("event_id_1")
        self.assertEqual(self.user.to_json(), {
            'id': "id",
            'login': "login",
            'password': "password",
            'nickname': "nickname",
            'avatar_url': "avatar_url",
            'birthday': datetime(1998, 5, 7),
            'event_id_list': ['event_id_1'],
            'friend_id_list': ['friend_id_1'],
            'chat_id_list': ['chat_id_1'],
            'invite_id_list': []
        })