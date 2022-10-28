requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


# Runned out of an item
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now :(")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


# When the list is empty
requested_toppings = []

if requested_toppings:  # This line of code checks whether the list is empty or not
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
    
# Eliminating the unusual toppings

available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni",
                     "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]


for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
