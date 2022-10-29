# ask the user for the first name. if it matches the previously assigned name, print the password. if it doesn't, do not print the password.

user = "Joseph"
password = "W@12"

name = input("Please enter your first name: ")

if user == name:
    print(f"Hello {name}! The password is: {password}")
else:
    print(f"Hello, {name}! See you later.")
