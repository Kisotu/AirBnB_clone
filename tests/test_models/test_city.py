#!/usr/bin/python3
'''Test for city class'''

import unittest
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    def test_attribs(self):
        ct = City()
        self.assertEqual(ct.state_id, "")
        self.assertEqual(ct.name, "")

    def test_parrent(self):
        ct = City()
        self.assertTrue(isinstance(ct, BaseModel))
