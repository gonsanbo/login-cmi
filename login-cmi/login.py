import json
import hashlib
import tkinter as tk

with open('credentials_file.json', 'r') as f:
    credentials = json.load(f)


def save_credentials():
    with open('credentials_file.json', 'w') as f:
        json.dump(credentials, f)


def encrypt_string(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def new_user_cmi():
    while True:
        new_user = input("Please select your username: ")
        if new_user in credentials:
            print("Username is already taken!")
        else:
            break
    while True:
        new_password = input("Please enter your password: ")
        new_password_confirm = input("Please confirm your password: ")
        if new_password == new_password_confirm:
            if len(new_password) + 1 <= 6:
                print("Password must contain at least 6 characters")
            else:
                credentials[new_user] = encrypt_string(new_password)
                new_password, new_password_confirm = "", ""
                save_credentials()
                print("Account created successfully")
                break
        else:
            print("Passwords do not match!")


def login_cmi():
    print("---------------------------")
    user = input("Enter your username: ")
    hash_password = encrypt_string(input("Enter your password: "))
    try:
        if credentials[user] == hash_password:
            print("You have been logged in")
        else:
            print("Username and password do not match!")
    except:
        print("User does not exist!")
        print("Would you like to create an account?")
        answer = input("[Y]es/[N]o ")
        if answer.lower() == "y":
            new_user_cmi()


def main():
    while True:
        w = input('Would you like to [L]og in, [C]reate an account or [E]xit? ')
        if w.lower() == "l":
            login_cmi()
        elif w.lower() == "c":
            new_user_cmi()
        else:
            break


main()
