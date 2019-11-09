from datetime import datetime
from unittest import TestCase

from server.database import user_dao, database
from server.entities.user import User
from server.enums import InviteType
from server.utils import user_utils


class TestUserUtils(TestCase):
    def setUp(self):
        self.user_id_1 = user_dao.save_user(User("user1", "password", "nickname", "avatar_url", datetime(1998, 5, 7)))
        self.user_id_2 = user_dao.save_user(User("user2", "password", "nickname", "avatar_url", datetime(2000, 2, 20)))

    def tearDown(self):
        user_dao.delete_user(self.user_id_1)
        user_dao.delete_user(self.user_id_2)

    def test_send_invite(self):
        self.assertTrue(database.id_is_valid(self.user_id_1))
        self.assertTrue(database.id_is_valid(self.user_id_2))

        # TODO check that users was create

        self.invite_to_friend_id = user_utils.send_invite(self.user_id_1, self.user_id_2, InviteType.FRIEND)

        # TODO check that invite id is valid and invite was create
