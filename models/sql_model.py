from pathlib import Path
from app import app
from flask_sqlalchemy import SQLAlchemy

Path("database").mkdir(parents=True, exist_ok=True)  # needed?
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://ericbanzuzi:mysql00eb@localhost/dbproject'
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    # address foreign key?

    # TODO: add relationships
    def __repr__(self):
        return f'Customer({id}, {firstname}, {lastname}, {phone_number}, {address})'


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(80), nullable=False)
    house_number = db.Column(db.String(5), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)

    # TODO: add relationships
    def __repr__(self):
        return f'Address({id}, {street}, {housenumber}, {city}, {postcode})'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    order_date = db.Column(db.DateTime, nullable=False)
    discount_code = db.Column(db.Boolean, nullable=False)

    # TODO: add relationships
    customer = relationship("Customer", back_populates="order")

    def __repr__(self):
        return f'Order({id}, {customer_id}, {order_date}, {discount_code})'


class Orderline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    quantity = db.Column(db.Integer, nullable=False)

    # drink and desert linked nicely

    # TODO: add relationships

    def __repr__(self):
        return f'Orderline({id}, {order_id}, {pizza_id}, {quantity} )'


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.DECIMAL(6, 2), nullable=False)  # data anomaly??
    vegeterian = db.Column(db.Boolean, nullable=False)

    # TODO: add relationships

    def __repr__(self):
        return f'Pizza({id}, {name}, {vegeterian})'


class Topping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.DECIMAL(6, 2), nullable=False)
    vegeterian = db.Column(db.Boolean, nullable=False)  # ??

    # TODO: add relationships

    def __repr__(self):
        return f'Topping({id}, {name}, {price}, {vegeterian} )'


class PizzaToppings(db.Model):
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    topping_id = db.Column(db.Integer, db.ForeignKey('topping.id'))


db.create_all()
