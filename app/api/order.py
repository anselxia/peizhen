from app.models.order import Order
from flask import jsonify, abort, request
from app.auth.auth import auth
from app import db
from . import api

@api.route('/orders/<int:id>')
@auth.login_required
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order.to_json())

@api.route('/orders', methods=['POST'])
@auth.login_required
def create_order():
    if not request.json:
        abort(400)
    order = Order()
    order.user_id = request.json.get('user_id', "")
    order.service_name = request.json.get('service_name', "")
    order.service_type = request.json.get('service_type', "")
    db.session.add(order)
    db.session.commit()
    return jsonify({'order': order.to_json()}), 201