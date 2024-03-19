from flask import session
from flask_login import current_user

from models import Post, User, followers

class TestData():

    def __init__(self, db):
        self.db = db
        self.sam = User(username="Sam", email="sam@guru.com", about_me="I like sports.")
        self.sam.set_password("Sam")
        self.zoe = User(username="Zoé", email="zoe@guru.com", about_me="I like cats.")
        self.zoe.set_password("Zoé")
        self.lea = User(username="Lea", email="lea@guru.com")
        self.lea.set_password("Lea")

    def exist_user(self, user):
        user = self.db.session.query(User).filter(User.username == user.username).first()
        return True if user else False

    def load(self):
        self.clear()
        self.load_users()
        self.load_posts()
    

    def clear(self):
        self.db.session.query(Post).delete()
        self.db.session.query(User).delete()
        self.db.session.execute(followers.delete())
        self.db.session.commit()


    def load_users(self):
        users = [self.sam, self.zoe, self.lea]
        for user in users:
            if not self.exist_user(user):
                self.db.session.add(user)
        self.db.session.commit()


    def load_posts(self):
        posts = [
            Post(body="Hello everybody", user_id=self.sam.id),
            Post(body="Hi sam", user_id=self.zoe.id),
            Post(body="Hello sam", user_id=self.lea.id)
        ]
        for post in posts:
            self.db.session.add(post)
        self.db.session.commit()


