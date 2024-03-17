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
    def username(self):
        return "Guest"

