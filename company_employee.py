# collect first name , last name and email
# generate random password
#   - first 2 letters of firstname
#   - last 2 letters of lastname
#   - random str  len 5 -> 9
# Print password - if satisfied -> YES end/ No - user enter password validate password
# User password
#   > 7 character, print user details end
#   < 7 input a new password equal to or greater than 7 in length
# Container for user data
#  - user data are stored in the container : list or dict
#  - print out each item in the container when all users are done.

from random import randint
from string import ascii_letters
import os

container = []


def get_user_details():
    user = {}
    user["first_name"] = input("Firstname: ")
    user["last_name"] = input("Lastname: ")
    user["email"] = input("email: ")

    return user


def generate_pwd(user):
    pwd = ""
    pt1 = user["first_name"][:2]
    pt2 = user["last_name"][-2:]

    while len(pwd) < 5:
        rand_num = randint(0, len(ascii_letters) - 1)
        pwd += ascii_letters[rand_num]

    return f"{pt1}{pt2}{pwd}"


def get_new_pwd():
    pwd = input("Enter your choice password \n >")

    while len(pwd) < 7:
        pwd = input(
            "Input a new password equal to or greater than 7 in length \n >")

    return pwd


def save_user(user, password):
    u = dict(user)
    u["password"] = password
    container.append(u)
    print("User Saved")


if __name__ == "__main__":
    print("Welcome to HNG IT Manager \n")
    running = True

    while running:
        try:
            option = int(input(
                "Press 1 to add a new user \nPress 2 to close application \n> "))

            if option in range(1, 3):
                if option == 1:
                    print("Please fill the following fields")
                    user = get_user_details()
                    pwd = generate_pwd(user)
                    print(f"* Your password is {pwd} *")
                    response = input(
                        "Press \n 'Y' - to accept \n 'Any Key' - if you want to enter your choice password \n > ")

                    if response.upper() == 'Y':
                        save_user(user, pwd)
                    else:
                        user_pwd = get_new_pwd()
                        save_user(user, user_pwd)
                elif option == 2:
                    print("Exiting...")
                    running = False

                    if len(container) == 0:
                        print("no user saved")
                    else:
                        print("**HNG USERS**")
                        for index, user in enumerate(container):
                            first_name = user["first_name"]
                            last_name = user["last_name"]
                            email = user["email"]
                            password = user["password"]
                            print(
                                f"{index + 1} \tName: {first_name} {last_name} \n\tEmail: {email}\n\tPassword: {password}\n")

            else:
                print("Option not included, Select -> ")
        except ValueError:
            print("Please select number 1 or 2")