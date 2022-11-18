""" Instantiation: Making an object from a class. """
""" Capitalized names refer to classes in Python. """

class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self,name,age):
        """Initiazlize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        

# Making an instance from a class

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Calling methods

my_dog.sit()
my_dog.roll_over()
