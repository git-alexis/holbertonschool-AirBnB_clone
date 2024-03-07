#!/usr/bin/python3
""" Unittest for file_storage """

import unittest
import json
import os.path
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """ Test class for the FileStorage class """

    def setUp(self):
        """ Set up test environment """
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """ Clean up test environment """
        file_path = self.storage._FileStorage__file_path
        if os.path.exists(file_path):
            os.remove(file_path)


    def test_file_path(self):
        """ Test file path """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_objects_dict(self):
        """ Test objects dictionary """
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)


    def test_all(self):
        """ Test all filestorage """
        instance = self.storage.all()
        self.assertIsNotNone(instance)
        self.assertIsInstance(instance, dict)

    def test_new(self):
        """ Test new filestorage """
        model = BaseModel()
        self.storage.new(model)
        obj_key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(obj_key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[obj_key], model)

    def test_save(self):
        """ Test save filestorage """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
        obj_key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(obj_key, data)
        self.assertEqual(data[obj_key], model.to_dict())

    def test_reload(self):
        """ Test reload filestorage """
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        obj_key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(obj_key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[obj_key].to_dict(), model.to_dict())

    def test_init(self):
        """ Test instance init"""
        self.assertIsInstance(self.storage._FileStorage__objects, dict)
        self.assertIsInstance(self.storage._FileStorage__file_path, str)


    def test_reload_with_invalid_json(self):
        """ Test reload with invalid JSON """
        with open(self.storage._FileStorage__file_path, 'w') as f:
            f.write("invalid json")
        with self.assertRaises(json.JSONDecodeError):
            self.storage.reload()

    def test_save_when_file_not_exist(self):
        """ Test save when file does not exist """
        file_path = self.storage._FileStorage__file_path
        os.remove(file_path) if os.path.exists(file_path) else None
        self.storage.save()
        self.assertTrue(os.path.exists(file_path))

    def test_save_when_file_empty(self):
        """ Test save when file is empty """
        with open(self.storage._FileStorage__file_path, 'w') as f:
            f.write("")
        self.storage.save()
        self.assertTrue(os.path.getsize(self.storage._FileStorage__file_path) > 0)


if __name__ == '__main__':
    unittest.main()
