"""-Define a function named my_fact to calculate factorial of the given number. 
    Given a non-negative integer return the factorial of the integer. 
    (Example: The factorial of 5 is: 5*4*3*2*1 = 120 and factorial of 0 is: 1)"""

""" To improve defining function skills and get familiar with the recursion concept."""

def my_fact(num):
    fact = 1
    
    if num == 0:
        return 1
    else:
        for i in range(1,num+1):
            fact *= i
        return fact
