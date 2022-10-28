age = float(input("Please enter your age:"))

if age<4:
    print("Your admission cost is £0")
elif age<18:
    print("Your admission cost is £25")
else:
    print("Your admission cost is £40.")
    

# More efficient and easy to modify version

age = float(input("Please enter your age: "))

if age<4:
    price = 0
elif age<18:
    price = 25
else:
    price = 40

print(f"Your admission cost is £{price}")


# Discount for seniors
# Anyone who is 65 and older pays half the regular price, £20

age = float(input("Please enter your age: "))

if age<4:
    price = 0
elif age<18:
    price = 25
elif age<65:
    prince = 40
else:
    price = 20
    
print(f"Your admission cost is £{price}")


# Omitting the else block
# Python does not require an else block at the end

age = float(input("Please enter your age: "))

if age<4:
    price = 0
elif age<18:
    price = 25
elif age<65:
    prince = 40
elif age >= 65:
    price = 20
    
print(f"Your admission cost is £{price}")
