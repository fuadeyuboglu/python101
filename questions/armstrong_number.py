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
