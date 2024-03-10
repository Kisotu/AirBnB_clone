#!/usr/bin/python3

'''Defines the base model'''
from datetime import datetime
import uuid


class BaseModel:
    '''Defines common attribs, methods for other classes'''

    def __init__(self, *args, **kwargs):
        '''init instance'''

        if kwargs is not None and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        '''string rep whem printing instance'''

        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        '''updates instance changes to storage'''

        self.__dict__.update({'updated_at': datetime.now()})
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        '''Dictionary rep of an instance'''

        diction = dict(self.__dict__)
        diction.update({'__class__': type(self).__name__,
                        'updated_at': self.updated_at.isoformat(),
                        'id': self.id,
                        'created_at': self.created_at.isoformat()})

        return diction
