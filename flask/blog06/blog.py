from flask import Flask, abort, request, jsonify, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from werkzeug.urls import url_parse

from config import Config

#
# initailize
#
app = Flask(__name__,
    static_url_path='',
    static_folder='static')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# init login manager
login = LoginManager(app)
login.login_view = 'login'

from data import DataService, TestData
from models import User, Post
from forms import LoginForm, RegistrationForm

# load test data
with app.app_context():
    testdata = TestData(db)
    testdata.load()

    print("### Init Testdata ###")
    users = User.query.all()
    for u in users:
        print(u)

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
@login_required
def home():
    return render_template('home.html', username=current_user.username, posts=ds.posts())


@app.route("/login", methods=['GET', 'POST'])
def login():
    # Check if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # Login Form
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        # Password check
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash("Login failed, please check your credentials")
            return redirect(url_for('home'))
        # Login OK
        login_user(user, remember=remember)
        # Page navigation
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    # Login (via get)
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    username = current_user.username
    logout_user()
    flash("Logout of {} successfully done.".format(username))
    return render_template('logout.html', username=username)


@app.route("/register", methods=['GET', 'POST'])
def register():
    # Check if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    # Register
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    # Route /register wurde mit GET betreten
    return render_template('register.html', title='Register', form=form)


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
