#!/usr/bin/python3
'''Test for File Storage engine'''

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class TestFileStorage(unittest.TestCase):
    def test_private_attr(self):
        bs = BaseModel()
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            file_path = storage.file_path
        with self.assertRaises(AttributeError):
            file_path = storage.__file_path
        with self.assertRaises(AttributeError):
            file_path = storage.objects
        with self.assertRaises(AttributeError):
            file_path = storage.__objects

        with self.assertRaises(AttributeError):
            FileStorage.file_path
        with self.assertRaises(AttributeError):
            FileStorage.__file_path
        with self.assertRaises(AttributeError):
            FileStorage.objects
        with self.assertRaises(AttributeError):
            FileStorage.__objects

    def test_reload(self):
        storage1 = FileStorage()
        bs1 = BaseModel({id: 8})
        bs1.save()
        storage.save()
        self.assertEqual(storage.reload(), None)

    def test_a(self):
        storage1 = FileStorage()
        self.assertIsInstance(storage1.all(), dict)

    def test_b(self):
        storage1 = FileStorage()
        bs = BaseModel()
        storage1.new(bs)
        key = type(bs).__name__ + '.' + bs.id
        self.assertEqual(storage1.all()[key], bs)
