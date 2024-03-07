#!/usr/bin/python3
""" Unittest for City """

import unittest
from models.base_model import BaseModel
from models.review import Review


class testCity(unittest.TestCase):
    """ Test class for Review """

    def test_class(self):
        """ Validate attributes type """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)
