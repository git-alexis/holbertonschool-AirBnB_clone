#!/usr/bin/python3

"""BaseModel class module"""


from uuid import uuid4
from datetime import datetime


class BaseModel:

    """BaseModel class"""

    def __init__(self):
        """Initializes a BaseModel instance"""
        self.name = ""
        self.my_number = 0
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates updated_at attribute with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of BaseModel instance"""
        return {
            "my_number": self.my_number,
            "name": self.name,
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "id": self.id,
            "created_at": self.created_at.isoformat()
        }
