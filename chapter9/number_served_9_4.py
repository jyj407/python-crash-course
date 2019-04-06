class Restaurant():
    """A simply attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine type of the restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is now open!!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served_one_day):
        self.number_served += number_served_one_day
        

my_restaurant = Restaurant("Old Code Seller", "Chinese Canadian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print("Number of customers have been served: " + str(my_restaurant.number_served))
my_restaurant.number_served = 12
print("Number of customers have been served: " + str(my_restaurant.number_served))
my_restaurant.set_number_served(1001)
print("Number of customers have been served: " + str(my_restaurant.number_served))
my_restaurant.increment_number_served(100)
print("Number of customers have been served: " + str(my_restaurant.number_served))




