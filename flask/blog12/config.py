import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # form secret
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    
    # database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # blog posts paggination size
    POSTS_PER_PAGE = 3
    
    # config for email class of this blog
    MAIL_ENABLED = False
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_DEFAULT_RECEIPIENT = os.environ.get('MAIL_DEFAULT_RECEIPIENT')

    # config for flask mail (with sendgrid settings as defaults, except the password)
    MAIL_SERVER   = os.environ.get('MAIL_SERVER')    or 'smtp.sendgrid.net'
    MAIL_PORT     = int(os.environ.get('MAIL_PORT')  or 587)
    MAIL_USE_TLS  = os.environ.get('MAIL_USE_TLS')   or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')  or "apikey"
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') 
    


