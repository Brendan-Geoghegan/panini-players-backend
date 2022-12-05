from flask import Blueprint, request, jsonify
# from ..database.db import User, Sticker
from werkzeug import exceptions
from ..controllers import sticker

main_routes = Blueprint('main', __name__)

@main_routes.route('/<string:code>')
def sticker_handler(code):
    fns = {
        'GET': sticker.show
    }
    resp = fns[request.method](code)
    return jsonify(resp)

