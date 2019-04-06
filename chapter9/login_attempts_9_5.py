class User():
    """A simply attempt to model a user."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("The first name of the user is " + self.first_name.title() + ".")
        print("The last name of the user is " + self.last_name.title() + ".")
        print("The user's age is " + self.age + ".")

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title()) 

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def login(self):
        self.increment_login_attempts()


user1 = User("Wukong", "Sun", "18000")
user1.describe_user()
user1.greet_user()
user1.login()
user1.login()
print("User1 have logined in " + str(user1.login_attempts) + " times.")
user1.reset_login_attempts()
print("After resetting, user1 have logined in " + str(user1.login_attempts) + " times.")
