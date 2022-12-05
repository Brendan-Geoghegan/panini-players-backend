from flask import Flask, jsonify
from flask_cors import CORS
from .database.db import db
from dotenv import load_dotenv
from os import environ
from flask_login import LoginManager
from .routes.main import auth
from werkzeug import exceptions

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

# auth start 
server.config['SECRET_KEY'] = "secretkey"
server.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///panini.db'
db.init_app(server)

server.register_blueprint(auth, url_prefix="/")

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(server)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@server.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"{err}"}), 404


@server.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"It's not you it's us"}), 500

@server.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error":  f"{err}"}), 400

# auth end

if __name__ == "__main__":
    server.run(debug=True)

