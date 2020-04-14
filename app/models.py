from app import db

import enum
import requests
from sqlalchemy import Enum

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(300), unique=False, nullable=True)
    words_count = db.Column(db.Integer, unique=False, nullable=True)
    http_status_code = db.Column(db.Integer)

class TaskStatus (enum.Enum):
    NOT_STARTED = 1
    PENDING = 2
    FINISHED = 3

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(300), unique=False, nullable=True)
    timestamp = db.Column(db.DateTime)
    task_status = db.Column(Enum(TaskStatus))
    http_status = db.Column(db.Integer)

class NSQD:
    def __init__(self, server):
        self.server= "http://{server}/pub".format(server=server)

    def send(self, topic, msg):
        res = requests.post(self.server, params={"topic": topic}, data=msg)
        if res.ok:
            return res