from datetime import datetime
from unittest import TestCase

from server.database import user_dao, chat_dao
from server.database.events import group_event_dao, event_member_dao
from server.entities.events.group_events.group_event import GroupEvent
from server.entities.user import User
from server.utils import user_utils


class TestFunctionForGroupEvent(TestCase):
    def setUp(self):
        self.user_id = user_dao.save_user(
            User("user1", "password", "nickname", "avatar_url", datetime(1998, 5, 7)))

        self.group_event_id = ""
        self.member_id = ""
        self.event_chat_id = ""

    def tearDown(self):
        user_dao.delete_user(self.user_id)
        group_event_dao.delete(self.group_event_id)
        event_member_dao.delete(self.member_id)
        chat_dao.delete_event_chat(self.event_chat_id)

    def test_create_group_event(self):
        group_event = GroupEvent("name", True, datetime.today(), "address", "description")
        user = user_dao.get_user(self.user_id)

        self.group_event_id = user_utils.create_group_event(user.id, group_event)
        group_event = group_event_dao.get(self.group_event_id)

        # check that group event was create
        self.assertTrue(group_event_dao.is_exists(self.group_event_id))

        event_member = event_member_dao.get_by_user_event(user.id, group_event.id)

        # check that event member was create for this user
        self.assertIsNotNone(event_member)

        # check count members in event
        self.assertEqual(len(group_event.member_id_list), 1)

        # check that member was create
        self.member_id = group_event.member_id_list[0]
        self.assertTrue(event_member_dao.is_exists(self.member_id))

        # check that member was create for this user
        event_member = event_member_dao.get(self.member_id)
        self.assertEqual(event_member.user_id, user.id)

        # check chat for event
        self.event_chat_id = group_event.chat_id
        self.assertIsNotNone(self.event_chat_id)
        self.assertNotEqual(len(str(self.event_chat_id)), 0)
        self.assertTrue(chat_dao.event_chat_is_exist(self.event_chat_id))

        # check that update user
        user = user_dao.get_user(self.user_id)
        self.assertEqual(len(user.event_id_list), 1)
        self.assertEqual(len(user.chat_id_list), 1)
