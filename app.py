# http://flask.pocoo.org/docs/1.0/quickstart/

from flask import Flask, request, make_response

app = Flask(__name__)

people = []


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user')
def show_users():
    return "\n".join(people)

@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    if username in people:
        return 'Hi %s, You are in the list' % username
    else:
        return '%s, you are not in the list' % username

# curl -v -XPOST 127.0.0.1:5000/user -H 'content-type: application/json' -d '{ "name": "renata" }' 
@app.route('/user', methods=['POST'])
def add_user_profile():
    user = request.get_json()
    username = user['name']
    
    if username in people:
        return 'Hi %s, you are in the list! :)' % username
    else:
        people.append(username)
        return '%s, you were not in the list but you\'re just added' % username 

@app.route('/user/<username>', methods=['DELETE'])
def remove_user_profile(username):
    if username in people:
        people.remove(username)
        return '%s, you were removed from the list.' % username
    else:
        return '%s, you were not in the list.' % username

# $ export FLASK_APP=app.py
# $ flask run
# * Running on http://127.0.0.1:5000/