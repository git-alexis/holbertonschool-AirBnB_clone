#!/usr/bin/python3

""" City class module """


from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherit from BaseModel
    Args:
    BaseModel : inheritance
    """
    state_id = str("")
    name = str("")
