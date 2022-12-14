"""Print numbers from 1 to 100 inclusively following these instructions:
1. if a number is multiple of 3, print "Fizz" instead of this number,
2. if a number is multiple of 5, print "Buzz" instead of this number,
3. for numbers that are multiples of both 3 and 5, print "FizzBuzz",
4. print the rest of the numbers unchanged."""


numbers = list(range(1,101))

for i in numbers:
    
    if i % 3 == 0 and i % 5 == 0:
        numbers[i-1] = "FizzBuzz"
    elif i % 3 == 0:
        numbers[i-1] = "Fizz"
    elif i % 5 == 0:
        numbers[i-1] = "Buzz"
    
print(numbers)
