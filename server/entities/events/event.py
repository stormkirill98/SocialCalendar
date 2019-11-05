from server.entities.datastore_object import DatastoreObject


class Event(DatastoreObject):
    def __init__(self, name, is_private, datetime, address, description, id=""):
        super().__init__(id)
        self.name = name
        self.is_private = is_private  # true or false
        self.datetime = datetime
        self.address = address
        self.description = description
