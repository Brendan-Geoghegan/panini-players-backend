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
    }
    return user
