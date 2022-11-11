""" Count the number of each letter in a sentence.
- The The department you work for undertook a project construction that makes word / text analysis. 
You are asked to calculate the number of letters or any chars in the sentences entered under this project.
- Write a Python program that;

  1. takes a sentence from the user,
  2. counts the number of each letter/chars of the sentence,
  3. collects the letters/chars as a key and the counted numbers as a value in a dictionary."""


def letters_count(n) :
    
    letters = list(n)
    chars = set(n)
    count = {}
    
    for i in chars:
        count[i] = letters.count(i)
        
    print(count)
