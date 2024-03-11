#!/usr/bin/python3
'''Test for State class'''

import unittest
from models.base_model import BaseModel
from models.state import State


class Test_State(unittest.TestCase):
    def test_string(self):
        st = State()
        self.assertEqual(st.name, "")

    def test_parnt(self):
        st = State()
        self.assertTrue(isinstance(st, BaseModel))
