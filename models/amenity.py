#!/usr/bin/python3
'''this defines the amenity model'''

from .base_model import BaseModel


class Amenity(BaseModel):
    '''The blueprint for amenity objects'''

    name = ""
