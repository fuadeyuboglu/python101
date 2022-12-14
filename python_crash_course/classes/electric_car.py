class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, milage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

""" The super() function is a special function that allows you to call a method
    from the parent class. This tells Python to call the __init__() method from Car,
    which gives an ElectricCar instance all the attributes defined in that method.
    The name super comes from a convention of calling the parent class a superclass
    and the child class a subclass."""

# Defining attributes and methods for the child class

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self,make,model,year):
        """ Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car."""
        super().__init__(make,model,year)
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# Overriding methods from the parent class

""" Say the class Car had a method called fill_gas_tank(). This method
    is meaningless for an all-electric vehicle, so you might want to override
    this method. """

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self,make,model,year):
        """ Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car."""
        super().__init__(make,model,year)
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        
# Instances as attributes

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self,battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")
        
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self,make,model,year):
        """ Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car."""
        super().__init__(make,model,year)
        self.battery = Battery()
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
        

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

