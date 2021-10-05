from flask import Flask, request, make_response
from sqlalchemy.sql import func

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/create-customer", methods=["POST"])
def create_customer():
    from models.sql_model import save_new_customer

    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    phone_number = request.form["phone_number"]
    street = request.form["street"]
    house_number = request.form["house_number"]
    city = request.form["city"]
    postcode = request.form["postcode"]

    try:
        save_new_customer(firstname, lastname, phone_number, street, house_number, city, postcode)
    except Exception as ex:
        return make_response({"error": f"could not create user {str(ex)}"}, 400)

    return make_response({"result": "success"}, 200)


@app.route("/create-order", methods=["POST"])
def create_order():
    from models.sql_model import save_new_order, save_new_orderline, find_single_customer, find_single_address
    import json

    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    street = request.form["street"]
    house_number = request.form["house_number"]
    postcode = request.form["postcode"]
    pizzas = json.loads(request.form["pizzas"])
    drinks = json.loads(request.form["drinks"])
    deserts = json.loads(request.form["deserts"])

    if len(pizzas) == 0:
        return make_response({"error": "order does not contain any pizzas"}, 400)

    address = find_single_address(street=street, house_number=house_number, postcode=postcode)
    if address is None:
        return make_response({"error": "address is not in the system"}, 400)

    customer = find_single_customer(firstname=firstname, lastname=lastname, address_id=address.id)
    if customer is None:
        return make_response({"error": "customer has not been created"}, 400)

    try:
        order = save_new_order(customer_id=customer.id, time=func.now())
        for orderline in pizzas:
            save_new_orderline(order.id, "Pizza", orderline[0], orderline[1])

        for orderline in drinks:
            save_new_orderline(order.id, "Drink", orderline[0], orderline[1])

        for orderline in deserts:
            save_new_orderline(order.id, "Desert", orderline[0], orderline[1])

        # TODO: add available delivery guy and place it to a delivery

    except Exception as ex:
        return make_response({"error": f"could not create order {str(ex)}"}, 400)

    return make_response({"result": "success"}, 200)

# TODO: let someone cancel the order if it's placed under 5 mins ago

# TODO: get customer
# TODO: get order -> display the status too
# TODO: get a delivery?

# --- TOM'S CODE --- ##
# from controler import hash_password, check_password, password_complexity
# from models.mongo_model import find_single_user, save_new_user
#
# INVALID_MESSAGE = "Invalid username or password"
#
# # https://flask.palletsprojects.com/en/2.0.x/quickstart
# # https://flask-sqlalchemy.palletsprojects.com/en/2.x/
#
#
# @app.route("/user/<user_id>")
# def get_user(user_id: int):
#     user = find_single_user(id=user_id)
#     if user:
#         return make_response({"username": user.username, "email": user.email}, 200)
#     else:
#         return make_response({"error": f"User with id {user_id} does not exist"})
#
#
# @app.route("/create", methods=["GET"])
# def create_user_template():
#     return render_template("create_user.html")
#
#
#
#
# @app.route("/login", methods=["GET"])
# def show_login():
#     return render_template("login.html", logged_in=False)
#
#
# @app.route("/login/template", methods=["POST"])
# def process_login_template():
#     username = request.form["username"]
#     password = request.form["password"]
#
#     # First, let's check if the user exists
#     the_user = find_single_user(username=username)
#     if the_user is None:
#         return render_template("login.html", logged_in=False, message=INVALID_MESSAGE)
#
#     # Now let's compare the stored password with the given password
#     if check_password(the_user, password):
#         return render_template("login.html", logged_in=True, username=username)
#     else:
#         return render_template("login.html", logged_in=False, message=INVALID_MESSAGE)
#
#
# @app.route("/login", methods=["POST"])
# def process_login():
#     username = request.form["username"]
#     password = request.form["password"]
#
#     # First, let's check if the user exists
#     the_user = find_single_user(username=username)
#     if the_user is None:
#         return INVALID_MESSAGE
#
#     # Now let's compare the stored password with the given password
#     if check_password(the_user, password):
#         return make_response({"result": "Login successful"}, 200)
#     else:
#         return make_response({"error": INVALID_MESSAGE}, 400)