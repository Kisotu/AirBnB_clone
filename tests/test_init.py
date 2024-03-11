#!/usr/bin/python3
'''Test for file storage'''

import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage


class Test_Storage(unittest.TestCase):
    def test_init(self):
        bs = BaseModel()
        self.assertEqual(bs.__class__, BaseModel)
        self.assertIsInstance(storage, FileStorage)
