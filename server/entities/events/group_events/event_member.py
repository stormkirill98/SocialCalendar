from bson import ObjectId

from server.entities.database_object import DatabaseObject


class EventMember(DatabaseObject):
    def __init__(self, event_id, user_id,
                 is_can_invite_user=False,
                 is_can_delete_user=False,
                 is_can_change_event=False,
                 is_can_delete_event=False,
                 id=""):
        super().__init__(id)
        self.is_can_invite_user = is_can_invite_user
        self.is_can_delete_user = is_can_delete_user
        self.is_can_change_event = is_can_change_event
        self.is_can_delete_event = is_can_delete_event
        self.user_id = user_id
        self.event_id = event_id

    def to_json(self):
        return {
            'id': self.id,
            'is_can_invite_user': self.is_can_invite_user,
            'is_can_delete_user': self.is_can_delete_user,
            'is_can_change_event': self.is_can_change_event,
            'is_can_delete_event': self.is_can_delete_event,
            'user_id': ObjectId(self.user_id),
            'event_id': ObjectId(self.event_id)
        }
