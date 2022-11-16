# Passing an Arbitrary Number of Arguments

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
    
""" The asterisk in the parameter name *toppings tells Python
    to make an empty tuple called toppings and pack whatever values
    it receives into this tuple.
    Note that Python packs the arguments into a tuple, even if the 
    function receives only one value. """

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
        
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing positional and arbitrary arguments

""" If you want to accept several different kinds of arguments,
    the parameter that accepts an arbitrary number of arguments 
    must be placed last in the function definiton."""

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
        
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
