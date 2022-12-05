from ..database.db import db
from flask_login import UserMixin

class Sticker(db.Model):
    code = db.Column(db.String(10), primary_key=True, unique=True)
    name = db.Column(db.String(50))
    image = db.Column(db.String(120))
    price = db.Column(db.String(7))


class User(db.Model, UserMixin):
    id = db.Column(db.String(10), primary_key=True, unique=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(30), unique=True)
    location = db.Column(db.String(15))
    cards = db.Column(db.String(5740))
    
