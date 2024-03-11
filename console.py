#!/usr/bin/python3
'''The AirBnb Console'''

import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    '''Entry to the command interpreter'''

    prompt = '(hbnb)'
    hbnb_classes = ['BaseModel', 'User', 'Place', 'State',
                    'City', 'Amenity', 'Review']
    dotcommnds = ['.all()', '.count()']

    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id
        '''

        if line == '':
            print('** class name missing **')
        elif line not in HBNBCommand.hbnb_classes:
            print('** class doesn\'t exist **')
        else:
            if line == 'BaseModel':
                objs = BaseModel()
            elif line == 'User':
                objs = User()
            elif line == 'Place':
                objs = Place()
            elif line == 'State':
                objs = State()
            elif line == 'City':
                objs = City()
            elif line == 'Amenity':
                objs = Amenity()
            elif line == 'Review':
                objs = Review()
            storage.save()
            print(objs.id)

    def do_show(self, line):
        '''Prints the string representation of an
        instance based on the class name and id'''

        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.hbnb_classes:
            print('** class doesn\'t exist **')
        else:
            if len(args) < 2:
                print('** instance id missing **')
            else:
                classname = args[0]
                obj_id = args[1]
                key = classname + '.' + obj_id
                try:
                    print(storage.all()[key])
                except KeyError:
                    print('** no instance found **')

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''

        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.hbnb_classes:
            print('** class doesn\'t exist **')
        else:
            if len(args) < 2:
                print('** instance id missing **')
            else:
                classname = args[0]
                obj_id = args[1]
                key = classname + '.' + obj_id
                try:
                    del storage.all()[key]
                    storage.save()
                except KeyError:
                    print('** no instance found **')

    def do_all(self, line):
        '''Prints all string representation of all instances
        based or not on the class name'''

        args = line.split()
        res = []
        if len(args) != 0:
            if args[0] not in HBNBCommand.hbnb_classes:
                print('** class doesn\'t exist **')
                return
            else:
                for key, value in storage.all().items():
                    if type(value).__name__ == args[0]:
                        res.append(value.__str__())
        else:
            for key, value in storage.all().items():
                res.append(value.__str__())
        print(res)

    def do_update(self, line):
        '''Updates an instance based on the class name
        and id by adding or updating attribute'''

        args = line.split()
        if line == '':
            print('** class name missing **')
        elif args[0] not in HBNBCommand.hbnb_classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')

        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')
        else:
            classname = args[0]
            obj_id = args[1]
            attrib = args[2]
            val = args[3]
            consts = ['id', 'created_at', 'updated_at']
            if attrib in consts:
                print('** attribute can\'t be updated **')
                return
            """
            string validity test begins (incomplete)
            """
            if val[0] == '"' and val[-1] == '"' or val[0] == "'":
                if val[0] != '"':
                    print("** A string argument must be between \
double quotes **")
                    return
                val = val[1:-1]
            else:
                try:
                    for ch in val:
                        if ch == '.':
                            val = float(val)
                            break
                    else:
                        val = int(val)
                except ValueError:
                    print("** A string argument must \
be between double quote **")
            if (attrib[0] == '"' and attrib[-1] == '"')\
               or attrib[0] == "'" or attrib[-1] == "'":
                if attrib[0] != '"' or attrib[-1] == "'":
                    print("** A string argument must be between \
double quotes **")
                    return
                attrib = attrib[1:-1]
            """ string validity test ends """
            key = classname + '.' + obj_id
            try:
                instance = storage.all()[key]
                instance.__dict__[attrib] = val
                instance.save()
            except KeyError:
                print('** no instance found **')

    def do_quit(self, line):
        '''Exit command'''
        return True

    def do_EOF(self, line):
        '''CTRL D - terminate program'''

        print()
        return True

    def do_emptyline(self):
        '''Empty arg - no execution'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
