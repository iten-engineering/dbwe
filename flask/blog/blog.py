from flask import Flask, abort, request, jsonify, render_template

#
# initailize
#
app = Flask(__name__,
    static_url_path='',
    static_folder='static')


#
# request handlers
#
@app.route("/")
def index():
    return app.send_static_file('index.html')


@app.route('/hello')
def hello():
    return 'Hello World!'
