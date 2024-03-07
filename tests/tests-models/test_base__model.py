#!/usr/bin/python3
""" Unittest for City """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test class for BaseModel """

    def test_init(self):
        """ Test constructor """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str(self):
        """ Test string """
        model = BaseModel()
        model_str = str(model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn(model.id, model_str)        
    
    def test_save(self):
        """ Test save """
        model = BaseModel()
        previous_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(previous_updated_at, model.updated_at)


    def test_to_dict(self):
        """ test to dict """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_format(self):
        """ Test to_dict format """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

    def test_to_dict_contains(self):
        """ Test to_dict contains all keys/values """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue(all(key in model_dict for key in ('id', 'created_at', 'updated_at', '__class__')))
        self.assertTrue(all(model_dict[key] == getattr(model, key) for key in ('id', 'created_at', 'updated_at', '__class__')))

    def test_to_dict_datetime(self):
        """ Test to_dict datetime conversion """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

        created_at = datetime.strptime(model_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(model_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")

        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)

if __name__ == "__main__":
    unittest.main()
