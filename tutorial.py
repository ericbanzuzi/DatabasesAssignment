from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


User.__table__
Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
print(ed_user.name)
print(str(ed_user.id))

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
print(our_user.__repr__)
print(ed_user is our_user)

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')])

ed_user.nickname = 'eddie'

print(session.dirty)
print(session.new)
session.commit()  # ed now has an id

ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)
print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())

session.rollback()  # revert changes
print(ed_user.name)
print(fake_user in session)
print(session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all())

# querying
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)

for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
    print(name)

from sqlalchemy.orm import aliased

user_alias = aliased(User, name='user_alias')

for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)

for u in session.query(User).order_by(User.id)[1:3]:
    print(u)

for user in session.query(User).filter(User.name == 'ed').filter(User.fullname == 'Ed Jones'):
    print(user)

print(session.query(User).filter(User.name.like('%ed')).count())

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


User.addresses = relationship("Address", order_by=Address.id, back_populates="user")
Base.metadata.create_all(engine)

jack = User(name='jack', fullname='Jack Bean', nickname='jackyboy')
jack.addresses = [
    Address(email_address='jack@google.com'),
    Address(email_address='j25@yahoo.com')
]
print(jack.addresses[1].user)
session.add(jack)
session.commit()
print(jack.addresses)

for u, a in session.query(User, Address).filter(User.id == Address.user_id).filter(
        Address.email_address == 'jack@google.com').all():
    print(u)
    print(a)

session.query(User).join(Address).filter(Address.email_address == 'jack@google.com').all()

session.query(Address).outerjoin(User.addresses).all()  # LEFT OUTER JOIN

for name, in session.query(User.name).filter(User.addresses.any()):  # any = EXISTS || has for many to one
    print(name)

