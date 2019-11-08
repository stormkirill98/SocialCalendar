from server.entities.database_object import DatabaseObject


class Event(DatabaseObject):
    def __init__(self, name, is_private, datetime, address, description, id=""):
        super().__init__(id)
        self.name = name
        self.is_private = is_private
        self.datetime = datetime
        self.address = address
        self.description = description
