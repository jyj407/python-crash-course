from admin import User, Admin

user1 = User("Wukong", "Sun", "18000")
user1.describe_user()
user1.greet_user()

privileges = ["Can add post", "Can delete post", "Can ban user"]
user2 = Admin("Mouni", "Sijia", "36000000", privileges)
user2.describe_user()
user2.greet_user()
user2.show_privileges()
