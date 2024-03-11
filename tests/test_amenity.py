#!/usr/bin/python3
'''Test for Amenity class'''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    def test_string(self):
        amt = Amenity()
        self.assertEqual(amt.name, "")

    def test_parent(self):
        amt = Amenity()
        self.assertTrue(isinstance(amt, BaseModel))
