from datetime import datetime
from random import randrange

from bson import ObjectId
from flask import Flask

from server.datastore import user_dao
from server.entities.user import User
from server.utils.chats import dialog_utils

app = Flask(__name__)


@app.route('/')
def run():
    return "Hello world"


@app.route('/create_user')
def create_user():
    user = User("login " + str(randrange(100)),
                "password " + str(randrange(100)),
                "nickname " + str(randrange(100)),
                "url " + str(randrange(100)),
                datetime.today())
    user_dao.save_user(user)
    return user.to_json()


@app.route('/get_user/<user_id>')
def get_user(user_id):
    user = user_dao.get_user(user_id)
    return user.to_json()


@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    count_deleted_user = user_dao.delete_user(user_id)
    return 'Delete ' + str(count_deleted_user) + ' users'


@app.route('/add_event_to_user/<user_id>/<event_id>')
def add_event_to_user(user_id, event_id):
    # TODO check that event_id is event
    modified_count = user_dao.add_event(user_id, event_id)
    return 'Add event to ' + str(modified_count) + ' users'


@app.route('/add_friend_to_user/<user_id>/<friend_id>')
def add_friend_to_user(user_id, friend_id):
    # TODO check that friend_id is friend
    modified_count = user_dao.add_friend(user_id, friend_id)
    return 'Add friend to ' + str(modified_count) + ' users'


@app.route('/add_chat_to_user/<user_id>/<chat_id>')
def add_chat_to_user(user_id, chat_id):
    # TODO check that friend_id is friend
    modified_count = user_dao.add_chat(user_id, chat_id)
    return 'Add chat to ' + str(modified_count) + ' users'


@app.route('/delete_event_from_user/<user_id>/<event_id>')
def delete_event_from_user(user_id, event_id):
    modified_count = user_dao.delete_event(user_id, event_id)
    return 'Delete event from ' + str(modified_count) + ' users'


@app.route('/delete_friend_from_user/<user_id>/<friend_id>')
def delete_friend_from_user(user_id, friend_id):
    modified_count = user_dao.delete_friend(user_id, friend_id)
    return 'Delete friend from ' + str(modified_count) + ' users'


@app.route('/delete_chat_from_user/<user_id>/<chat_id>')
def delete_chat_from_user(user_id, chat_id):
    modified_count = user_dao.delete_chat(user_id, chat_id)
    return 'Delete chat from ' + str(modified_count) + ' users'


@app.route('/create_dialog/<user_id_1>/<user_id_2>')
def create_dialog(user_id_1, user_id_2):
    dialog_utils.create_dialog(user_id_1, user_id_2)
    return ""


@app.route('/delete_dialog/<dialog_id>')
def delete_dialog(dialog_id):
    dialog_utils.delete_dialog(dialog_id)
    return ""


# uncomment for debug locale
app.run()
