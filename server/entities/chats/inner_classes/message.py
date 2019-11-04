from server.entities.datastore_object import DatastoreObject


class Message(DatastoreObject):
    def __init__(self, user_id, chat_id, datetime, text, id=""):
        super().__init__(id)
        self.chat_id = chat_id
        self.user_id = user_id
        self.datetime = datetime
        self.text = text

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'chat_id': self.chat_id,
            'datetime': self.datetime,
            'text': self.text
        }
