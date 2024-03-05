#!/usr/bin/python3

""" Define FileStorage class """


from models.base_model import BaseModel


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

	def new(self, obj):
	
	def save(self):
	
	def reload(self):
