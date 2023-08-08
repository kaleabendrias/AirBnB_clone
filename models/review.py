#!/usr/bin/python3

"""
this module contains the Review class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    contains the amenities of user
    """
    place_id = ""
    user_id = ""
    text = ""
