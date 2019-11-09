from datetime import datetime
from unittest import TestCase

from server.database import user_dao, invite_dao
from server.database.database import id_is_valid
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
        invite_dao.delete_invite(self.invite_to_friend_id)

    def test_send_invite(self):
        # check that user ids are valid
        self.assertTrue(id_is_valid(self.user_id_1))
        self.assertTrue(id_is_valid(self.user_id_2))

        # check that users were create
        self.assertTrue(user_dao.is_exists(self.user_id_1))
        self.assertTrue(user_dao.is_exists(self.user_id_2))

        # send invite from user_1 to user_2 in friends
        self.invite_to_friend_id = user_utils.send_invite(self.user_id_1, self.user_id_2, InviteType.FRIEND)

        # check invite id and invite existing
        self.assertTrue(id_is_valid(self.invite_to_friend_id))
        self.assertTrue(invite_dao.is_exists(self.invite_to_friend_id))

        # check that invite is added to user
        user = user_dao.get_user(self.user_id_2)
        self.assertIn(self.invite_to_friend_id, user.invite_id_list)
