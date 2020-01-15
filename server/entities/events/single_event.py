from server.entities.events.event import Event


class SingleEvent(Event):
    def __init__(self, name, is_private, datetime, address, description, icon, id=""):
        super().__init__(name, is_private, datetime, address, description, icon, id)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_private': self.is_private,
            'datetime': self.datetime,
            'address': self.address,
            'description': self.description,
            'icon': self.icon
        }
