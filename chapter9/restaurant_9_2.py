class Restaurant():
    """A simply attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title() + ".")
        print("The cuisine type of the restaurant is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is now open!!")


my_restaurant = Restaurant("Old Code Seller", "Chinese Canadian")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant = Restaurant("Dosa Haka", "Indian")
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

her_restaurant = Restaurant("Shawarma Stop", "Middle East")
her_restaurant.describe_restaurant()
her_restaurant.open_restaurant()
