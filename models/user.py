#!/usr/bin/python3

"""
this is a module that is used in housing the User subclass
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    this is user class used in creating user objects
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
