number = int(input("Enter a number: "))
n = [2,3,4,5,6,7,8,9]

for i in n :
    if number % i == 0:
        print("Not a prime number")
        break
    else:
        print(f"{number} is a prime number.")
        break
        
# Alternative
n = int(input("Enter a number: "))
count = 0

for i in range(1, n+1):
    if n%i == 0: count += 1
    else: count += 0

if count < 3: print(f'{n} is a prime number.')
else: print(f'{n} is NOT a prime number.')

    
# Assignment 15:

prime = []
n = 100 # int(input("Enter a number: "))

for x in range(1,n) :
    count = 0
    for y in range(1, n) :
        if x % y == 0 : count += 1
    if count == 2 : prime.append(x)

print(prime)
