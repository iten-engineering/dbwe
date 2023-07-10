from flask import Flask, abort, request, jsonify, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from forms import LoginForm

#
# initailize
#
app = Flask(__name__,
    static_url_path='',
    static_folder='static')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from data import DataService, TestData
from models import User, Post

# load test data
with app.app_context():
    testdata = TestData(db)
    testdata.load()

# init data service
ds = DataService()


#
# flask shell
#
@app.shell_context_processor
def make_shell_context():
    return {"db":db, "User":User, "Post":Post }

#
# request handlers
#

@app.route('/help')
def help():
    return app.send_static_file('help.html')


@app.route("/")
@app.route('/home')
def home():
    if ds.is_logged_in():
        return render_template('home.html', username=ds.username(), posts=ds.posts())
    return redirect(url_for('login'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if ds.is_logged_in():
        return redirect(url_for('home'))
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        if ds.login(username, password):
            flash( "Login successfully done for user {} with remember {}".format(username, remember) )
            return redirect(url_for('home'))
        flash("Login failed, please check your credentials")
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    username = ds.username()
    ds.logout()
    flash("Logout of {} successfully done.".format(username))
    return render_template('logout.html', username=username)


@app.route('/welcome')
def welcome():
    mike = {
        "firstname": "Mike",
        "lastname" : "Müller",
        "birthday" : "17.04.1966"
    }
    return render_template(
        'welcome.html', title="Chat", user="Sam", text="Test 123",
        numbers=[1,2,3,4], person=mike) 
