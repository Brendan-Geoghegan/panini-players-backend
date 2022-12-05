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

@main_routes.route('/country/<string:country_code>')
# Get stickers by country code
def sticker_country_handler(country_code):
    fns = {
        'GET': sticker.show_by_country
    }
    resp = fns[request.method](country_code)
    return jsonify(resp)

@main_routes.route('/users/<string:id>/friends', methods=['GET', 'POST'])
def friend_handler(id):
    fns = {
        'GET': user.friends,
        # 'POST': user.add_friend
    }
    resp = fns[request.method](id)
    return jsonify(resp)
