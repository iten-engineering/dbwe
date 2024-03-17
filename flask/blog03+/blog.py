from flask import Flask, abort, request, jsonify, render_template, flash, redirect, url_for
from data import DataService

#
# initailize
#
app = Flask(__name__,
    static_url_path='',
    static_folder='static')

ds = DataService()


#
# request handlers
#

@app.route('/help')
def help():
    return app.send_static_file('help.html')


@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', username=ds.username(), posts=ds.posts())
