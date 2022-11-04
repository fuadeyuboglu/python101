fibonacci = [1, 1]
x = 0

for i in range(8):
    i = fibonacci[x] + fibonacci[x + 1]
    fibonacci.append(i)
    x += 1
    

print(fibonacci)

# Solution2
fibonacci = []
x = 0

for i in range(1, 11):
    if len(fibonacci) < 2:
        fibonacci.append(x+1)
        
    else:
        i = fibonacci[x] + fibonacci[x + 1]
        fibonacci.append(i)
        x += 1
        
    
print(fibonacci)
