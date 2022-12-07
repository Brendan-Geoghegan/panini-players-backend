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
from flask_socketio import SocketIO, emit

server = Flask(__name__)
mail = mail_config(server)
server.register_blueprint(auth, url_prefix="/")
server.register_blueprint(main_routes, url_prefix="/")

CORS(server, resources={r"/*":{"origins":"*"}})
socketio = SocketIO(server, cors_allowed_origins="*")
server.host = 'localhost'

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
    return 'Panini Players woooooooooop'

@server.route('/trade', methods=['POST'])
def trade():
    sender = request.json['username']
    receiver = request.json['receiver']
    msg = Message(f'{sender} wants to trade with you!', sender="panini.players@futureproof.com", recipients=[receiver])
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
# auth end

@server.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({"error": f"{err}"}), 404


@server.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({"error": f"It's not you it's us"}), 500

@server.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return jsonify({"error":  f"{err}"}), 400


# socket 
@socketio.on("connect")
def connected():
    """event listener when client connects to the server"""
    print(request.sid)
    print("client has connected")
    emit("connect",{"data":f"id: {request.sid} is connected"})

@socketio.on('data')
def handle_message(data):
    """event listener when client types a message"""
    print("data from the front end: ",str(data))
    emit("data",{'data':data,'id':request.sid},broadcast=True)

@socketio.on("disconnect")
def disconnected():
    """event listener when client disconnects to the server"""
    print("user disconnected")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=True)
#end socket io

if __name__ == "__main__":
    # server.run(debug=True)
    socketio.run(server, debug=True)
