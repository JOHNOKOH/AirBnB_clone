#!/usr/bin/python3
"""a Review class module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """manages review objects"""

    place_id = ""
    user_id = ""
    text = ""
