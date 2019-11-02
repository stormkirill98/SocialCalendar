class ChatMember:
    def __init__(self, chat_id, user_id,
                 is_can_invite_user=False,
                 is_can_delete_user=False,
                 is_can_change_event=False,
                 id=""):
        self.id = id
        self.is_can_invite_user = is_can_invite_user
        self.is_can_delete_user = is_can_delete_user
        self.is_can_change_event = is_can_change_event
        self.user_id = user_id
        self.chat_id = chat_id

    def set_id(self, id):
        self.id = id

    def to_json(self):
        return {
            'id': self.id,
            'is_can_invite_user': self.is_can_invite_user,
            'is_can_delete_user': self.is_can_delete_user,
            'is_can_change_event': self.is_can_change_event,
            'user_id': self.user_id,
            'chat_id': self.chat_id
        }
