from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug import exceptions
from flask_login import login_required, login_user, logout_user, current_user
from ..database.db import db
from ..models.main import User
from panini.database.data import cards
from ..helper import id_generator

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json
        id = id_generator()
        email = data['email']
        username = data['username']
        location= data['location']
        password_1 = data['password_1']
        password_2 = data['password_2']

        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        if username_exists:
            raise exceptions.BadRequest("Username already in database")
        elif email_exists:
            raise exceptions.BadRequest("Email already in database")
        elif password_1 != password_2:
            raise exceptions.BadRequest("Passwords have to be the same")
        else:
            new_user = User(id=id, email=email, username=username, password=generate_password_hash(password_1, method='sha256'), location=location, cards=cards, friends="")
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return jsonify({"message": "New user created"}), 201
    else:
        raise exceptions.BadRequest(f"Please fill in all required information")


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        username = data['username']
        password = data['password']
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return jsonify({"message": "Welcome Panini Player"}), 201
            else:
                raise exceptions.BadRequest(f"Incorrect password")
        else:
            raise exceptions.NotFound(f"User not found")
    else:
        raise exceptions.BadRequest(f"Please fill in all required information")

@login_required
@auth.route("/logout")
def logout():
    logout_user()
    return jsonify({"message": "See you soon!"})
