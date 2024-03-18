#!/usr/bin/python3
'''Tests for TestHBNBCommand class'''

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import json
from io import StringIO
import re
import os


class TestHBNBCommand(unittest.TestCase):

    '''test HBNBCommand console'''

    attribute_values = {
        str: "foobar108",
        int: 1008,
        float: 1.08
    }

    reset_values = {
        str: "",
        int: 0,
        float: 0.0
    }

    test_random_attributes = {
        "string1": "kisote",
        "integer1": 2445,
        "float1": 89.3
    }

    def setUp(self):
        '''Sets up test cases'''

        if os.path.isfile("myfile.json"):
            os.remove("myfile.json")
        self.resetStorage()

    def resetStorage(self):
        '''reset storage data'''

        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help(self):
        '''Tests the help command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        st = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""
        self.assertEqual(st, f.getvalue())

    def test_help_EOF(self):
        '''tests the EOF command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        sf = 'Handle End Of File character\n'
        self.assertEqual(sf, f.getvalue())

    def test_help_quit(self):
        '''tests the quit command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        sf = 'exits the program\n'
        self.assertEqual(sf, f.getvalue())

    def test_help_create(self):
        '''tests the create command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        sf = 'Creates an instance\n'
        self.assertEqual(sf, f.getvalue())

    def test_help_show(self):
        '''tests the show command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        sf = 'Prints string representation of an instance\n'
        self.assertEqual(sf, f.getvalue())

    def test_help_destroy(self):
        '''tests the destroy command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        sf = 'Deletes instance based on the class name and id\n'
        self.assertEqual(sf, f.getvalue())

    def test_help_all(self):
        '''tests the all command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        sf = 'prints string representation of all instance\n'
        self.assertEqual(sf, f.getvalue())

    def test_help_count(self):
        '''tests the count command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        sf = 'Counts the instances of a class\n'
        self.assertEqual(sf, f.getvalue())

    def test_help_update(self):
        '''tests the update command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        sf = 'Updates an instance by adding or updating attribute\n'
        self.assertEqual(sf, f.getvalue())

    def test_do_quit(self):
        '''tests quit commmand'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        text = f.getvalue()
        self.assertTrue(len(text) == 0)
        self.assertEqual("", text)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit garbage")
        text = f.getvalue()
        self.assertTrue(len(text) == 0)
        self.assertEqual("", text)

    def test_do_EOF(self):
        '''tests EOF commmand'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        text = f.getvalue()
        self.assertTrue(len(text) == 1)
        self.assertEqual("\n", text)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF garbage")
        text = f.getvalue()
        self.assertTrue(len(text) == 1)
        self.assertEqual("\n", text)

    def test_emptyline(self):
        '''tests emptyline functionality'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        sf = ""
        self.assertEqual(sf, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        sf = ""
        self.assertEqual(sf, f.getvalue())

    def test_do_create(self):
        '''tests create for all classes'''

        for classname in self.valid_class():
            self.help_test_do_create(classname)

    def help_test_do_create(self, classname):
        '''helps test the create commmand'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        key = "{}.{}".format(classname, uid)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        self.assertTrue(uid in f.getvalue())

    def test_do_create_error(self):
        '''tests create command with errors'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create garbage")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

    def test_do_show(self):
        '''tests show all classes'''

        for classname in self.valid_class():
            self.help_test_do_show(classname)
            self.help_test_show_advanced(classname)

    def help_test_do_show(self, classname):
        '''tests the show command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show {} {}".format(classname, uid))
        sf = f.getvalue()[:-1]
        self.assertTrue(uid in sf)

    def test_do_show_error(self):
        '''tsts show command errors'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show garbage")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 6524359")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** no instance found **")

    def help_test_show_advanced(self, classname):
        '''helps test show() command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        sf = f.getvalue()
        self.assertTrue(uid in sf)

    def test_do_show_error_advanced(self):
        '''tests show() command plus errors'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".show()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.show()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("6524359")')
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** no instance found **")

    def test_do_destroy(self):
        '''tests destroy all classes'''

        for classname in self.valid_class():
            self.help_test_do_destroy(classname)
            self.help_test_destroy_advanced(classname)

    def help_test_do_destroy(self, classname):
        '''helps test destroy command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy {} {}".format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in f.getvalue())

    def test_do_destroy_error(self):
        '''tests destroy command plus errors'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy garbage")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 6524359")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** no instance found **")

    def help_test_destroy_advanced(self, classname):
        '''test the destroy command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.destroy("{}")'.format(classname, uid))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".all()")
        self.assertFalse(uid in f.getvalue())

    def test_do_destroy_error_advanced(self):
        '''tests destroy() command plus errors'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".destroy()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.destroy()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.destroy("6524359")')
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** no instance found **")

    def test_do_all(self):
        '''tests all classes'''

        for classname in self.valid_class():
            self.help_test_do_all(classname)
            self.help_test_all_advanced(classname)

    def help_test_do_all(self, classname):
        '''helps test all command'''

        uid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(uid, s)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(classname))
        s = f.getvalue()[:-1]
        self.assertTrue(len(s) > 0)
        self.assertIn(uid, s)

    def test_do_all_error(self):
        '''tests all command + errors'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all garbage")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

    def help_test_all_advanced(self, classname):
        '''helps test all command'''

        uid = self.create_class(classname)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("{}.all()".format(classname))
        sf = f.getvalue()[:-1]
        self.assertTrue(len(sf) > 0)
        self.assertIn(uid, sf)

    def test_do_all_error_advanced(self):
        '''tests all() command with errors'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.all()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

    def test_count_all(self):
        '''tests count for all classes'''

        # for classname in self.valid_class():
        #     self.test_count_adv(classname)
        pass

    # def test_count_adv(self, classname):
    #     '''helps test count() command'''

    #     for i in range(19):
    #         uid = self.create_class(classname)
    #     with patch('sys.stdout', new=StringIO()) as f:
    #         HBNBCommand().onecmd("{}.count()".format(classname))
    #     sf = f.getvalue()[:-1]
    #     self.assertTrue(len(sf) > 0)
    #     self.assertEqual(sf, '19')

    def test_do_count_with_error(self):
        '''tests count() command with errors'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.count()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".count()")

        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class name missing **")

    def test_update_1(self):
        '''Tests update basemodek'''

        classname = "BaseModel"
        attr = "foostr"
        val = "fooval"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_update_user(self):
        '''Tests update user'''

        classname = "User"
        attr = "foostr"
        val = "fooval"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_update_city(self):
        '''Tests update city'''

        classname = "City"
        attr = "foostr"
        val = "fooval"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_update_state(self):
        '''tests update state'''

        classname = "State"
        attr = "foostr"
        val = "fooval"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'

        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_update_amenity(self):
        '''tests update amenity'''

        classname = "Amenity"
        attr = "foostr"
        val = "fooval"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_update_review(self):
        '''tests update review'''

        classname = "Review"
        attr = "foostr"
        val = "fooval"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'

        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_update_place(self):
        '''tests update place'''

        classname = "Place"
        attr = "foostr"
        val = "fooval"
        uid = self.create_class(classname)
        cmd = '{}.update("{}", "{}", "{}")'
        cmd = cmd.format(classname, uid, attr, val)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        s = f.getvalue()
        self.assertEqual(len(s), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        s = f.getvalue()
        self.assertIn(attr, s)
        self.assertIn(val, s)

    def test_update_all(self):
        '''tests update command with all'''

        for classname, cls in self.valid_class().items():
            uid = self.create_class(classname)
            for attr, value in self.test_random_attributes.items():
                if type(value) is not str:
                    pass
                quotes = (type(value) == str)
                self.help_test_update(classname, uid, attr,
                                      value, quotes, False)
                self.help_test_update(classname, uid, attr,
                                      value, quotes, True)
            pass
            if classname == "BaseModel":
                continue
            for attr, attr_type in self.attributes()[classname].items():
                if attr_type not in (str, int, float):
                    continue
                self.help_test_update(classname, uid, attr,
                                      self.attribute_values[attr_type],
                                      True, False)
                self.help_test_update(classname, uid, attr,
                                      self.attribute_values[attr_type],
                                      False, True)

    def help_test_update(self, classname, uid, attr, val, quotes, func):
        '''tests update commmand'''

        FileStorage._FileStorage__objects = {}
        if os.path.isfile("myfile.json"):
            os.remove("myfile.json")
        uid = self.create_class(classname)
        value_str = ('"{}"' if quotes else '{}').format(val)
        if func:
            cmd = '{}.update("{}", "{}", {})'
        else:
            cmd = 'update {} {} {} {}'
        cmd = cmd.format(classname, uid, attr, value_str)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(cmd)
        text = f.getvalue()[:-1]
        self.assertEqual(len(text), 0)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('{}.show("{}")'.format(classname, uid))
        sf = f.getvalue()
        self.assertIn(str(val), sf)
        self.assertIn(attr, sf)

    def test_do_update_error_0(self):
        '''Tests update command with errors'''

        uid = self.create_class("BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update garbage")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 6534276893")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel {}'.format(uid))
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update BaseModel {} name'.format(uid))
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** value missing **")

    def test_do_update_error_1(self):
        '''tests update() command with errors'''

        uid = self.create_class("BaseModel")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(".update()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("garbage.update()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(6534276893)")
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("{}")'.format(uid))
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** attribute name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.update("{}", "name")'.format(uid))
        text = f.getvalue()[:-1]
        self.assertEqual(text, "** value missing **")

    def create_class(self, classname):
        '''makes a class for console tests'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(classname))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        return uid

    def help_load_dict(self, rep):
        '''tests dictionary equality'''

        regx = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        reslt = regx.match(rep)
        self.assertIsNotNone(reslt)
        s = reslt.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        dt = json.loads(s.replace("'", '"'))
        return dt

    def valid_class(self):
        '''returns a dictionary of valid classes'''

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        valid_class = {"BaseModel": BaseModel,
                       "User": User,
                       "State": State,
                       "City": City,
                       "Amenity": Amenity,
                       "Place": Place,
                       "Review": Review}
        return valid_class

    def attributes(self):
        '''returns valid attributes and types of classname'''

        attribs = {
            "BaseModel":
            {"id": str,
             "created_at": datetime.datetime,
             "updated_at": datetime.datetime},

            "User":
            {"email": str,
             "password": str,
             "first_name": str,
             "last_name": str},

            "State":
            {"name": str},

            "City":
            {"state_id": str,
             "name": str},

            "Amenity":
            {"name": str},

            "Place":
            {"city_id": str,
             "user_id": str,
             "name": str,
             "description": str,
             "number_rooms": int,
             "number_bathrooms": int,
             "max_guest": int,
             "price_by_night": int,
             "latitude": float,
             "longitude": float,
             "amenity_ids": list},

            "Review":
            {"place_id": str,
             "user_id": str,
             "text": str}
        }
        return attribs


if __name__ == "__main__":
    unittest.main()
