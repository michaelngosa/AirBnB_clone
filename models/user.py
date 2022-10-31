#!/usr/bin/python3
"""
User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """
        constructor
        """
        super().__init__(*args, **kwargs)
