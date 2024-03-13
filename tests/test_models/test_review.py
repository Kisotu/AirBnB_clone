#!/usr/bin/python3
'''Test for review class'''

import unittest
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    def test_string(self):
        rv = Review()
        self.assertEqual(rv.place_id, "")
        self.assertEqual(rv.user_id, "")
        self.assertEqual(rv.text, "")

    def test_parnt(self):
        rv = Review()
        self.assertTrue(isinstance(rv, BaseModel))
