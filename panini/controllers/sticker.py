from ..models.main import Sticker, User
from ..database.db import db
from ..helper import add_sticker, remove_sticker, rarity_calculator

def show(request, code): # request == the code
    # request.upper()
    output = Sticker.query.filter_by(code=str(code)).first()
    sticker = {
        'code': output.code,
        'name': output.name,
        'image': output.image,
        'price': output.price
    }
    return sticker, 200

def add(request, code):
    data = request.json.get('user')
    output = User.query.filter_by(id=str(data)).first() 
    output.cards = add_sticker(output.cards, code)
    db.session.commit()
    return output.cards, 201

def remove(request, code):
    data = request.json.get('user')
    output = User.query.filter_by(id=str(data)).first() 
    output.cards = remove_sticker(output.cards, code)
    db.session.commit()
    return output.cards, 200

def show_by_country(request):
    # request.upper()
    outputs = Sticker.query.filter(Sticker.code.contains(request)).all()
    stickers = []
    for sticker in outputs:
        stickers.append({
            'code': sticker.code,
            'name': sticker.name,
            'image': sticker.image,
            'price': sticker.price,
            'rarity': rarity_calculator(sticker)
        })
    return stickers, 200
