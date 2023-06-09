from datetime import datetime
from messageboard import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    message = db.Column(db.String(20))
    time = db.Column(db.DateTime, default=datetime.utcnow)
