from app import db
from .order import Order
from flask import jsonify, url_for


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    mobile = db.Column(db.String(64), unique=True, index=True)
    id_card_no = db.Column(db.String(64), unique=True, index=True)
    secure_card_no = db.Column(db.String(64))
    city = db.Column(db.String(64))
    address = db.Column(db.String(64))
    orders = db.relationship('Order', backref='user', lazy='dynamic')

    def to_json(self):
        json_user = {
            'url': url_for('api.get_user', id=self.id, _external=True),
            'username': self.username,
            'mobile': self.mobile,
            'id_card_no': self.id_card_no,
            'secure_card_no': self.secure_card_no,
            'city': self.city,
            'address': self.address,
            'orders': url_for('api.get_user_orders', id=self.id, _external=True),
        }
        return json_user
