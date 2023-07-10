from flask import session
from models import Post, User

class DataService():

    # 
    # applicaton data
    #
    def posts(self):
        records = []
        posts = Post.query.all()
        for p in posts:
            u = User.query.get(p.user_id)
            record = {"author": {"username": u.username}, "body": p.body}
            records.append(record)
        return records        

    # 
    # session data
    #
    def login(self, username, password):
        if password == "invalid":
            return False
        session['username'] = username
        return True
    
    def logout(self):
        session.pop('username', None)
        return True

    def clear(self):
        session.clear()
        return True

    def is_logged_in(self):
        return True if 'username' in session else False
    
    def username(self):
        if 'username' in session:
            username = session['username']
            return username
        return None


class TestData():

    def __init__(self, db):
        self.db = db
        self.sam = User(username="Sam", email="sam@guru.com", password_hash="Sam")
        self.zoe = User(username="Zoé", email="zoe@guru.com", password_hash="Zoé")
        self.lea = User(username="Lea", email="lea@guru.com", password_hash="Lea")

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


