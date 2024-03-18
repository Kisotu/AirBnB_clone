#!/usr/bin/python3
'''Test for city class'''

import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from models.engine.file_storage import FileStorage
import os
from models import storage


class Test_City(unittest.TestCase):
    '''tests for city class'''

    def test_teardown(self):
        '''tears test methods'''

        self.resetStorage()
        pass

    def resetStorage(self):
        '''reset file storage'''

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        '''tests instantiation of city class'''

        bs = City()
        self.assertEqual(str(type(bs)), "<class 'models.city.City'>")
        self.assertIsInstance(bs, City)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test_attribs(self):
        '''tests city attributes'''

        attributes = storage.attributes()["City"]
        ct = City()
        for k, v in attributes.items():
            self.assertTrue(hasattr(ct, k))
            self.assertEqual(type(getattr(ct, k, None)), v)


if __name__ == '__main__':
    unittest.main()
