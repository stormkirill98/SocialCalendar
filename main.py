from datetime import datetime
from random import randrange

from flask import Flask

from server import datastore
from shared.entities.user import User

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
    datastore.save_user(user)
    return user.to_json()


# uncomment for debug locale
app.run()
