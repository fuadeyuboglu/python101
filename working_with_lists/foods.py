# To copy a list, we can make a slice ---> list[:]
my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print()

# we have two seperate lists. to prove that we add a new different item to each list:
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print()

# If you don't use slice[:]
my_foods = ["pizza","falafel","carrot cake"]
friend_foods = my_foods  # You assign a new variable "friend_foods" to the same list that was assigned to "my_foods"
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
