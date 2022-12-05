from flask import Blueprint, request, jsonify, redirect
from werkzeug import exceptions
from ..controllers import sticker, user

main_routes = Blueprint('main', __name__)

@main_routes.route('/<string:code>', methods=['GET', 'POST', 'PUT'])
def sticker_handler(code):
    fns = {
        'GET': sticker.show,
        'POST': sticker.add,
        'PUT': sticker.remove
    }
    resp = fns[request.method](request, code)
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
        'GET': user.friends_string,
        'POST': user.add_friend
    }
    resp = fns[request.method](request, id)
    return jsonify(resp)


@main_routes.route('/users/<string:id>/friends_list')
def friends_list_handler(id):
    fns = {
        'GET': user.friends,
    }
    resp = fns[request.method](id)
    return jsonify(resp)


@main_routes.route('/users/<string:id>/stickers', methods=['GET', 'POST'])
def all_stickers_handler(id):
    fns = {
        'GET': user.all_stickers,
        # 'POST': user.add_friend
    }
    resp = fns[request.method](id)
    return jsonify(resp)


@main_routes.route('/users/location/<string:location>')
def users_location_handler(location):
    fns = {
        'GET': user.users_by_location
    }
    resp = fns[request.method](location)
    return jsonify(resp)
