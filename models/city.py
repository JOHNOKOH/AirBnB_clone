#!/usr/bin/python3
"""User class module"""

from models.base_model import BaseModel


class City(BaseModel):
    """manages city objects"""

    state_id = ""
    name = ""
