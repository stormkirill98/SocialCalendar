class Event:

    def __init__(self, id, name, private, datetime, address, description):
        self.id = id
        self.event_name = name
        self.is_private = private  # true or false
        self.datetime = datetime
        self.address = address
        self.description = description
