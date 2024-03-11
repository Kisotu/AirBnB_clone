#!/usr/bin/python3
'''This defines the city model'''

from .base_model import BaseModel


class City(BaseModel):
    '''The blueprint for city objects'''

    state_id = ""
    name = ""
