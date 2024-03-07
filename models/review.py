#!/usr/bin/python3

""" Review class module """


from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherit from BaseModel 
    Args:
    BaseModel : inheritance
    """
    place_id = str("")
    user_id = str("")
    text = str("")
