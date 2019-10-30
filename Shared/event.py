
class Event:

    def __init__(self, name, private, date, time, address, description):
        """Constructor"""
        self.event_name = name
        self.is_private = private  # true of false
        self.date = date  # day of event
        self.time = time
        self.address = address
        self.description = description
