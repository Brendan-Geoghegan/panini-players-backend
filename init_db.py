from panini import db, server
from panini.models.main import User, Sticker
from panini.database.data import cards, stickers
from helper import id_generator

#dummy data
users = [
    {'username': 'Sean', 'password': 'password123', 'email': 'sean@123.com', 'location': 'Lodon', 'cards': cards, 'friends': ''},
    {'username': 'Kornelia', 'password': 'password234', 'email': 'kornelia@123.com', 'location': 'Lodon', 'cards': cards, 'friends': ''},
    {'username': 'George', 'password': 'password345', 'email': 'george@123.com', 'location': 'Lodon', 'cards': cards, 'friends': ''},
    {'username': 'Brendan', 'password': 'password456', 'email': 'Brendan@123.com', 'location': 'Lodon', 'cards':cards, 'friends': ''},
]

with server.app_context():
    db.drop_all()
    db.create_all()
    for user in users:
        db.session.add(User(id=id_generator(), username=user['username'], password=user['password'], email=user['email'], location=user['location'], cards=user['cards'], friends=user['friends']))
        db.session.commit()

    for sticker in stickers:
        db.session.add(Sticker(code=sticker['code'], name=sticker['name'], image=sticker['image'], price=sticker['price']))
        db.session.commit()
