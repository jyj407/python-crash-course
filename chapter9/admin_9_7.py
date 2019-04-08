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

class Admin(User):
    """A simply attempt to model an admin user."""

    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = privileges

    def show_privileges(self):
        print("Here are the Admin user privileges");
        for privilege in self.privileges:
            print(privilege)

user1 = User("Wukong", "Sun", "18000")
user1.describe_user()
user1.greet_user()

privileges = ["Can add post", "Can delete post", "Can ban user"]
user2 = Admin("Mouni", "Sijia", "36000000", privileges)
user2.describe_user()
user2.greet_user()
user2.show_privileges()
