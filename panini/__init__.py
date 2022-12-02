from flask import Flask
from flask_cors import CORS
from .database.db import db
from dotenv import load_dotenv
from os import environ


#testing purposes
from .models.main import User, List


server = Flask(__name__)
CORS(server)

load_dotenv()
server.config.update(
    SQLALCHEMY_DATABASE_URI=environ.get('DATABASE_URL'),
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)

with server.app_context():
    db.app = server
    db.init_app(server)

@server.route('/')
def home():
    users = User.query.all()
    for user in users:
        cards = List.query.filter_by(user=user.cards).all() #  list of instances of List
        outputs = map(lambda y: {
            'user': y.user,
            'panini': y.panini,

        }, cards)

        print('######################')
        print(list(outputs))
    return 'usable'

if __name__ == "__main__":
    server.run(debug=True)

