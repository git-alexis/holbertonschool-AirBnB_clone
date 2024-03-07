#!/usr/bin/python3

""" City class module """


from base_model import BaseModel


class City(BaseModel):
    """ City class that inherit from BaseModel """
    state_id = str("")
    name = str("")
