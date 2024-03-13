#!/usr/bin/python3
'''Test for User class'''

import unittest
from models.base_model import BaseModel
from models.user import User


class Test_User(unittest.TestCase):
    def test_attrib(self):
        usr = User()
        self.assertEqual(usr.first_name, '')
        self.assertEqual(usr.last_name, '')
        self.assertEqual(usr.email, '')
        self.assertEqual(usr.password, '')

        self.assertEqual(User.first_name, '')
        self.assertEqual(User.last_name, '')
        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')

    def test_string(self):
        usr = User()
        self.assertEqual(usr.__class__, User)

    def test_parnt(self):
        usr = User()
        self.assertTrue(isinstance(usr, BaseModel))
