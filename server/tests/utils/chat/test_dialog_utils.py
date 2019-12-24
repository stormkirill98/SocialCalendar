from datetime import datetime
from unittest import TestCase

from server.database import user_dao, chat_dao
from server.entities.user import User
from server.utils.chats import dialog_utils


class TestFunctionForDialog(TestCase):
    def setUp(self):
        self.user_id_1 = user_dao.save_user(
            User("user1", "password", "nickname", "avatar_url", datetime(1998, 5, 7)))
        self.user_id_2 = user_dao.save_user(
            User("user2", "password", "nickname", "avatar_url", datetime(2000, 2, 20)))

        self.dialog_id = ""

    def tearDown(self):
        user_dao.delete_user(self.user_id_1)
        user_dao.delete_user(self.user_id_2)

        chat_dao.delete_dialog(self.dialog_id)

    def test_create_and_delete_dialog(self):
        dialog = dialog_utils.create_dialog(self.user_id_1, self.user_id_2)
        self.assertIsNotNone(dialog)

        self.dialog_id = dialog.id

        # check that dialog was create
        self.assertTrue(chat_dao.dialog_is_exist(dialog.id))

        user1 = user_dao.get_user(self.user_id_1)
        user2 = user_dao.get_user(self.user_id_2)

        # check that dialog was add to users
        self.assertIn(dialog.id, user1.chat_id_list)
        self.assertIn(dialog.id, user2.chat_id_list)

        dialog_utils.delete_dialog(dialog.id)

        user1 = user_dao.get_user(self.user_id_1)
        user2 = user_dao.get_user(self.user_id_2)

        # check that dialog was remove from users
        self.assertNotIn(dialog.id, user1.chat_id_list)
        self.assertNotIn(dialog.id, user2.chat_id_list)

        # check that dialog was delete
        self.assertFalse(chat_dao.dialog_is_exist(dialog.id))
