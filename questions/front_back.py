"""Given a string, return a new string where the first and last chars have been exchanged."""

def front_back(word): 
    if len(word) >1:
        new_word = word[-1] + word[1:-1] + word[0]
        return new_word
    else:
        return word
