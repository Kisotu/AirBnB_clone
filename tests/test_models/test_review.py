#!/usr/bin/python3
'''Test for review class'''

import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


class Test_Review(unittest.TestCase):
    '''tests for Review class'''

    def test_tearDown(self):
        '''tears test methods'''

        self.resetStorage()
        pass

    def resetStorage(self):
        '''reset storage data'''

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_init(self):
        '''tests instantiation of review class'''

        bs = Review()
        self.assertEqual(str(type(bs)), "<class 'models.review.Review'>")
        self.assertIsInstance(bs, Review)
        self.assertTrue(issubclass(type(bs), BaseModel))

    def test_attribs(self):
        '''tests attributes of review class'''

        attributes = storage.attributes()["Review"]
        rv = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(rv, k))
            self.assertEqual(type(getattr(rv, k, None)), v)


if __name__ == "__main__":
    unittest.main()
