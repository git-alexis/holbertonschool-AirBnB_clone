#!/usr/bin/python3

"""BaseModel class module"""


from uuid import uuid4
from datetime import datetime


class BaseModel:

    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initializes BaseModel instance
        Args:
            args: set of arguments
            kwargs: set of arguments with keywords
        """
        # if kwargs not empty: reconstruct instance from dictionary
        if kwargs:
            for key, value in kwargs.items():
                # Convert created_at and updated_at strings to datetime objects
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
            # if id not provided: generate a new one
            if "id" not in kwargs:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates updated_at attribute with current datetime"""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

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
