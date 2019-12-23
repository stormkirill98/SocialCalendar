import json
import os

import requests
from flask import redirect, request, url_for
from flask_login import (
    login_user)
from oauthlib.oauth2 import WebApplicationClient

from server.database import user_dao
from server.entities.user import User

try:
    # for local debug
    import local
except ImportError as error:
    pass

# Configuration
GOOGLE_CLIENT_ID = "1033315078324-tb38sppml93t1kpdmrm3ukgqg873meap.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "nZKk83_UNwrCg0QECwgwOnRQ"
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


def login(client: WebApplicationClient):
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return request_uri


def callback(client: WebApplicationClient):
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    user_info_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(user_info_endpoint)
    user_info_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if user_info_response.json().get("email_verified"):
        unique_id = user_info_response.json()["sub"]
        users_email = user_info_response.json()["email"]
        picture = user_info_response.json()["picture"]
        users_name = user_info_response.json()["name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in your db with the information provided by Google
    user = user_dao.get_user_by_google_id(unique_id)
    if user is None:
        user = User(unique_id, users_name, users_email, picture, "")
        user_dao.save_user(user)
        # TODO send request about birthday
    else:
        if user.profile_pic != picture:
            user.profile_pic = picture
            user_dao.update_picture(user.id, picture)

    # Begin user session by logging the user in
    login_user(user)
