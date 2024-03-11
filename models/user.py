#!/usr/bin/python3
'''Defines a user model'''

from .base_model import BaseModel


class User(BaseModel):
    '''The blueprint for a user obj'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
