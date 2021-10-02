from PyInquirer import prompt
import requests
from models.sql_model import show_menu

BASE_URL = "http://localhost:5000"

main_list = {
    "type": "list",
    "name": "choice",
    "message": "What do you want to do?",
    "choices": ["Create a user", "Create an order", "Login", "Get a user", "Get an order", "See delivery", "Quit"],
}


login_questions = [
    {"type": "input", "message": "First name", "name": "firstname"},
    {"type": "input", "message": "Last name", "name": "lastname"},
    {"type": "input", "message": "Phone number", "name": "phone_number"},
    {"type": "input", "message": "Street", "name": "street"},
    {"type": "input", "message": "House number", "name": "house_number"},
    {"type": "input", "message": "City", "name": "city"},
]

create_questions = [
    {"type": "input", "message": "First name", "name": "firstname"},
    {"type": "input", "message": "Last name", "name": "lastname"},
    {"type": "input", "message": "Phone number", "name": "phone_number"},
    {"type": "input", "message": "Street", "name": "street"},
    {"type": "input", "message": "House number", "name": "house_number"},
    {"type": "input", "message": "City", "name": "city"},
    {"type": "input", "message": "Post code", "name": "postcode"}
]

user_id_questions = [
    {"type": "input", "message": "Enter the id", "name": "user_id"},
]


def login(username, password):
    response = requests.post(BASE_URL + "/login", data={"username": username, "password": password})
    print(response.json())


def create(firstname, lastname, phone_number, street, house_number, city, postcode):
    response = requests.post(BASE_URL + "/create-customer", data={"firstname": firstname, "lastname": lastname, "phone_number": phone_number,
                                                                  "street": street, "house_number": house_number, "city": city, "postcode": postcode})
    print(response.json())


def get_user(user_id):
    response = requests.get(BASE_URL + "/user/" + user_id)
    print(response.json())


if __name__ == "__main__":
    show_menu()
    while True:
        answers = prompt(main_list)
        answer = answers["choice"]
        if answer == "Create a user":
            create_answers = prompt(create_questions)
            create(**create_answers)
        if answer == "Login":
            login_answers = prompt(login_questions)
            login(**login_answers)
        if answer == "Get a user":
            get_user_answers = prompt(user_id_questions)
            get_user(**get_user_answers)
        if answer == "Quit":
            break