#!/usr/bin/python3
'''Test for State class'''

import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage


class Test_State(unittest.TestCase):
    '''Tests for State class'''

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
        '''test instantiation of state class'''

        st = State()
        self.assertEqual(str(type(st)), "<class 'models.state.State'>")
        self.assertIsInstance(st, State)
        self.assertTrue(issubclass(type(st), BaseModel))

    def test_attribs(self):
        '''tests attributes of state class'''

        attributes = storage.attributes()["State"]
        st = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(st, k))
            self.assertEqual(type(getattr(st, k, None)), v)


if __name__ == "__main__":
    unittest.main()
