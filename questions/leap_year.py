year = int(input("Please enter a year to see whether it is a leap year or not: "))

mod4 = (year % 4 == 0)
mod100 = (year % 100 == 0)
mod400 = (year % 400 == 0)

if mod4 :
    if mod100 :
        if mod400 : 
            print(f"{year} is a leap year.")
        else :
            print(f"{year} is not a leap year.")
    else :
        print(f"{year} is a leap year.")
else :
    print(f"{year} is not a leap year.")
