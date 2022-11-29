import random 
random.randint(1,30)

uppers = [chr(random.randint(65, 90)) for i in range(3)]
lowers = [chr(random.randint(97, 122)) for i in range(3)]
numbers = [chr(random.randint(48, 57)) for i in range(3)]
chars = chr(random.randint(33, 47)) + chr(random.randint(58, 64))

password = "".join(uppers) + "".join(lowers) + "".join(numbers) + chars

def mixer(x):
    templist = list(x)
    random.shuffle(templist)
    return "".join(templist)

print(mixer(password))
