#!/usr/bin/python3
'''Test for User class'''

import unittest
import os
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):

    '''Tests for the User class'''

    def test_teardown(self):
        '''tears test methods'''

        self.resetStorage()
        pass

    def resetStorage(self):
        '''reset storage'''

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        '''tests instantiation of User class'''

        usr = User()
        self.assertEqual(str(type(usr)), "<class 'models.user.User'>")
        self.assertIsInstance(usr, User)
        self.assertTrue(issubclass(type(usr), BaseModel))

    def test_attribs(self):
        '''tests attributes of User class'''

        attributes = storage.attributes()["User"]
        usr = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(usr, k))
            self.assertEqual(type(getattr(usr, k, None)), v)


if __name__ == "__main__":
    unittest.main()
