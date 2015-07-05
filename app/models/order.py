from app import db
from flask import jsonify, url_for

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    service_name = db.Column(db.String(64))
    service_type = db.Column(db.String(64))
    service_time = db.Column(db.DateTime)

    def to_json(self):
        json_order = {
            'url': url_for('api.get_order', id=self.id, _external=True),
            'service_name': self.service_name,
            'service_type': self.service_type,
            'service_time': self.service_time,
            'user': url_for('api.get_user', id=self.user_id, _external=True)
        }
        return json_order




