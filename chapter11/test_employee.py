import unittest
from employee import Employee

class testEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('Shan', 'Zhang', 5000)

    def test_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 10000)

    def test_custom_raise(self):
        self.my_employee.give_raise(10000)
        self.assertEqual(self.my_employee.salary, 15000)



unittest.main()
