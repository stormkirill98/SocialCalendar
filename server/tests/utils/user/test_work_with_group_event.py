from datetime import datetime
from unittest import TestCase

from server.database import user_dao, chat_dao
from server.database.events import group_event_dao, event_member_dao
from server.entities.events.group_events.group_event import GroupEvent
from server.entities.user import User
from server.utils import user_utils
from server.utils.events import group_event_utils


class TestFunctionForGroupEvent(TestCase):
    def setUp(self):
        self.user_id_1 = user_dao.save_user(
            User("user1", "password", "nickname", "avatar_url", datetime(1998, 5, 7)))
        self.user_id_2 = user_dao.save_user(
            User("user2", "password", "nickname", "avatar_url", datetime(2000, 2, 20)))

        self.group_event_id_test_create = ""
        self.group_event_id_test_delete = ""
        self.group_event_id_test_leave = ""

        self.member_id_test_create = ""
        self.member_id_test_delete_1 = ""
        self.member_id_test_delete_2 = ""
        self.member_id_test_leave_1 = ""
        self.member_id_test_leave_2 = ""
        self.event_chat_id = ""

    def tearDown(self):
        user_dao.delete_user(self.user_id_1)
        user_dao.delete_user(self.user_id_2)

        group_event_dao.delete(self.group_event_id_test_create)
        group_event_dao.delete(self.group_event_id_test_delete)
        group_event_dao.delete(self.group_event_id_test_leave)

        event_member_dao.delete(self.member_id_test_create)
        event_member_dao.delete(self.member_id_test_delete_1)
        event_member_dao.delete(self.member_id_test_delete_2)
        event_member_dao.delete(self.member_id_test_leave_1)
        event_member_dao.delete(self.member_id_test_leave_2)
        chat_dao.delete_event_chat(self.event_chat_id)

    def test_create_group_event(self):
        group_event = GroupEvent("name", True, datetime.today(), "address", "description")
        user = user_dao.get_user(self.user_id_1)

        self.group_event_id_test_create = user_utils.create_group_event(user.id, group_event)
        group_event = group_event_dao.get(self.group_event_id_test_create)

        # check that group event was create
        self.assertTrue(group_event_dao.is_exist(self.group_event_id_test_create))

        event_member = event_member_dao.get_by_user_event(user.id, group_event.id)

        # check that event member was create for this user
        self.assertIsNotNone(event_member)

        # check count members in event
        self.assertEqual(len(group_event.member_id_list), 1)

        # check that member was create
        self.member_id_test_create = group_event.member_id_list[0]
        self.assertTrue(event_member_dao.is_exists(self.member_id_test_create))

        # check that member was create for this user
        event_member = event_member_dao.get(self.member_id_test_create)
        self.assertEqual(event_member.user_id, user.id)

        # check chat for event
        self.event_chat_id = group_event.chat_id
        self.assertIsNotNone(self.event_chat_id)
        self.assertNotEqual(len(str(self.event_chat_id)), 0)
        self.assertTrue(chat_dao.event_chat_is_exist(self.event_chat_id))

        # check that update user
        user = user_dao.get_user(self.user_id_1)
        self.assertEqual(len(user.event_id_list), 1)
        self.assertEqual(len(user.chat_id_list), 1)

    def test_delete_event(self):
        group_event = GroupEvent("name", True, datetime.today(), "address", "description")
        group_event.member_id_list.clear()  # hz, no pochemuto was not empty

        # create
        self.group_event_id_test_delete = user_utils.create_group_event(self.user_id_1, group_event)

        # add member
        self.member_id_test_delete_2 = group_event_utils.add_member(self.group_event_id_test_delete, self.user_id_2)
        self.assertIsNotNone(self.member_id_test_delete_2)

        group_event = group_event_dao.get(self.group_event_id_test_delete)
        event_chat = chat_dao.get_event_chat(group_event.chat_id)

        self.member_id_test_delete_1 = group_event.member_id_list[0]
        self.assertNotEqual(self.member_id_test_delete_1, self.member_id_test_delete_2)

        # delete by member without permission on it
        user_utils.delete_group_event(self.member_id_test_delete_2, group_event.id)

        # check that group_event already is exist
        self.assertTrue(group_event_dao.is_exist(self.group_event_id_test_delete))

        # delete by member with permission on it
        user_utils.delete_group_event(self.member_id_test_delete_1, group_event.id)

        # check that members was remove
        self.assertFalse(event_member_dao.is_exists(self.member_id_test_delete_1))
        self.assertFalse(event_member_dao.is_exists(self.member_id_test_delete_2))

        # check that chat was remove
        self.assertFalse(chat_dao.event_chat_is_exist(event_chat.id))

        # check that users were clear
        user1 = user_dao.get_user(self.user_id_1)
        self.assertNotIn(event_chat.id, user1.chat_id_list)
        self.assertNotIn(group_event.id, user1.event_id_list)
        user2 = user_dao.get_user(self.user_id_2)
        self.assertNotIn(event_chat.id, user2.chat_id_list)
        self.assertNotIn(group_event.id, user2.event_id_list)

        # check that event was remove
        self.assertFalse(group_event_dao.is_exist(group_event.id))

    def test_leave_event(self):
        group_event = GroupEvent("name", True, datetime.today(), "address", "description")
        group_event.member_id_list.clear()  # hz, no pochemuto was not empty

        # create
        self.group_event_id_test_leave = user_utils.create_group_event(self.user_id_1, group_event)

        # add member
        self.member_id_test_leave_2 = group_event_utils.add_member(self.group_event_id_test_leave, self.user_id_2)
        self.assertIsNotNone(self.member_id_test_leave_2)

        group_event = group_event_dao.get(self.group_event_id_test_leave)
        event_chat = chat_dao.get_event_chat(group_event.chat_id)

        # for clearing after test
        self.event_chat_id = event_chat.id
        self.member_id_test_leave_1 = group_event.member_id_list[0]

        # check that in group 2 members
        self.assertEqual(len(group_event.member_id_list), 2)

        user_utils.leave_group_event(self.member_id_test_leave_2, group_event.id)

        # check that user were clear
        user2 = user_dao.get_user(self.user_id_2)
        self.assertNotIn(event_chat.id, user2.chat_id_list)
        self.assertNotIn(group_event.id, user2.event_id_list)

        # check that member was remove
        self.assertFalse(event_member_dao.is_exists(self.member_id_test_delete_1))

        # check that member was remove from event
        group_event = group_event_dao.get(self.group_event_id_test_leave)
        self.assertNotIn(self.member_id_test_leave_2, group_event.member_id_list)

        self.member_id_test_leave_1 = group_event.member_id_list[0]
        user_utils.leave_group_event(self.member_id_test_leave_1, group_event.id)

        # check that event was remove because this member is last
        self.assertFalse(group_event_dao.is_exist(group_event.id))
