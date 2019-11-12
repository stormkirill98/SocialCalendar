from server.entities.events.event import Event


class SingleEvent(Event):
    def __init__(self, name, is_private, datetime, address, description, id=""):
        super().__init__(name, is_private, datetime, address, description, id)
