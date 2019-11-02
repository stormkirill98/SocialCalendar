class Message:
    def __init__(self, user_id, datetime, text, id=""):
        self.id = id
        self.user_id = user_id
        self.datetime = datetime
        self.text = text
