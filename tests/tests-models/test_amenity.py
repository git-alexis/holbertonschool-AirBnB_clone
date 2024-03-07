#!/usr/bin/python3
""" Unittest for Amenity """

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test class for Amenity """

    def test_default_values(self):
        """ Validate default attribute values """
        amenity_instance = Amenity()

        self.assertEqual(amenity_instance.name, "")


    def test_property_assignment(self):
        """ Validate attribute assignment """
        amenity_instance = Amenity()

        amenity_instance.name = "WiFi"
        self.assertEqual(amenity_instance.name, "WiFi")


    def test_type_check(self):
        """ Validate attribute types """
        amenity_instance = Amenity()

        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(amenity_instance.name, str)

if __name__ == "__main__":
    unittest.main()
