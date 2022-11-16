# Modifying a list in a function

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
       Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Pringint model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_mmodels):
    """Show all the models that were printed."""
    i = 1
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(f"{i}. {completed_model}")
        i += 1
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

""" Every function should have one specific job.
    If you're writing a function and notice the function
    is doing too many different tasks,
    try tp split the code into two functions. """

# Preventing a function from modifying a list

""" You can send a copy of a list to a function like this:
    function_name(list_name[:]) 
    The slice notation [:] makes a copy of the list to send to the function."""
