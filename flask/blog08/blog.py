import os, logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
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

# init logger
if not os.path.exists("logs"):
    os.mkdir("logs")

file_handler = RotatingFileHandler("logs/blog.log", maxBytes=1014, backupCount=10)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"))
file_handler.setLevel(logging.INFO)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info("Blog startup")

# init database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# init login manager
login = LoginManager(app)
login.login_view = 'login'

# import models and data services
from data import DataService, TestData
from models import User, Post
from forms import LoginForm, RegistrationForm, EditProfileForm

# init data service
ds = DataService()


#
# flask shell
#
@app.shell_context_processor
def make_shell_context():
    return {"db":db, "User":User, "Post":Post }


#
# error handlers
#

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

#
# request handlers
#

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

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


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = ds.posts()
    return render_template('user.html', user=user, posts=posts)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)


@app.route("/load")
def load():
    """Load test data"""
    with app.app_context():
        testdata = TestData(db)
        testdata.load()
        print("### Load Testdata ###")
        users = User.query.all()
        print("Loaded users:")
        for u in users:
            print("-", u)
        print("Loaded posts:")
        posts = Post.query.all()
        for p in posts:
            print("-", p)
    return redirect(url_for('home'))


@app.route("/clear")
def clear():
    """Clear test data"""
    with app.app_context():
        testdata = TestData(db)
        testdata.clear()
    return redirect(url_for('home'))
