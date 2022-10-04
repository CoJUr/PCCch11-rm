import unittest
from name_function import get_formatted_name


# make class that inherits from unittest.TestCase
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work? Test for names with first +
        last format."""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    # if this file is run as the main program, __name__ will be set to __main__
    unittest.main()
    # if a testing framework is used to import this file, __name__ will be set
    # to the name of the file instead and so unittest.main() will not be run


