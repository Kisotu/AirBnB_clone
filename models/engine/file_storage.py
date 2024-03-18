#!/usr/bin/python3
'''It serializes instance to json file and
deserilizes json file to instance'''

import json
import datetime
import os


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
        setkey = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[setkey] = obj

    def save(self):
        '''serializes __objects to json fiele path'''
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            dt = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dt, f)

    def classes(self):
        '''Returns dict of valid classes and references'''
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        '''deserializes json file to __objects'''
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") \
                    as my_file:
                dict_obj = json.loads(my_file.read())
            final_dict = {}

            for id, dictionary in dict_obj.items():
                class_name = dictionary['__class__']
                final_dict[id] = self.classes()[class_name](**dictionary)
            FileStorage.__objects = final_dict

    def attributes(self):
        '''Returns valid attributes and types for classname'''
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
