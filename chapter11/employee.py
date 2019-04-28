class Employee():
    """Simulate an employee"""

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def give_raise(self, amount = 5000):
        self.salary += amount
