#!/usr/bin/python3
'''Test for place class'''

import unittest
from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    def test_str(self):
        pl = Place()
        self.assertEqual(pl.city_id, "")
        self.assertEqual(pl.user_id, "")
        self.assertEqual(pl.name, "")
        self.assertEqual(pl.description, "")
        self.assertEqual(pl.number_rooms, 0)
        self.assertEqual(pl.number_bathrooms, 0)
        self.assertEqual(pl.max_guest, 0)
        self.assertEqual(pl.price_by_night, 0)
        self.assertEqual(pl.latitude, 0.0)
        self.assertEqual(pl.longitude, 0.0)
        self.assertEqual(pl.amenity_ids, [])

    def test_parent(self):
        p = Place()
        self.assertTrue(isinstance(pl, BaseModel))
