import os

from flask import Flask, redirect, url_for, request
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    logout_user)
from oauthlib.oauth2 import WebApplicationClient
from flask_cors import CORS, cross_origin

from server import auth
from server.auth import GOOGLE_CLIENT_ID
from server.database import user_dao
from server.utils import user_utils
from server.utils.chats import chat_utils, msg_utils
from server.utils.events import event_utils

app = Flask(__name__)
CORS(app)
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
@cross_origin()
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
@cross_origin()
def login():
    request_uri = auth.login(client)
    return redirect(request_uri)


@app.route("/login/callback")
@cross_origin()
def callback():
    auth.callback(client)
    return redirect("https://social-calendar-front.herokuapp.com/")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("https://social-calendar-front.herokuapp.com/")


@app.route("/events", methods=['GET'])
@login_required
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
@login_required
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
@login_required
def group_event():
    if request.method == 'DELETE':
        """Leave group event by ID
        :arg id - event id"""
        event_id = request.args.get('id')
        return user_utils.leave_group_event(event_id, current_user)


@app.route("/chat", methods=['GET', 'POST', 'DELETE'])
@login_required
def chat():
    if request.method == 'GET':
        """Get chat by id"""
        chat_id = request.args.get('id')
        return chat_utils.get_chat(chat_id, current_user)


@app.route("/chat/msg", methods=['POST', 'PUT', 'DELETE'])
@login_required
def chat_msg():
    if request.method == 'POST':
        """send msg
        :arg chat_id - where send
        :arg text - text of msg"""
        received_json = request.get_json()
        return msg_utils.send_msg(received_json, current_user)

    if request.method == 'PUT':
        """update msg
        :arg id - msg id
        :arg text - text of msg"""
        received_json = request.get_json()
        return msg_utils.update_msg(received_json, current_user)

    if request.method == 'DELETE':
        """delete msg
        :arg id - msg id"""
        msg_id = request.args.get('id')
        return msg_utils.delete_msg(msg_id)


@app.route("/chats", methods=['GET'])
@login_required
def chats():
    if request.method == 'GET':
        """Get N chats sorted by last msg datetime
        :arg count_getting - count already is get
        :arg count - count require chat"""

        count_getting = request.args.get('count_getting')
        count = request.args.get('count')

        return chat_utils.get_chats(current_user, count_getting, count)


@app.route("/friends", methods=['GET'])
@login_required
def friends():
    if request.method == 'GET':
        """Get all friends"""
        return user_utils.get_friends(current_user)


@app.route("/friend", methods=['GET', 'DELETE'])
@login_required
def friend():
    if request.method == 'GET':
        """Get friend by id"""
        friend_id = request.args.get('id')
        return user_utils.get_friend(friend_id)

    if request.method == 'DELETE':
        """Remove user from friends by id
        :arg id - id of friend which need remove from friends"""
        friend_id = request.args.get('id')
        return user_utils.remove_friend(friend_id, current_user)


@app.route("/invites", methods=['GET'])
@login_required
def invites():
    if request.method == 'GET':
        """Get all invites"""
        return user_utils.get_invites(current_user)


@app.route("/invite", methods=['POST', 'DELETE'])
@login_required
def invite():
    if request.method == 'POST':
        """Send invite
        :arg type - to friends or to group event
        :arg receiver_id - who receive this invite
        :arg event_id - optional is type is friend"""
        received_json = request.get_json()
        return user_utils.send_invite(received_json, current_user)

    if request.method == 'DELETE':
        """Accept or decline invite
        :arg id - invite id
        :arg action - accept or decline"""
        invite_id = request.args.get('id')
        action = request.args.get('action')
        return user_utils.handle_invite(invite_id, action, current_user)


@app.route("/search/users", methods=['GET'])
@login_required
def search_users():
    if request.method == 'GET':
        """Get users filtered by filtered string
        :arg filtered_str"""
        filtered_str = request.args.get('filtered_str')
        return user_utils.search_users(filtered_str)


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
