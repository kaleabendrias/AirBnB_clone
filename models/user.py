#!/usr/bin/env python3
"""user class contained here"""
from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        """init method"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.pasword = ""
        self.first_name = ""
        self.last_name = ""
