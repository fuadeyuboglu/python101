"""- Given a list, return the most frequent (repeating) element.
- **Note** : If there are the same number of repeating elements, it returns the first element that repeats most from left to right in the list."""

""" This code does not returns the first element that repeats most from left to right in the list."""


def most_freq(*listem): 
    for i in listem:
        return max(set(listem), key=listem.count)
       
