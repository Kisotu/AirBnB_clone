#!/usr/bin/python3
'''This definesa place model'''

from .base_model import BaseModel


class Place(BaseModel):
    '''Blueprint for the place objs'''

    city_id = ""
    name = ""
    description = ""
    user_id = ""
    amenity_ids = []
    number_rooms = 0
    number_bathrooms = 0
    price_by_night = 0
    max_guest = 0
    latitude = 0.0
    longitude = 0.0
