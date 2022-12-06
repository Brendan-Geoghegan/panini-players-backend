from flask import Flask, jsonify, request
from flask_cors import CORS
from .database.db import db
from dotenv import load_dotenv
from os import environ
from flask_login import LoginManager
from .routes.auth import auth
from .routes.main import main_routes
from werkzeug import exceptions
from flask_mail import Message
from .mailers import mail_config
from .models.main import User

server = Flask(__name__)
mail = mail_config(server)
server.register_blueprint(auth, url_prefix="/")
server.register_blueprint(main_routes, url_prefix="/")

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
    return 'Panin Players woooooooooop'

@server.route('/trade', methods=['POST'])
def trade():
    sender = request.form['username']
    receiver = request.form['receiver']
    msg = Message(f'{sender} wants to trade with you!', sender="millington.sean12@gmail.com", recipients=[receiver])
    mail.send(msg)
    return "messge sent", 200

# auth start 
server.config['SECRET_KEY'] = "secretkey"
server.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///panini.db'
db.init_app(server)

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
