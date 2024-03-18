#!/usr/bin/python3

'''Defines the base model'''
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    '''Defines common attribs, methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''init instance'''

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''string rep whem printing instance'''

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''updates instance changes to storage'''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''Dictionary rep of an instance'''

        diction = self.__dict__.copy()
        diction["__class__"] = type(self).__name__
        diction["created_at"] = diction["created_at"].isoformat()
        diction["updated_at"] = diction["updated_at"].isoformat()

        return diction
