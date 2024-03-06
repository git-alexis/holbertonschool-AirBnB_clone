#!/usr/bin/python3

""" Define FileStorage class | Serializes and deserializes a JSON file """

from models.base_model import BaseModel
from models.user import User
import json


class FileStorage():
    """ Serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
        __file_path: str - path to the JSON file
        __objects: dict - dictionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Add new object in __objects dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file """
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            # Read JSON file
            with open(self.__file_path, "r", encoding='utf-8') as file:
                data = json.load(file)
                # Iterate in deserialized data & creates instances
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    instance = eval(class_name)(**value)
                    # Stores them in a dictionary
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass
