while True:
    try:
        number = int(input("Please enter a number: ")) 
        if number > 0:
            digits = list(str(number))
            count = 0

            for i in range(0, len(digits)):
                digits[i] = int(digits[i])

            for j in digits:
                count += j**len(digits)

            if count == int(number):
                print(f"{number} is an Armstrong number :)")
            else: 
                print(f"{number} is NOT an Armstrong number :(")
            break
        else:
            print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    except ValueError:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        

# Alternative 1
while True :
    number = input("Armstrong Number detector: ")
    digits = len(number)
    sum_ = 0
    
    if not number.isdigit() :
        print(number, " is an invalid entry. Please do not use non-numeric, float or negative values!")
    
    elif int(number) >= 0 :
        for i in range(len(number)) :
            sum_ = sum_ + int(number[i]) ** digits
            
        if sum_ == int(number) :
            print(number, ": Detected! It's an Armstrong Number.")
            break
        else:
            print(number, " isn't an Armstrong Number. You can do it!")


# Alternative 2

number = input("Armstrong Number detector: ")
digits = len(number)
sum_ = 0

set1 = set(number)
set2 = set("0123456789")

if set1 & set2 != set1 :
    print(number, "is an invalid entry. Please do not use non-numeric, float or negative values!")
    
else:
    for i in number:
        sum_ = int(i) ** digits
        
    if int(number) == sum_ : 
        print(f"{number} Detected! It's an Armstrong Number.")
    else:
        print(f"{number} is NOT an Armstrong Number.")
