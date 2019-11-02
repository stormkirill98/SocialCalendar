from server.entities.events.event import Event


class GroupEvent(Event):
    def __init__(self, name, private, datetime, address, description, members=[], id=""):
        super().__init__(name, private, datetime, address, description, id)
        self.members = members
