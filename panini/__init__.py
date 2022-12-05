from flask import Flask, jsonify
from flask_cors import CORS
from .database.db import db
from dotenv import load_dotenv
from os import environ
from flask_login import LoginManager
from .routes.main import auth
from werkzeug import exceptions

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

