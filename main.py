import os

from flask import Flask, redirect, url_for, request
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    logout_user)
from oauthlib.oauth2 import WebApplicationClient

from server import auth
from server.auth import GOOGLE_CLIENT_ID
from server.database import user_dao
from server.utils import user_utils
from server.utils.chats import chat_utils
from server.utils.events import event_utils

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
login_manager = LoginManager()
login_manager.init_app(app)

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)


@login_manager.user_loader
def load_user(user_id):
    return user_dao.get_user(user_id)


@app.route("/")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'


@app.route("/login")
def login():
    request_uri = auth.login(client)
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    auth.callback(client)
    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/events", methods=['GET'])
def events():
    if request.method == 'GET':
        """Get events in json for month of year
        :arg month
        :arg year"""
        month = request.args.get('month')
        year = request.args.get("year")

        return event_utils.get_events(month, year, current_user)
    else:
        return "Error. This method is not handle"


@app.route("/event", methods=['GET', 'POST', 'PUT', 'DELETE'])
def event():
    if request.method == 'GET':
        """Get event by ID
        :arg id - event id"""
        event_id = request.args.get('id')
        return event_utils.get_event(event_id, current_user)

    if request.method == 'POST':
        """Create new event"""
        event_json = request.get_json()
        return event_utils.create_event(event_json, current_user)  # TODO check that current user was be update

    if request.method == 'PUT':
        """Update name, is_private, datetime, address, description"""
        event_json = request.get_json()
        return event_utils.update_event(event_json, current_user)

    if request.method == 'DELETE':
        """Delete event by ID
        :arg id - event id"""
        event_id = request.args.get('id')
        return event_utils.delete_event(event_id, current_user)


@app.route("/event/group/leave", methods=['DELETE'])
def group_event():
    if request.method == 'DELETE':
        """Leave group event by ID
        :arg id - event id"""
        event_id = request.args.get('id')
        return user_utils.leave_group_event(event_id, current_user)


@app.route("/chat", methods=['GET', 'POST', 'DELETE'])
def chat():
    if request.method == 'GET':
        """Get chat by id"""
        chat_id = request.args.get('id')
        return chat_utils.get_chat(chat_id, current_user)

    if request.method == 'POST':
        """Create new dialog"""
        # TODO request create new dialog
        pass


@app.route("/chat/msg", methods=['POST', 'PUT', 'DELETE'])
def chat_msg():
    if request.method == 'POST':
        """send msg
        :arg chat_id - where send
        :arg text - text of msg"""
        received_json = request.get_json()
        return user_utils.send_msg(received_json, current_user)

    if request.method == 'PUT':
        """update msg
        :arg id - msg id
        :arg text - text of msg"""
        pass

    if request.method == 'DELETE':
        """delete msg
        :arg id - msg id"""
        pass


@app.route("/chats", methods=['GET'])
def chats():
    if request.method == 'GET':
        """Get chats start-end sorted by last msg datetime
        :arg start - number first require chat
        :arg end - number last require chat"""
        pass


@app.route("/friends", methods=['GET', 'POST', 'DELETE'])
def friends():
    if request.method == 'GET':
        """Get all friends"""
        pass

    if request.method == 'DELETE':
        """Remove user from friends
        :arg user_id - who remove from friends"""
        pass


@app.route("/invites", methods=['GET', 'POST', 'DELETE'])
def invites():
    if request.method == 'GET':
        """Get all invites"""
        pass

    if request.method == 'POST':
        """Send invite
        :arg type - to friends or to group event
        :arg where - friend if or group event id"""
        pass

    if request.method == 'DELETE':
        """Accept or decline invite
        :arg id - invite id
        :arg action - accept or decline"""


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
