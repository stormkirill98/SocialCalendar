from datetime import datetime
from unittest import TestCase

from server.database import user_dao
from server.entities.user import User


class TestFunctionForGroupEvent(TestCase):
    def setUp(self):
        self.user = user_dao.save_user(
            User("user1", "password", "nickname", "avatar_url", datetime(1998, 5, 7)))

    def tearDown(self):
        user_dao.delete_user(self.user)

    def test_create_group_event(self):
        pass
