import json
import os

from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests


app = Flask(__name__)


@app.route('/')
def run():
    return "Hello world"

# uncomment for debug locale
# app.run()
