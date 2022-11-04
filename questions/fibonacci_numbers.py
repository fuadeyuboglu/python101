# Alternative 1

fibo = [1, 1]

for i in range(8):
    fibo.append(fibo[i] + fibo[i + 1])
    
print(fibo)

# Alternative 2

fibo = []

for i in range(1, 9):
    
    if len(fibo) < 2:
        fibo.append(i+1)
        
    else:
        fibo.append(fibo[-1] + fibo[-2])
            
print(fibo)

# Alternative 3

fibonacci = []
x, y = 1, 1

while x <= 55:
    fibonacci.append(x)
    x, y = y, (x + y)
    
print(fibonacci) 

# Alternative 4

def fibonacci(n):
    fibo = [1,1]
    
    for i in range(2, n):
        next_num = fibo[-1] + fibo[-2]
        fibo.append(next_num)
    return fibo
print('fibonacci numbers: ', fibonacci(10)) 
