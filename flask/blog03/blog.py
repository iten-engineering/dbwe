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

@app.route('/hello/<name>')
def hello_name(name):
    return '<h1>Hello {}!</h1>'.format(name)

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


@app.route('/home')
def home():
    return render_template('home.html', title="Home")