#!/usr/bin/python3
""" Unittest for Review """

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Test class for Review """

    def test_default_values(self):
        """ Validate default attribute values """
        review_instance = Review()

        self.assertEqual(review_instance.place_id, "")
        self.assertEqual(review_instance.user_id, "")
        self.assertEqual(review_instance.text, "")


    def test_property_assignment(self):
        """ Validate attribute assignment """
        review_instance = Review()

        review_instance.place_id = "123"
        review_instance.user_id = "456"
        review_instance.text = "Cool"

        self.assertEqual(review_instance.place_id, "123")
        self.assertEqual(review_instance.user_id, "456")
        self.assertEqual(review_instance.text, "Cool")


    def test_type_check(self):
        """ Validate attribute types """
        review_instance = Review()

        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(review_instance.place_id, str)
        self.assertIsInstance(review_instance.user_id, str)
        self.assertIsInstance(review_instance.text, str)

if __name__ == "__main__":
    unittest.main()