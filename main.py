import os

try:
    import local
except ImportError as error:
    pass

from flask import Flask

# Configuration
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

app = Flask(__name__)


@app.route('/')
def run():
    return GOOGLE_CLIENT_ID


# uncomment for debug locale
# app.run()
