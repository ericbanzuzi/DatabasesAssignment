from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.sql import func

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://ericbanzuzi:mysql00eb@localhost/dbproject'
db = SQLAlchemy(app)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    # relationships, many to one
    address = db.relationship('Address', back_populates='customer')
    order = db.relationship('Order', back_populates='customer')

    def __repr__(self):
        return f'Customer({self.firstname}, {self.lastname}, {self.phone_number}, {self.address})'


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(80), nullable=False)
    house_number = db.Column(db.String(5), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)

    customer = db.relationship('Customer', order_by=Customer.id, back_populates="address")

    def __repr__(self):
        return f'Address({self.street}, {self.housenumber}, {self.city}, {self.postcode})'


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    order_datetime = db.Column(db.DateTime, nullable=False, default=datetime.now())
    discount_code = db.Column(db.Boolean, nullable=False)

    # relationships
    customer = db.relationship('Customer', back_populates='order', uselist=False) # many to one
    delivery = db.relationship('DeliveryPerson', secondary='delivery', back_populates='delivery', uselist=False) # one to one

    def __repr__(self):
        return f'Order({self.customer_id}, {self.order_date}, {self.discount_code})'


class Orderline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    drink_id = db.Column(db.Integer, db.ForeignKey('drink.id'))
    desert_id = db.Column(db.Integer, db.ForeignKey('desert.id'))
    quantity = db.Column(db.Integer, nullable=False)

    # relationships, many to many
    order = db.relationship('Order')
    pizza = db.relationship('Pizza')
    drink = db.relationship('Drink')
    desert = db.relationship('Desert')

    def __repr__(self):
        return f'Orderline({self.order_id}, {self.pizza_id}, {self.drink_id}, {self.desert_id}, {self.quantity})'


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # vegetarian = db.Column(db.Boolean, nullable=False) # denormalization?

    # relationships
    toppings = db.relationship('Topping', secondary='pizza_toppings', back_populates='pizza')

    def __repr__(self):
        return f'Pizza({self.name})'


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.DECIMAL(6, 2), nullable=False)

    def __repr__(self):
        return f'Drink({self.name}, {self.price})'


class Desert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.DECIMAL(6, 2), nullable=False)

    def __repr__(self):
        return f'Desert({self.name}, {self.price})'


class Topping(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.DECIMAL(6, 2), nullable=False)
    vegetarian = db.Column(db.Boolean, nullable=False)

    # relationships
    pizza = db.relationship('Pizza', secondary='pizza_toppings', back_populates='toppings')

    def __repr__(self):
        return f'Topping({self.name}, {self.price}, {self.vegetarian})'


class PizzaToppings(db.Model):
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), primary_key=True)
    topping_id = db.Column(db.Integer, db.ForeignKey('topping.id'), primary_key=True)

    def __repr__(self):
        return f'Pizza_toppings({self.pizza_id}, {self.topping_id})'


class DeliveryPerson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_code = db.Column(db.String(10), nullable=False)

    # relationships, many to one
    delivery = db.relationship('Order', secondary='delivery', back_populates='delivery')

    def __repr__(self):
        return f'Delivery_person({self.area_code})'


class Delivery(db.Model):
    delivery_person_id = db.Column(db.Integer, db.ForeignKey('delivery_person.id'), primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    estimated_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'Delivery({self.delivery_person_id}, {self.order_id}, {self.stimated_time})'


# run to initialize the menu data
def create_menu():
    mozzarella = Topping(name='mozzarella', price=1.59, vegetarian=True)
    tomato_sauce = Topping(name='tomato sauce', price=0.99, vegetarian=True)
    oregano = Topping(name='oregano', price=0.49, vegetarian=True)
    ham = Topping(name='ham', price=2.49, vegetarian=False)
    pineapple = Topping(name='pineapple', price=1.20, vegetarian=True)
    mushroom = Topping(name='mushroom', price=1.00, vegetarian=True)
    onion = Topping(name='onion', price=0.39, vegetarian=True)
    pepper = Topping(name='pepper', price=1.20, vegetarian=True)
    tomato = Topping(name='tomato', price=0.49, vegetarian=True)
    spicy_salami = Topping(name="spicy salami", price=2.99, vegetarian=False)
    pepperoni = Topping(name='pepperoni', price=2.49, vegetarian=False)
    egg = Topping(name='egg', price=1.49, vegetarian=True)
    chicken = Topping(name='chicken', price=2.49, vegetarian=False)
    eggplant = Topping(name='eggplant', price=1.49, vegetarian=True)

    pizza = Pizza(name='Margherita')
    pizza.toppings = [
        tomato_sauce, mozzarella, oregano, Topping(name='garlic oil', price=0.49, vegetarian=True)
    ]
    pizza2 = Pizza(name='Hawaii')
    pizza2.toppings = [
        tomato_sauce, mozzarella,  ham, pineapple
    ]
    pizza3 = Pizza(name='Veggie')
    pizza3.toppings = [
        tomato_sauce, mozzarella, onion, tomato, mushroom, pepper
    ]
    pizza4 = Pizza(name='Forest')
    pizza4.toppings = [
        tomato_sauce, mozzarella, mushroom, ham
    ]
    pizza5 = Pizza(name='Diavolo')
    pizza5.toppings = [
        tomato_sauce, mozzarella, spicy_salami, onion, pepper
    ]
    pizza6 = Pizza(name='Pepperoni')
    pizza6.toppings = [
        tomato_sauce, mozzarella, pepperoni
    ]
    pizza7 = Pizza(name='Peppel Pizza')
    pizza7.toppings = [
        tomato_sauce, mozzarella, pepperoni, pepper, chicken
    ]
    pizza8 = Pizza(name='Romano')
    pizza8.toppings = [
        tomato_sauce, mozzarella, oregano, spicy_salami, egg, tomato
    ]
    pizza9 = Pizza(name='Veggie Deluxe')
    pizza9.toppings = [
        tomato_sauce, mozzarella, onion, tomato, mushroom, pepper, oregano, eggplant
    ]
    pizza10 = Pizza(name='Meatlovers')
    pizza10.toppings = [
        tomato_sauce, pepperoni, spicy_salami, ham, chicken, onion
    ]

    # drinks
    coke = Drink(name='Coca-Cola', price=1.99)
    fanta = Drink(name='Fanta', price=1.99)

    # deserts
    cheese_cake = Desert(name='Cheese cake', price=3.50)
    ice_cream = Desert(name='Ice cream', price=2.50)

    db.session.add_all([
        pizza, pizza2, pizza3, pizza4, pizza5, pizza6, pizza7, pizza8, pizza9, pizza10,
        coke, fanta, cheese_cake, ice_cream
    ])
    db.session.commit()


# run to initialize the delivery persons
def create_delivery_persons():
    db.session.add_all([
        DeliveryPerson(area_code='60'),
        DeliveryPerson(area_code='60'),
        DeliveryPerson(area_code='61'),
        DeliveryPerson(area_code='61'),
        DeliveryPerson(area_code='62'),
        DeliveryPerson(area_code='62'),
        DeliveryPerson(area_code='63'),
        DeliveryPerson(area_code='63'),
        DeliveryPerson(area_code='64'),
        DeliveryPerson(area_code='64')
    ])
    db.session.commit()


def save_new_customer(firstname, lastname, phone_number, street, house_number, city, postcode):
    new_customer = Customer(firstname=firstname, lastname=lastname, phone_number=phone_number)

    address = find_single_address(street=street, house_number=house_number, city=city, postcode=postcode)
    if address is None:
        address = Address(street=street, house_number=house_number, city=city, postcode=postcode)

    address.customer = address.customer + [new_customer]
    db.session.add(new_customer)
    db.session.commit()
    return new_customer


def find_single_address(**kwargs):
    return Address.query.filter_by(**kwargs).first()


def show_menu():

    print('MENU:')
    for pizza, total_price, vegetarian in db.session.query(Pizza, func.sum(Topping.price), func.count(Topping.vegetarian)).select_from(Pizza).join(PizzaToppings).\
            join(Topping).group_by(Pizza.id).order_by(Pizza.id).all():

        if vegetarian == len(pizza.toppings):
            print(pizza.name + ' (V) ' + str(total_price))
        else:
            print(pizza.name + '  ' + str(total_price))
        print([topping.name for topping in pizza.toppings])

    # alternative way
    # for pizza in db.session.query(Pizza).order_by(Pizza.id).all():
    #     price = 0
    #     toppings = []
    #     vegetarian = True
    #     for topping in pizza.toppings:
    #         toppings.append(topping.name)
    #         price = price + topping.price
    #         if not topping.vegetarian:
    #             vegetarian = False
    #
    #     if vegetarian:
    #         print(pizza.name + ' (V) ' + str(price))
    #     else:
    #         print(pizza.name + '  ' + str(price))
    #     print(toppings)

    print()
    print('DRINKS:')
    for drink in db.session.query(Drink).order_by(Drink.id).all():
        print(drink.name + '  ' + str(drink.price))

    print()
    print('DESERTS:')
    for desert in db.session.query(Desert).order_by(Desert.id).all():
        print(desert.name + '  ' + str(desert.price))


db.create_all()
