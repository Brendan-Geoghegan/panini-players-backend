from ..models.main import User

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

def friends(request):
    output = User.query.filter_by(id=str(request)).first()

    print(output.friends)
    # friends = output.friends
    # print (friends)
    # return friends
