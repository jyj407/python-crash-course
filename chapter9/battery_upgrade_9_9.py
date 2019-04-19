class Car():
    """A simple attemp to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attribute to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer!") 

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehichles."""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""

        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        """Provide interface to upgrade the battery size"""

        if self.battery_size < 85:
            print("Now upgrade your battery to the maximum 85-kWh!")
            self.battery_size = 85

    def get_range(self):
        """Print a statement about the range this battery provides."""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_new_car.update_odometer(22)
my_new_car.read_odometer()
my_new_car.update_odometer(24089)
my_new_car.read_odometer()
my_new_car.increment_odometer(10000)
my_new_car.read_odometer()

my_tesla = ElectricCar('telsa', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.get_range()
my_tesla.upgrade_battery()
my_tesla.get_range()

