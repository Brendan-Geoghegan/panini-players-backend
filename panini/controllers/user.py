from ..models.main import User
from ..database.db import db


def show(request):  # request == the id
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


def friends(request):
    """Gets a list of the user's friends' IDs"""
    outputs = User.query.filter_by(id=str(request)).first()
    friends = outputs.friends.split(' ')
    return friends


def all_stickers(request):
    """Gets all stickers associated with a given user account. A dictionary with the count for each specific sticker is returned"""
    outputs = User.query.filter_by(id=str(request)).first()
    stickers = outputs.cards.split(' ')
    sticker_counts = {}
    for sticker in stickers:
        split = sticker.split('-')
        sticker_counts[split[0]] = int(split[1])
    return sticker_counts


def users_by_location(request):
    request.lower()
    outputs = User.query.filter_by(location=str(request).capitalize()).all()
    users = []
    for user in outputs:
        users.append({
            'id': user.id,
            'username': user.username,
            'location': user.location
        })
    return users


def friends_string(request, id):
    output = User.query.filter_by(id=str(id)).first()
    friend_list = output.friends
    print(friend_list)
    return friend_list


def add_friend(request, id):
    data = request.json
    profile = User.query.filter_by(id=str(id)).first()
    profile.friends += f" {data['friend']}"
    db.session.commit()
    return show(id)
