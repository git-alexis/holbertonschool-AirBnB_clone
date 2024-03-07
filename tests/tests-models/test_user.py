#!/usr/bin/python3
""" Unittest for City """

import unittest
from models.user import User
from models.base_model import BaseModel


class testCity(unittest.TestCase):
    """ Test class for User """

    def test_values(self):
        """ Test default values (empty) """
        user_instance = User()

        self.assertEqual(user_instance.email, "")
        self.assertEqual(user_instance.password, "")
        self.assertEqual(user_instance.first_name, "")
        self.assertEqual(user_instance.last_name, "")


    def test_assignment(self):
        """ Validate attributes type after assignment """
        user_instance = User()

        user_instance.email = "email@email.com"
        user_instance.password = "password"
        user_instance.first_name = "Alexis"
        user_instance.last_name = "Billemont"

        self.assertEqual(user_instance.email, "email@email.com")
        self.assertEqual(user_instance.password, "password")
        self.assertEqual(user_instance.first_name, "Alexis")
        self.assertEqual(user_instance.last_name, "Billemont")


    def test_type_check(self):
        """ Validate attribute types """
        user_instance = User()

        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(user_instance.email, str)
        self.assertIsInstance(user_instance.password, str)
        self.assertIsInstance(user_instance.first_name, str)
        self.assertIsInstance(user_instance.last_name, str)

if __name__ == "__main__":
    unittest.main()