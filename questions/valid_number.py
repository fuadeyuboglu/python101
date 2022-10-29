"""Take the age of the user using input() and while() loop.
    - Take the age from user
    - Check the age if it is correct numeric format."""

age = input("Please enter your age: ")

while not age.isdigit():  
    
    print("Please enter a valid input.")
    age = input("Please enter your age: ")
    
print("Thank you! You entered a valid input. Your age is:", age)


"""Objectives:
    1. While loops
    2. str.isdigit()"""
