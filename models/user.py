#!/usr/bin/python3
"""a User class module"""
from models.base_model import BaseModel


class User(BaseModel):
    """manages User objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
