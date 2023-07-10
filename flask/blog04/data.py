from flask import session

class DataService():

    _posts = [
        {"author": {"username": "Tom"},  "body": "Hallo zäme, chunnt öpper i d'Aare?" },
        {"author": {"username": "Anna"}, "body": "Hoi Tom, bi gärn derbi. Liebi Grüess Anna." }
    ]


    # 
    # applicaton data
    #
    def posts(self):
        return DataService._posts


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

