from sqlalchemy import create_engine

engine = create_engine('mysql://ericbanzuzi:mysql00eb@localhost/dbproject', echo=True)

from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DECIMAL

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    phone_number = Column(String(20), nullable=False)
    # address foreign key?
    # TODO: add relationships
    def __repr__(self):
        return f'Customer({id}, {firstname}, {lastname}, {phone_number})'

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(80), nullable=False)
    house_number = Column(String(5), nullable=False)
    area = Column(String(80), nullable=False) # or city, how do we define area???
    postcode = Column(String(10), nullable=False)

    # TODO: add relationships

    def __repr__(self):
        return f'Address({id}, {street}, {housenumber}, {area}, {postcode})'

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    order_date = Column(String(80), nullable=False)
    # discount code?

    # TODO: add relationships
    customer = relationship("Customer", back_populates="order")
    def __repr__(self):
        return f'Order({id}, )'

class Orderline(Base):
    __tablename__ = 'orderline'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    pizza_id = Column(Integer, ForeignKey('pizza.id'))
    quantity = Column(Integer, nullable=False)
    # drink and desert linked nicely

    # TODO: add relationships

    def __repr__(self):
        return f'Orderline({id}, )'


class Pizza(Base):
    __tablename__ = 'pizza'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    price = Column(DECIMAL(6,2), nullable=False)
    vegeterian = Column(Boolean, nullable=False)

    # TODO: add relationships

    def __repr__(self):
        return f'Pizza({id}, )'

class Topping(Base):
    __tablename__ = 'topping'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    price = Column(DECIMAL(6,2), nullable=False)
    vegeterian = Column(Boolean, nullable=False)

    # TODO: add relationships

    def __repr__(self):
        return f'Topping({id}, )'

Base.metadata.create_all(engine)