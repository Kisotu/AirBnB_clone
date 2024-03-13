#!/usr/bin/python3
'''Test for Base Model'''

import uuid
from datetime import datetime
import unittest
from base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    '''Base Model unittest'''

    def test_string(self):
        '''checks string rep of instance'''
        bs = BaseModel()
        self.assertEqual(bs.__str__(),
                         f"[{type(bs).__name__}] ({bs.id}) {bs.__dict__}")

    def test_todict(self):
        bs = BaseModel()
        update_time = bs.updated_at
        self.assertDictEqual(bs.to_dict(),
                             {'__class__': type(bs).__name__,
                              'updated_at': bs.updated_at.isoformat(),
                              'id': bs.id,
                              'created_at': bs.created_at.isoformat()})
        bs.save()
        self.assertNotEqual(update_time, bs.updated_at)

    def test_attrib_classes(self):
        '''checks for correct attribs used'''

        bs = BaseModel()
        bs2 = BaseModel()
        self.assertIsInstance(bs.id, str)
        self.assertIsInstance(bs.created_at, datetime)
        self.assertIsInstance(bs.updated_at, datetime)
        self.assertNotEqual(bs.id, bs2.id)

    def test_save(self):
        '''Test saving instance to file'''

        bs = BaseModel()
        update_time = bs.updated_at
        bs.save()
        new_time = bs.updated_at
        self.assertNotEqual(update_time, new_time)


if __name__ == "__main__":
    unittest.main()
