from flask import Blueprint, request, jsonify
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
    resp, status = fns[request.method](request, code)
    return jsonify(resp), status


@main_routes.route('/users/<string:username>')
def user_handler(username):
    fns = {
        'GET': user.show
    }
    resp = fns[request.method](username)
    return jsonify(resp)


@main_routes.route('/friends/<string:id>')
def friend_handler(id):
    fns = {
        'GET': user.show_friend
    }
    resp, status = fns[request.method](id)
    return jsonify(resp), status


@main_routes.route('/country/<string:country_code>')
# Get stickers by country code
def sticker_country_handler(country_code):
    fns = {
        'GET': sticker.show_by_country
    }
    resp, status = fns[request.method](country_code)
    return jsonify(resp), status


@main_routes.route('/users/<string:id>/friends', methods=['GET', 'POST'])
def friend_handler2(id):
    fns = {
        'GET': user.friends_string,
        'POST': user.add_friend
    }
    resp, status = fns[request.method](request, id)
    return jsonify(resp), status


@main_routes.route('/users/<string:id>/friends_list')
def friends_list_handler(id):
    fns = {
        'GET': user.friends,
    }
    resp, status = fns[request.method](id)
    return jsonify(resp), status


@main_routes.route('/users/<string:id>/stickers', methods=['GET', 'POST'])
def all_stickers_handler(id):
    fns = {
        'GET': user.all_stickers,
        # 'POST': user.add_friend
    }
    resp, status = fns[request.method](id)
    return jsonify(resp), status


@main_routes.route('/users/location/<string:location>')
def users_location_handler(location):
    fns = {
        'GET': user.users_by_location
    }
    resp, status = fns[request.method](location)
    return jsonify(resp), status


@main_routes.route('/location', methods=['POST'])
def handle_location():
    resp, status = user.change_location(request)
    return jsonify(resp), status
