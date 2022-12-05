from ..models.main import Sticker
from ..database.db import db

def show(request): # request == the code
    output = Sticker.query.filter_by(code=str(request)).first()
    sticker = {
        'code': output.code,
        'name': output.name,
        'image': output.image,
        'price': output.price
    }
    return sticker

def show_by_country(request):
    request.upper()
    outputs = Sticker.query.filter(Sticker.code.contains(request)).all()
    stickers = []
    for sticker in outputs:
        stickers.append({
            'code': sticker.code,
            'name': sticker.name,
            'image': sticker.image,
            'price': sticker.price
        })
    return stickers
