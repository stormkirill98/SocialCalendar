from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
@app.route('/index')
def run():
    return jsonify('Привет мир')