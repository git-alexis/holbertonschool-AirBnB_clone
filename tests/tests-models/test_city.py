#!/usr/bin/python3
""" Unittest for City """

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Test class for City """

    def test_default_values(self):
        """ Validate default attribute values """
        city_instance = City()

        self.assertEqual(city_instance.state_id, "")
        self.assertEqual(city_instance.name, "")


    def test_property_assignment(self):
        """ Validate attribute assignment """
        city_instance = City()

        city_instance.state_id = "123"
        city_instance.name = "New York"

        self.assertEqual(city_instance.state_id, "123")
        self.assertEqual(city_instance.name, "New York")


    def test_type_check(self):
        """ Validate attribute types """
        city_instance = City()

        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(city_instance.state_id, str)
        self.assertIsInstance(city_instance.name, str)

if __name__ == "__main__":
    unittest.main()
