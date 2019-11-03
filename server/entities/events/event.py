class Event:
    def __init__(self, name, private, datetime, address, description, id=""):
        self.id = id
        self.event_name = name
        self.is_private = private  # true or false
        self.datetime = datetime
        self.address = address
        self.description = description
