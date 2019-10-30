from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient("mongodb+srv://admin:admin@socialcalendar-kjwvs.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


@app.route('/')
def run():
    return "qu qu"
