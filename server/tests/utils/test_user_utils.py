from datetime import datetime
from unittest import TestCase

from server.database import user_dao, invite_dao
from server.database.events import group_event_dao, event_member_dao
from server.entities.events.group_events.group_event import GroupEvent
from server.entities.user import User
from server.enums import InviteType
from server.utils import user_utils


class TestUserUtils(TestCase):
    def setUp(self):
        self.sender_invites = user_dao.save_user(
            User("user1", "password", "nickname", "avatar_url", datetime(1998, 5, 7)))
        self.receiver_invites = user_dao.save_user(
            User("user2", "password", "nickname", "avatar_url", datetime(2000, 2, 20)))
        self.group_event_id = group_event_dao.save(
            GroupEvent("group_event", False, datetime.today(), "address", "description", [self.sender_invites]))

        self.invite_to_friend_id_test_send = ""
        self.invite_to_event_id_test_send = ""

        self.invite_to_friend_id_test_accept_invite = ""
        self.invite_to_event_id_test_accept_invite = ""

    def tearDown(self):
        user_dao.delete_user(self.sender_invites)
        user_dao.delete_user(self.receiver_invites)
        group_event_dao.delete(self.group_event_id)

        invite_dao.delete_invite(self.invite_to_friend_id_test_send)
        invite_dao.delete_invite(self.invite_to_event_id_test_send)

        invite_dao.delete_invite(self.invite_to_friend_id_test_accept_invite)
        invite_dao.delete_invite(self.invite_to_event_id_test_accept_invite)

    def test_send_invite(self):
        # check that users were create
        self.assertTrue(user_dao.is_exists(self.sender_invites))
        self.assertTrue(user_dao.is_exists(self.receiver_invites))

        # send invite from user_1 to user_2 in friends
        self.invite_to_friend_id_test_send = user_utils.send_invite(self.sender_invites, self.receiver_invites,
                                                                    InviteType.FRIEND)

        # check invite id and invite existing
        self.assertTrue(invite_dao.is_exists(self.invite_to_friend_id_test_send))

        # check that invite is added to user
        user = user_dao.get_user(self.receiver_invites)
        self.assertIn(self.invite_to_friend_id_test_send, user.invite_id_list)

        # send invite from user_1 to user_2 in event
        self.invite_to_event_id_test_send = user_utils.send_invite(self.sender_invites, self.receiver_invites,
                                                                   InviteType.EVENT, self.group_event_id)

        # check invite id and invite existing
        self.assertTrue(invite_dao.is_exists(self.invite_to_event_id_test_send))

        # check that invite is added to user
        user = user_dao.get_user(self.receiver_invites)
        self.assertIn(self.invite_to_event_id_test_send, user.invite_id_list)

    def test_accept_invite_to_friend(self):
        # INVITE TO FRIEND
        self.invite_to_friend_id_test_accept_invite = user_utils.send_invite(self.sender_invites, self.receiver_invites,
                                                                             InviteType.FRIEND)
        # check invite id and invite existing
        self.assertTrue(invite_dao.is_exists(self.invite_to_friend_id_test_accept_invite))

        invite_to_friend = invite_dao.get_invite(self.invite_to_friend_id_test_accept_invite)

        # accept invite
        user_utils.accept_invite(self.invite_to_friend_id_test_accept_invite)

        # check invite type
        self.assertEqual(invite_to_friend.type, InviteType.FRIEND)

        receiver_user = user_dao.get_user(invite_to_friend.receiver_id)
        sender_user = user_dao.get_user(invite_to_friend.sender_id)

        # check that users became friends
        self.assertIn(invite_to_friend.sender_id, receiver_user.friend_id_list)
        self.assertIn(invite_to_friend.receiver_id, sender_user.friend_id_list)

        # check that invite was delete
        self.assertFalse(invite_dao.is_exists(self.invite_to_friend_id_test_accept_invite))
        self.assertNotIn(self.invite_to_friend_id_test_accept_invite, receiver_user.invite_id_list)

    def test_accept_invite_to_event(self):
        # INVITE TO EVENT
        self.invite_to_event_id_test_accept_invite = user_utils.send_invite(self.sender_invites, self.receiver_invites,
                                                                            InviteType.EVENT, self.group_event_id)
        # check invite id and invite existing
        self.assertTrue(invite_dao.is_exists(self.invite_to_event_id_test_accept_invite))

        invite_to_event = invite_dao.get_invite(self.invite_to_event_id_test_accept_invite)

        # accept invite
        user_utils.accept_invite(self.invite_to_event_id_test_accept_invite)

        # check invite type
        self.assertEqual(invite_to_event.type, InviteType.EVENT)

        receiver_user = user_dao.get_user(invite_to_event.receiver_id)
        event = group_event_dao.get(invite_to_event.event_id)
        member = event_member_dao.get_by_user_event(receiver_user.id, event.id)

        # check that user became event member
        self.assertIn(event.id, receiver_user.event_id_list)

        self.assertIn(member.id, event.member_id_list)

        # check that invite was delete
        self.assertFalse(invite_dao.is_exists(self.invite_to_event_id_test_accept_invite))
        self.assertNotIn(self.invite_to_event_id_test_accept_invite, receiver_user.invite_id_list)

        self.assertEqual(event_member_dao.delete(member.id), 1)

    def test_send_msg(self):
        pass
