import json
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
 
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    identifier = db.Column(db.Integer)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))

    def __init__(self, username, identifier, firstName, lastName):
        self.username = username
        self.identifier = identifier
        self.firstName = firstName
        self.lastName = lastName

@app.route('/save_csv', methods=['POST'])
def save_csv():
    with open('username.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        next(reader)
        for user in reader:
            print(user)
            username = user['Username']
            identifier = user[' Identifier']
            firstName = user['First name']
            lastName = user['Last name']
            new_user = Users(username, identifier, firstName, lastName)
            db.session.add (new_user)
            db.session.commit()
    return 'csv File Saved Succesfully'

@app.route('/users', methods = ['GET'])
def crud_users():
    if request.method == 'GET':
        res = []
        for user in Users.query.all():
            res.append({'id': user.id, 'username': user.username, 'identifier': user.identifier, 'firstName': user.firstName, 'lastName': user.lastName})
        return (json.dumps(res))

@app.route('/')
def test():
    return 'How to save csv file to flask using sqlaclhemy'
 
if __name__ == '__main__':
    with app.app_context():db.create_all()
    app.run(debug = True)