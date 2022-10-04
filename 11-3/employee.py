"""
An employee class with a name and salary attributes, and a give_raise()
which increments the salary by a given amount. Also a test case for the
class to test the give_raise() method.
"""


class Employee:
    """A simple representation of an employee for testing purposes."""

    def __init__(self, first_name, last_name, salary):
        """Initialize the employee attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise of $5k by default."""
        self.salary += amount


# me = Employee('josh', 'harris', 100000)
# print(me.salary)
#
# me.give_raise()
# print(me.salary)
# me.give_raise(10000)
# print(me.salary)