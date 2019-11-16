import os

from flask import Flask, redirect, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required, logout_user)
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
    return auth.login(client)


@app.route("/login/callback")
def callback():
    return auth.callback(client)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
