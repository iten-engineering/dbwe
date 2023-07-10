from datetime import datetime
from blog import db

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email    = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(64))

    def __repr__(self):
        return "User: {}, id={}".format(self.username, self.id)


class Post(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    body     = db.Column(db.String(140))
    timestamp= db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "Post: {}, id={}".format(self.body, self.id)
