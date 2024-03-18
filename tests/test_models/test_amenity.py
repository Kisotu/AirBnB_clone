#!/usr/bin/python3
'''Test for Amenity class'''

import unittest
from datetime import datetime
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
import os


class Test_Amenity(unittest.TestCase):
    def test_test(self):
        '''tears down test funcs'''
        self.resetStorage()
        pass

    def resetStorage(self):
        '''Resets FileStorage'''

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        '''tests instantiation'''

        am = Amenity()
        self.assertEqual(str(type(am)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(am, Amenity)
        self.assertTrue(issubclass(type(am), BaseModel))

    def test_attribs(self):
        '''tests attributes'''

        attributes = storage.attributes()["Amenity"]
        am = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(am, k))
            self.assertEqual(type(getattr(am, k, None)), v)


if __name__ == "__main__":
    unittest.main()
