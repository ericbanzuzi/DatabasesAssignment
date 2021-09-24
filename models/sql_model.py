from pathlib import Path
from app import app
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://ericbanzuzi:mysql00eb@localhost/db_project'
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)

    # relationships
    address = db.relationship('Address', back_populates='customer')

    def __repr__(self):
        return f'Customer({id}, {firstname}, {lastname}, {phone_number}, {address})'


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(80), nullable=False)
    house_number = db.Column(db.String(5), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'Address({id}, {street}, {housenumber}, {city}, {postcode})'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    order_datetime = db.Column(db.DateTime, nullable=False)
    discount_code = db.Column(db.Boolean, nullable=False)

    # relationships
    customer = db.relationship('Customer', back_populates='order')
    delivery = db.relationship('DeliveryPerson', secondary='delivery', back_populates='delivery')

    def __repr__(self):
        return f'Order({id}, {customer_id}, {order_date}, {discount_code})'


class Orderline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    drink_id = db.Column(db.Integer, db.ForeignKey('drink.id'))
    desert_id = db.Column(db.Integer, db.ForeignKey('desert.id'))
    quantity = db.Column(db.Integer, nullable=False)

    # relationships
    order = db.relationship('Order', back_populates='orderline')
    pizza = db.relationship('Pizza', back_populates='orderline')
    drink = db.relationship('Drink', back_populates='orderline')
    desert = db.relationship('Desert', back_populates='orderline')

    def __repr__(self):
        return f'Orderline({id}, {order_id}, {pizza_id}, {drink_id}, {desert_id}, {quantity})'


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    vegeterian = db.Column(db.Boolean, nullable=False) # denormalization?

    # relationships
    toppings = db.relationship('Topping', secondary='pizza_toppings', back_populates='pizza')

    def __repr__(self):
        return f'Pizza({id}, {name}, {vegeterian})'


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.DECIMAL(6, 2), nullable=False)

    def __repr__(self):
        return f'Drink({id}, {name}, {price})'


class Desert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.DECIMAL(6, 2), nullable=False)

    def __repr__(self):
        return f'Desert({id}, {name}, {price})'


class Topping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.DECIMAL(6, 2), nullable=False)
    vegeterian = db.Column(db.Boolean, nullable=False)

    # relationships
    pizza = db.relationship('Pizza', secondary='pizza_toppings', back_populates='topping')

    def __repr__(self):
        return f'Topping({id}, {name}, {price}, {vegeterian})'


class PizzaToppings(db.Model):
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), primary_key=True)
    topping_id = db.Column(db.Integer, db.ForeignKey('topping.id'), primary_key=True)

    def __repr__(self):
        return f'Pizza_toppings({pizza_id}, {topping_id})'


class DeliveryPerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_code = db.Column(db.String(10), nullable=False)

    # relationships
    pizza = db.relationship('Order', secondary='delivery', back_populates='order')

    def __repr__(self):
        return f'Delivery_person({id}, {area_code})'


class Delivery(db.Model):
    delivery_person_id = db.Column(db.Integer, db.ForeignKey('delivery_person.id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    estimated_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Delivery({delivery_person_id}, {order_id}, {estimated_time})'

db.create_all()
