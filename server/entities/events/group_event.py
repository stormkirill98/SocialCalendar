from server.entities.events.event import Event


class GroupEvent(Event):
    def __init__(self, name, private, datetime, address, description, member_id_list=[], id=""):
        super().__init__(name, private, datetime, address, description, id)
        self.members = member_id_list
