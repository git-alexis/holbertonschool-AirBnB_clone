#!/usr/bin/python3

""" Review class module """


from base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherit from BaseModel """
    place_id = str("")
    user_id = str("")
    text = str("")