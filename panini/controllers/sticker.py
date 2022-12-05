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
