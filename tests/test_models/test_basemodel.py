#!/usr/bin/python3
'''Test for Base Model'''

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
import unittest
import json
import os
import re
import time
import uuid


class Test_BaseModel(unittest.TestCase):
    '''Base Model unittest'''

    def test_test(self):
        '''tests tear down'''

        self.resetStorage()
        pass

    def resetStorage(self):
        '''resets file storage'''
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        '''tests instantiation'''

        b = BaseModel()
        self.assertEqual(str(type(b)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_init_noargs(self):
        # '''tests init without args'''

        # self.resetStorage()
        # with self.assertRaises(TypeError) as e:
        #     BaseModel.__init__()
        # text = "__init__() missing 1 required positional argument: 'self'"
        # self.assertEqual(str(e.exception), text)
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_init_args(self):
        '''tests init with args'''

        self.resetStorage()
        args = [i for i in range(1000)]
        bs = BaseModel(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        bs = BaseModel(*args)

    def test_attribs(self):
        '''test atribs for instance of BM class'''

        attribs = storage.attributes()["BaseModel"]
        bs = BaseModel()
        for k, v in attribs.items():
            self.assertTrue(hasattr(bs, k))
            self.assertEqual(type(getattr(bs, k, None)), v)

    def test_date_created(self):
        '''tests updated_at && created_at'''

        date_now = datetime.now()
        bs = BaseModel()
        diff = bs.updated_at - bs.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = bs.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id(self):
        '''tests uniq ids'''

        uniq = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(uniq)), len(uniq))

    def test_save(self):
        '''tests mthod save()'''

        bs = BaseModel()
        time.sleep(0.5)
        date_now = datetime.now()
        bs.save()
        diff = bs.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_str(self):
        '''tests __str__()'''

        bm = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(bm))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), bm.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = bm.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_to_dict(self):
        '''tests to_dict()'''

        bs = BaseModel()
        bs.name = "Laura"
        bs.age = 23
        d = bs.to_dict()
        self.assertEqual(d["id"], bs.id)
        self.assertEqual(d["__class__"], type(bs).__name__)
        self.assertEqual(d["created_at"], bs.created_at.isoformat())
        self.assertEqual(d["updated_at"], bs.updated_at.isoformat())
        self.assertEqual(d["name"], bs.name)
        self.assertEqual(d["age"], bs.age)

    # def test_to_dict_noargs(self):
    #     '''tests to_dict() without args'''

    #     self.resetStorage()
    #     with self.assertRaises(TypeError) as e:
    #         BaseModel.to_dict()
    #     txt = "to_dict() missing 1 required positional argument: 'self'"
    #     self.assertEqual(str(e.exception), txt)

    # def test_to_dict_many_args(self):
    #     '''tests to_dict too many args'''

    #     self.resetStorage()
    #     with self.assertRaises(TypeError) as e:
    #         BaseModel.to_dict(self, 68)
    #     txt = "to_dict() takes 1 positional argument but 2 were given"
    #     self.assertEqual(str(e.exception), txt)

    def test_init_kwargs(self):
        '''test instantiation with kwargs'''

        my_model = BaseModel()
        my_model.name = "Maunda"
        my_model.my_number = 56
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_new_model.to_dict(), my_model.to_dict())

    def test_init_dict(self):
        '''tests init with kwargs from custom dictionary'''

        my_dict = {"__class__": "BaseModel",
                   "updated_at":
                   datetime(2043, 11, 14, 13, 49, 44, 146431).isoformat(),
                   "created_at": datetime.now().isoformat(),
                   "id": uuid.uuid4(),
                   "var": "barcode",
                   "int": 156,
                   "float": 3.14}

        o = BaseModel(**my_dict)
        self.assertEqual(o.to_dict(), my_dict)

    def test_save_called_from(self):
        '''tests where save is called from'''

        self.resetStorage()
        bs = BaseModel()
        bs.save()
        key = "{}.{}".format(type(bs).__name__, bs.id)
        d = {key: bs.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def save_no_args(self):
        '''test save, no args'''

        self.resetStorage()
        with self.assertRaises(TypeError) as e:
            BaseModel.save()
        txt = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), txt)

    # def test_save_many_args(self):
    #     '''tests save, too mnay args'''

    #     self.resetStorage()
    #     with self.assertRaises(TypeError) as e:
    #         BaseModel.save(self, 98)
    #     txt = "save() takes 1 positional argument but 2 were given"
    #     self.assertEqual(str(e.exception), txt)


if __name__ == "__main__":
    unittest.main()
