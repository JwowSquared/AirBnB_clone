#!/usr/bin/python3
"""
Module that contains the class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of the class Review"""
    place_id = ''
    user_id = ''
    text = ''
