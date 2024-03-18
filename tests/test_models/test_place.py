#!/usr/bin/python3
'''Test for place class'''

import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
import os
from datetime import datetime


class Test_Place(unittest.TestCase):
    '''tests for place class'''

    def test_teardown(self):
        '''tear test mthods'''

        self.resetStorage()
        pass

    def resetStorage(self):
        '''reset storage data'''

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        '''test instantiation of place class'''

        bs = Place()
        self.assertEqual(str(type(bs)), "<class 'models.place.Place'>")
        self.assertIsInstance(bs, Place)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test_attribs(self):
        '''tests place class attributes'''

        attributes = storage.attributes()["Place"]
        pl = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(pl, k))
            self.assertEqual(type(getattr(pl, k, None)), v)


if __name__ == "__main__":
    unittest.main()
