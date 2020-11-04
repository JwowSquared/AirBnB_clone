#!/usr/bin/python3
"""This module contains the class User"""

from models.base_model import BaseModel


class User(BaseModel):
    """This class contains information based on the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

#    def __init__(self, *args, **kwargs):
#        """initialises class User"""
#        super().__init__(*args, **kwargs)
