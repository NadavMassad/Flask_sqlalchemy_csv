# How to save csv file to flask using sqlaclhemy
## Only Server - No GUI
The first thing we do is create a virtual environment.
If we don't have it install on our pc, we need to install it.
Make sure you are in the prject directory in the terminal.
Use the terminal and write this command:
`python -m pip install --user virtualenv `

To create it write in the terminal this:
`python -m virtualenv env`

To activate write this:
`env\Scripts\activate`

Than you need to install the requirements
use the cmd and write:
`pip install -r requirements.txt`

* Some of the package are required for the GUI.

Next we initialize the app, the db and use CORS on the app:

app = Flask(name)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

Then we create a Class That will define how we store the data:

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


We have two actions in this app: save the file, and display the data.
* We can use fake client like `Thunder Client` to help us display
the data.

We need to pay attention to some things when we want to save the file:
1. Check what is the delimeter - In csv files,
the `,` is not always the seperator, so we need to specify it.
The defualt is a comma - `,`.
2. We use the `DictReader` method to create a dictionary from the file:
    `reader = csv.DictReader(f, delimiter=';')`
3. Next, we need to check if the first line of the csv file is the field names,
and not the data it self. If the field names are there, we need to use the 
`next(reader)` function before we iterate over the reader.