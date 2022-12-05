from flask import Flask
from flask_cors import CORS
from .database.db import db
from dotenv import load_dotenv
from os import environ


#testing purposes
from .models.main import User


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

def add_code(user, input_code):
    # say the code is ECU4
    cards_array = user['cards'].split(' ')
    for card in cards_array:
        if str.__contains__(card, input_code):
            # add conditionals here for cases where ECU1 and ECU10
            index = cards_array.index(card)
            unique = card
    [code , num] = unique.split('-')
    added = int(num) + 1
    cards_array[index] = f"{code}-{added}"
    return cards_array



@server.route('/')
def home():
    users = User.query.all()
    output = map(lambda y : {
        'username' : y.username,
        'cards' : y.cards
    }, users)
    print('######################')
    sean = list(output)[0]
    result = add_code(sean, 'ECU4')
    print(result)
    print('######################')
    return list(output)

if __name__ == "__main__":
    server.run(debug=True)

