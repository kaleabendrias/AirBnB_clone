#!/usr/bin/python3

"""
this module contains the city  class
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    contains the city of user
    """
    state_id = ""
    name = ""
