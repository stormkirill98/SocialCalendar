from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def run():
    return "qu qu"
