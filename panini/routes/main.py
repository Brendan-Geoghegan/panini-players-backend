from flask import Blueprint, request, jsonify
# from ..database.db import User, Sticker
from werkzeug import exceptions
from ..controllers import sticker, user

main_routes = Blueprint('main', __name__)

@main_routes.route('/<string:code>')
def sticker_handler(code):
    fns = {
        'GET': sticker.show
    }
    resp = fns[request.method](code)
    return jsonify(resp)

@main_routes.route('/users/<string:id>')
def user_handler(id):
    fns = {
        'GET': user.show
    }
    resp = fns[request.method](id)
    return jsonify(resp)
