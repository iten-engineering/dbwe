import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "axyp8945cxdg4529ocmy"