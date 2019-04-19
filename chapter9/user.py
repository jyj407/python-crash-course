class User():
    """A simply attempt to model a user."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("The first name of the user is " + self.first_name.title() + ".")
        print("The last name of the user is " + self.last_name.title() + ".")
        print("The user's age is " + self.age + ".")

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title()) 
