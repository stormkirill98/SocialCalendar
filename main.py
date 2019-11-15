from flask import Flask

app = Flask(__name__)


@app.route('/')
def run():
    return "Hello world"

# uncomment for debug locale
# app.run()
