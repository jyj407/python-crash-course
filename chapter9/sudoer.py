from user import User

class Admin(User):
    """A simply attempt to model an admin user."""

    def __init__(self, first_name, last_name, age, privileges):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        print("Here are the Admin user privileges");
        for privilege in self.privileges:
            print(privilege)

class Privileges:
    """A simply attempt to model the privileges an admin user can have."""
    
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Here are the Admin user privileges");
        for privilege in self.privileges:
            print(privilege)


