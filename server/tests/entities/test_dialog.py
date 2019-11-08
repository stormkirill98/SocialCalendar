from unittest import TestCase

from server.entities.chats.dialog import Dialog


class TestDialog(TestCase):
    def setUp(self):
        self.dialog = Dialog("user_id_1", "user_id_2", "id123")

    def test_add_msg(self):
        self.assertEqual(len(self.dialog.msg_id_list), 0)
        self.dialog.add_msg("msg_id_1")
        self.assertEqual(len(self.dialog.msg_id_list), 1)
        self.dialog.add_msg("msg_id_2")
        self.assertEqual(len(self.dialog.msg_id_list), 2)

    def test_delete_msg(self):
        self.assertEqual(len(self.dialog.msg_id_list), 2)
        self.dialog.delete_msg("msg_id_1")
        self.assertEqual(len(self.dialog.msg_id_list), 1)
        self.dialog.delete_msg("msg_id_2")
        self.assertEqual(len(self.dialog.msg_id_list), 0)
