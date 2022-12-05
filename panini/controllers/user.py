from ..models.main import User
from ..database.db import db

def show(request): # request == the id
    output = User.query.filter_by(id=str(request)).first()
    user = {
        'id': output.id,
        'username': output.username,
        'password': output.password,
        'email': output.email,
        'location': output.location,
        'cards': output.cards,
        'friends': output.friends
    }
    return user

def friends(request ,id):
    output = User.query.filter_by(id=str(id)).first()
    friend_list = output.friends
    print(friend_list)


def add_friend(request, id):
    data = request.json
    profile = User.query.filter_by(id=str(id)).first() 
    profile.friends += f" {data['friend']}"
    db.session.commit() 
    return show(id)
