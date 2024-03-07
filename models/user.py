#!/usr/bin/python3

""" User class module """


from models.base_model import BaseModel


class User(BaseModel):
    """ Class User inherits from BaseModel """
    email = str("")
    password = str("")
    first_name = str("")
    last_name = str("")
