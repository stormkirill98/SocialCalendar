class Invite:
    def __init__(self, sender_id, invite_type, place_id, id=""):
        self.id = id
        self.sender_id = sender_id
        self.invite_type = invite_type
        self.place_id = place_id
