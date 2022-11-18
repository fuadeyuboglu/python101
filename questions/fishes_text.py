""" Write a code that inserts a newline char \n to 
    between lines of the text of the 'fishes.txt' file 
    and read the new content of that file. """

with open("fishes.txt", 'r', encoding = 'utf-8') as sea:
    fish_lines = sea.readlines()
    
with open("fishes.txt", 'w', encoding = 'utf-8') as sea:
    for reef in fish_lines:
        sea.write(reef + "\n")

with open("fishes.txt", 'r', encoding = 'utf-8') as sea:
    print(sea.read())
