#!/usr/bin/python3
""" Unittest for State """

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Test class for State """

    def test_default_values(self):
        """ Validate default attribute values """
        state_instance = State()

        self.assertEqual(state_instance.name, "")


    def test_property_assignment(self):
        """ Validate attribute assignment """
        state_instance = State()

        state_instance.name = "California"
        self.assertEqual(state_instance.name, "California")


    def test_type_check(self):
        """ Validate attribute types """
        state_instance = State()

        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(state_instance.name, str)

if __name__ == "__main__":
    unittest.main()
