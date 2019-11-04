from server.entities.datastore_object import DatastoreObject


class Invite(DatastoreObject):
    def __init__(self, sender_id, type, place_id, id=""):
        super().__init__(id)
        self.sender_id = sender_id
        self.type = type
        self.place_id = place_id  # ид куда приглашают

    def to_json(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'type': self.type,
            'place_id': self.place_id
        }
