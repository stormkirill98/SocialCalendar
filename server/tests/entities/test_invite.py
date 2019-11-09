from unittest import TestCase

from server.entities.invite import Invite


class TestInvite(TestCase):
    def setUp(self):
        self.invite = Invite("sender_id", "receiver_id", "invite_type", "event_id", "id")
        
    def test_to_json(self):
        self.assertEqual(self.invite.to_json(), {
            'id': 'id',
            'sender_id': 'sender_id',
            'receiver_id': 'receiver_id',
            'type': 'invite_type',
            'event_id': 'event_id'
        })
