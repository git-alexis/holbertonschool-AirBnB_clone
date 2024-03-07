#!/usr/bin/python3
""" Unittest for Place """

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Test class for Place """

    def test_default_values(self):
        """ Validate default attribute values """
        place_instance = Place()

        self.assertEqual(place_instance.city_id, "")
        self.assertEqual(place_instance.user_id, "")
        self.assertEqual(place_instance.name, "")
        self.assertEqual(place_instance.description, "")
        self.assertEqual(place_instance.number_rooms, 0)
        self.assertEqual(place_instance.number_bathrooms, 0)
        self.assertEqual(place_instance.max_guest, 0)
        self.assertEqual(place_instance.price_by_night, 0)
        self.assertEqual(place_instance.latitude, 0.0)
        self.assertEqual(place_instance.longitude, 0.0)
        self.assertEqual(place_instance.amenity_ids, [])


    def test_property_assignment(self):
        """ Validate attribute assignment """
        place_instance = Place()

        place_instance.city_id = "123"
        place_instance.user_id = "456"
        place_instance.name = "Cozy Apartment"
        place_instance.description = "A lovely place to stay"
        place_instance.number_rooms = 2
        place_instance.number_bathrooms = 1
        place_instance.max_guest = 4
        place_instance.price_by_night = 100
        place_instance.latitude = 40.7128
        place_instance.longitude = -74.0060
        place_instance.amenity_ids = ["wifi", "parking"]

        self.assertEqual(place_instance.city_id, "123")
        self.assertEqual(place_instance.user_id, "456")
        self.assertEqual(place_instance.name, "Cozy Apartment")
        self.assertEqual(place_instance.description, "A lovely place to stay")
        self.assertEqual(place_instance.number_rooms, 2)
        self.assertEqual(place_instance.number_bathrooms, 1)
        self.assertEqual(place_instance.max_guest, 4)
        self.assertEqual(place_instance.price_by_night, 100)
        self.assertEqual(place_instance.latitude, 40.7128)
        self.assertEqual(place_instance.longitude, -74.0060)
        self.assertEqual(place_instance.amenity_ids, ["wifi", "parking"])


    def test_type_check(self):
        """ Validate attribute types """
        place_instance = Place()

        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(place_instance.city_id, str)
        self.assertIsInstance(place_instance.user_id, str)
        self.assertIsInstance(place_instance.name, str)
        self.assertIsInstance(place_instance.description, str)
        self.assertIsInstance(place_instance.number_rooms, int)
        self.assertIsInstance(place_instance.number_bathrooms, int)
        self.assertIsInstance(place_instance.max_guest, int)
        self.assertIsInstance(place_instance.price_by_night, int)
        self.assertIsInstance(place_instance.latitude, float)
        self.assertIsInstance(place_instance.longitude, float)
        self.assertIsInstance(place_instance.amenity_ids, list)

if __name__ == "__main__":
    unittest.main()