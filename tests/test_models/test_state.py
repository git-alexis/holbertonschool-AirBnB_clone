#!/usr/bin/python3
""" Unittest for City """

import unittest
from models.base_model import BaseModel
from models.state import State


class testCity(unittest.TestCase):
    """ Test class for State """

    def test_class(self):
        """ Validate attributes type """
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(State, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(State.name, str)
