from datetime import datetime
from unittest import TestCase

from server.entities.events.group_events.group_event import GroupEvent
from server.utils import user_utils
from server.utils.chats import chat_utils


class TestGettingChats(TestCase):
    print(chat_utils.get_chats("5dd0330f9a5ef7791b641fff"))
