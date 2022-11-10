""" Ask user for an input. Evaluate the value of the word according to the dictionary you created."""

# Alternative 1
letters = list(" abcdefghijklmnopqrstuvwxyz")
numbers = list(range(0,28))

my_dict = dict(zip(letters,numbers))

word = input("Please enter any word: ").lower()
count = 0

for i in list(word):
    count += my_dict[i]
    
print(f"{word} = {count}")


# Alternative 2
def value_of_word(word):
    letters = list(" abcdefghijklmnopqrstuvwxyz")
    values = list(range(0,28))
    value_dict = dict(zip(letters,values))
    
    value = 0 
    
    for i in list(word.lower()):
        value += value_dict[i]
        
    print(f"{word} = {value}")
