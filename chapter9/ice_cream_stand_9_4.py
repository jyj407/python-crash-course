class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine type of the restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is now open!!")

class IceCreamStand(Restaurant):
    """A simple attempt to model an Ice Cream Stand."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        print("Ice Cream Stand " + self.restaurant_name + " serves " + self.flavors + " flavors Ice Cream!")

my_restaurant = Restaurant("Old Code Seller", "Chinese Canadian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_ice_cream_stand = IceCreamStand("DQ", "Canadian", "Chocolate")
my_ice_cream_stand.describe_restaurant()
my_ice_cream_stand.open_restaurant()
my_ice_cream_stand.describe_flavors()

