from panini import db, server
from panini.models.main import Sticker, User, List
import string, random

users = [
    {'id': 1, 'username': 'Sean', 'password': 'password123', 'email': 'sean@123.com', 'location': 'Lodon', 'cards': 'afjonivew'},
    {'id': 2, 'username': 'Kornelia', 'password': 'password234', 'email': 'kornelia@123.com', 'location': 'Lodon', 'cards': 'fnaadvo'},
    {'id': 3, 'username': 'George', 'password': 'password345', 'email': 'george@123.com', 'location': 'Lodon', 'cards': 'fmvidfjsd'},
    {'id': 4, 'username': 'Brendan', 'password': 'password456', 'email': 'Brendan@123.com', 'location': 'Lodon', 'cards': 'mfnvrlkf'},
]

list = [
    {'user': 'afjonivew', 'panini': 0, 'FWC1': 1},
    {'user': 'fnaadvo', 'panini': 1, 'FWC1': 1},
    {'user': 'fmvidfjsd', 'panini': 1, 'FWC1': 0},
    {'user': 'mfnvrlkf', 'panini': 0, 'FWC1': 0},
]

def id_generator():
    letters = string.ascii_lowercase + string.digits
    id = ''.join(random.choice(letters) for i in range(10))
    return id

with server.app_context():
    db.drop_all()
    db.create_all()
    for user in users:
        db.session.add(User(id=id_generator(), username=user['username'], password=user['password'], email=user['email'], location=user['location'], cards=user['cards']))

    for cards in list:
        db.session.add(List(user=cards['user'], panini=cards['panini'], fwc1=cards['FWC1'] ))
        db.session.commit()

