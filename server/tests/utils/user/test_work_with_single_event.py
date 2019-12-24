from datetime import datetime
from unittest import TestCase

from server.database import user_dao
from server.database.events import single_event_dao
from server.entities.events.single_event import SingleEvent
from server.entities.user import User
from server.utils import user_utils


class TestFunctionForSingleEvent(TestCase):
    def setUp(self):
        self.user_id = user_dao.save_user(
            User("user1", "password", "nickname", "avatar_url", datetime(1998, 5, 7)))

        self.single_event_id_test_create = ""
        self.single_event_id_test_delete = ""

    def tearDown(self):
        user_dao.delete_user(self.user_id)

        single_event_dao.delete(self.single_event_id_test_create)
        single_event_dao.delete(self.single_event_id_test_delete)

    def test_create_single_event(self):
        single_event = SingleEvent("name", True, datetime.today(), "address", "descisadsda")

        self.single_event_id_test_create = user_utils.create_single_event(self.user_id, single_event)

        self.assertTrue(single_event_dao.is_exist(single_event.id))

        user = user_dao.get_user(self.user_id)

        self.assertIn(single_event.id, user.event_id_list)

    def test_delete_single_event(self):
        single_event = SingleEvent("name", True, datetime.today(), "address", "descisadsda")

        self.single_event_id_test_delete = user_utils.create_single_event(self.user_id, single_event)

        user_utils.delete_single_event(self.user_id, single_event.id)

        user = user_dao.get_user(self.user_id)

        self.assertFalse(single_event_dao.is_exist(single_event.id))
        self.assertNotIn(single_event.id, user.event_id_list)

