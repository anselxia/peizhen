import app
from app.models.user import User
from app.models.order import Order
from datetime import datetime

if __name__ == '__main__':

    #app.db.create_all()

    # user1 = User(username='xiaxun',mobile='18612568925', id_card_no='123', secure_card_no='456', city='beijing')
    # user4 = User(username='mm',mobile='18600001001', id_card_no='23424', secure_card_no='63643', city='beijing')

    # app.db.session.add(user1)

    # peizhen_date = datetime.now()
    #
    # order1 = Order(user_id=1, service_name='peizhen', service_type='class1', service_time=peizhen_date)
    # order2 = Order(user_id=2, service_name='peizhen', service_type='class1', service_time=peizhen_date)
    # order3 = Order(user_id=3, service_name='peizhen', service_type='class1', service_time=peizhen_date)
    #
    # app.db.session.add(order1)
    # app.db.session.add(order2)
    # app.db.session.add(order3)
    # print 'calling this'
    # app.db.session.commit()

    app.app.run(debug=True)
