def get_formatted(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
  
  """ When you call a function that returns a value, 
    you need to provide a variable that the return 
    value can be assigned to."""

musician = get_formatted("henry", "hendrix")
print(musician)

# Making an Argument Optional

def get_formatted_name(first_name, last_name, middle_name=""):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
        
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
