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
        """Get events start-end sorted by datetime
        :arg start - number first require event
        :arg end - number last require event"""
        # TODO better set count days forward and back relatively today
        pass


@app.route("/event", methods=['GET', 'POST', 'PUT'])
def event():
    if request.method == 'GET':
        """Get event by ID"""
        pass

    if request.method == 'POST':
        """Create new event"""
        pass

    if request.method == 'PUT':
        """Add member, remove member; update name, is_private, datetime, address, description"""
        pass


@app.route("/chats", methods=['GET', 'POST'])
def chats():
    if request.method == 'GET':
        """Get chats start-end sorted by last msg datetime
        :arg start - number first require chat
        :arg end - number last require chat"""
        pass

    if request.method == 'POST':
        """Create new dialog"""
        pass


@app.route("/chat", methods=['GET', 'POST', 'PUT', 'DELETE'])
def chat():
    if request.method == 'GET':
        """Get chat by id"""
        pass

    if request.method == 'POST':
        """send msg
        :arg user_id - who send
        :arg chat_id - where send
        :arg text - text of msg"""
        pass

    if request.method == 'PUT':
        """update msg
        :arg msg_id
        :arg text - text of msg"""
        pass

    if request.method == 'DELETE':
        """delete msg
        :arg msg_id"""
        pass


@app.route("/chats", methods=['GET', 'POST'])
def chats():
    if request.method == 'GET':
        """Get chats start-end sorted by last msg datetime
        :arg start - number first require chat
        :arg end - number last require chat"""
        pass

    if request.method == 'POST':
        """Create new dialog"""
        pass


@app.route("/friends", methods=['GET', 'POST', 'DELETE'])
def friends():
    if request.method == 'GET':
        """Get all friends"""
        pass

    if request.method == 'POST':
        """Send invite to friends
        :arg user_id - who invite to friends"""
        pass

    if request.method == 'DELETE':
        """Remove user from friends
        :arg user_id - who remove from friends"""
        pass


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
