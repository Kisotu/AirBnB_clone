#!/usr/bin/python3
'''It serializes instance to json file and
deserilizes json file to instance'''

import json
from datetime import datetime
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    '''Serializes instance to json file and
    deserializes json file to instance'''

    __file_path = 'myfile.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key'''
        setkey = type(obj).__name__ + '.' + obj.id
        FileStorage.__objects[setkey] = obj

    def save(self):
        '''serializes __objects to json fiele path'''
        with open(FileStorage.__file_path, 'w+') as f:
            dict_objs = {}
            for key, value in FileStorage.__objects.items():
                dict_objs[key] = value.to_dict()
            json.dump(dict_objs, f)

    def reload(self):
        '''deserializes json file to __objects'''
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dict_objs = json.loads(f.read())
                from models.base_model import BaseModel
                from models.user import User
                for key, value in dict_objs.items():
                    if value['__class__'] == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value['__class__'] == 'User':
                        FileStorage.__objects[key] = User(**value)
                    elif value['__class__'] == 'Place':
                        FileStorage.__objects[key] = Place(**value)
                    elif value['__class__'] == 'State':
                        FileStorage.__objects[key] = State(**value)
                    elif value['__class__'] == 'City':
                        FileStorage.__objects[key] = City(**value)
                    elif value['__class__'] == 'Amenity':
                        FileStorage.__objects[key] = Amenity(**value)
                    elif value['__class__'] == 'Review':
                        FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
