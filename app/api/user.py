from flask import jsonify, abort, request
from . import api
from app import db
from app.auth.auth import auth
from app.models.user import User


@api.route('/users/<int:id>')
@auth.login_required
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_json())


@api.route('/users/<int:id>/orders/')
@auth.login_required
def get_user_orders(id):
    user = User.query.get_or_404(id)
    orders = user.orders
    return jsonify({'orders': [order.to_json() for order in orders]})

@api.route('/users', methods=['POST'])
@auth.login_required
def create_user():
    if not request.json:
        abort(400)

    user = User()
    user.address = request.json.get('address', "")
    user.city = request.json.get('city', "")
    user.id_card_no = request.json.get('id_card_no', "")
    user.secure_card_no = request.json.get('secure_card_no', "")
    user.mobile = request.json.get('mobile', "")
    user.username = request.json.get('username', "")

    db.session.add(user)
    db.session.commit()
    return jsonify({'user': user.to_json()}), 201

