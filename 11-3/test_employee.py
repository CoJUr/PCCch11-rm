"""A test case for the employee class."""

from employee import Employee
import unittest


class EmployeeTestCase(unittest.TestCase):
    """Tests for the Employee's methods"""

    def setUp(self):
        """Initialize an employee instance."""
        self.zizz = Employee('zizz', 'zazz', 100000)

    def test_give_default_raise(self):
        """Test that the default raise is $5000."""
        self.zizz.give_raise()

        self.assertEqual(self.zizz.salary, 105000)

    def test_give_custom_raise(self):
        """Test that a custom raise can be given."""
        self.zizz.give_raise(7500)

        self.assertEqual(self.zizz.salary, 107500)


