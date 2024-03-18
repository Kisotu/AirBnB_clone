#!/usr/bin/python3
'''Defines review model'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''The blueprint for a review obj'''

    user_id = ""
    place_id = ""
    text = ""
