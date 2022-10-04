"""Test the city_functions.py module."""
import unittest
from city_country import location_stringer


class LocationTestCase(unittest.TestCase):
    """Tests for 'city_country.py'."""

    def test_city_country(self):
        """Do locations like 'Santiago, Chile' work?"""
        formatted_location = location_stringer('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')

    def test_city_country_population(self):
        """Do locations like 'Santiago, Chile - population=500000' work?"""
        formatted_location = location_stringer('santiago', 'chile', 500000)
        self.assertEqual(formatted_location, 'Santiago, Chile - population 500000')


if __name__ == '__main__':
    unittest.main()