#!/usr/bin/python3

"""
the main file of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ The main class of the AirBnb console"""
    prompt = "(hbnb) "
    dictOfClasses = {"BaseModel": BaseModel(), "User": User(),
                     "Place": Place(), "State": State(), "City": City(),
                     "Amenity": Amenity(), "Review": Review()}

    def do_exit(self, arg):
        """Exits the cmd interpreter """
        return True

    def do_EOF(self, arg):
        """ Exits the command interpreter """
        return True

    def emptyline(self):
        """ do nothing when an emptyline is entered """
        return False

    @classmethod
    def check_arg_if_passed(self, arg):
        """
        checks if the  class exists
        """
        if not arg:
            print("** class name missing **")
            return 0

    @classmethod
    def check_multiple_arg_passed(cls, listOfArg):
        """
        checks if the two arg are passed
        """
        if listOfArg[0] in HBNBCommand.dictOfClasses.keys():
            try:
                # checks out if the argument exists
                if listOfArg[1]:
                    pass
            except IndexError:
                print("** instance id missing **")
                return (0)
            return (1)
        else:
            print("** class doesn't exist **")

    @classmethod
    def dict_to_str(cls, dictOfObj):
        """
        receive a dictionary of Objects and changes it to a string
        """
        listOfObj = []
        for key, value in dictOfObj.items():
            splitKey = key.split(".")
            my_string = f'[{splitKey[0]}] ({splitKey[1]}) {value}'
            listOfObj.append(my_string)
        return listOfObj

    @classmethod
    def get_obj_of_a_class(cls, dictOfAllObjects, specifiedClass):
        """ gets all objects for a specific class """
        objectsDictionary = {}
        for key in dictOfAllObjects.keys():
            if dictOfAllObjects[key]["__class__"] == specifiedClass:
                objectsDictionary[key] = dictOfAllObjects[key]
        return (objectsDictionary)

    @classmethod
    def strip_char(cls, string, char_to_remove):
        """
        removes certain characters and returns back the string
        """
        return ''.join(char for char in string if char not in char_to_remove)

    def do_create(self, arg):
        """ creates a new instance of a class"""
        if HBNBCommand.check_arg_if_passed(arg) == 0:
            return
        try:
            if arg in HBNBCommand.dictOfClasses:
                arg = HBNBCommand.dictOfClasses[arg]
            storage.new(arg)
            storage.save()
            print(arg.id)
        except Exception:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """  prints the string representation of an instance
        based on the class name and id """
        if HBNBCommand.check_arg_if_passed(arg) == 0:
            return
        # arg must be broken since the cmd module does not allow multiple arg
        listOfArg = arg.split()
        if HBNBCommand.check_multiple_arg_passed(listOfArg) == 1:
            storage.reload()
            dictOfObj = storage.all()
            key = f"{listOfArg[0]}.{listOfArg[1]}"
            if key not in dictOfObj.keys():
                print("** no instance found **")
                return
            listOfStrings = HBNBCommand.dict_to_str(dictOfObj)
            print(listOfStrings[0])

    def do_destroy(self, arg):
        """ deletes the existence of an instance """
        if HBNBCommand.check_arg_if_passed(arg) == 0:
            return
        # arg must be broken since the cmd module does not multiple arg
        listOfArg = arg.split()
        if HBNBCommand.check_multiple_arg_passed(listOfArg) == 1:
            storage.reload()
            dictOfObj = storage.all()
            key = f"{listOfArg[0]}.{listOfArg[1]}"
            if key not in dictOfObj.keys():
                print("** no instance found **")
                return
            del dictOfObj[key]
            storage.save()

    def do_all(self, arg):
        """ prints all objects in the json file """
        if not arg:
            pass
        elif arg == "BaseModel":
            pass
        elif arg in HBNBCommand.dictOfClasses.keys():
            dictOfObj = storage.all()
            my_dict = HBNBCommand.get_obj_of_a_class(dictOfObj, arg)
            listOfStrings = HBNBCommand.dict_to_str(my_dict)
            print(listOfStrings)
            return
        else:
            print("** class doesn't exist **")
            return
        storage.reload()
        dictOfObj = storage.all()
        listOfStrings = HBNBCommand.dict_to_str(dictOfObj)
        print(listOfStrings)

    def do_update(self, arg):
        """ updates an instance based on class name and id """
        if HBNBCommand.check_arg_if_passed(arg) == 0:
            return
        # arg must be broken since the cmd module does not multiple arg
        listOfArg = arg.split()
        if HBNBCommand.check_multiple_arg_passed(listOfArg) == 1:
            storage.reload()
            dictOfObj = storage.all()
            key = f"{listOfArg[0]}.{listOfArg[1]}"
            if key not in dictOfObj.keys():
                print("** no instance found **")
                return
            if len(listOfArg) == 2:
                print("** attribute name missing **")
                return
            if len(listOfArg) == 3:
                print("** value missing **")
                return
            objectDict = dictOfObj[key]
            objectDict[listOfArg[2]] = str(listOfArg[3])
            storage.save()

    def do_count(self, arg):
        """ retrieves the number of instances of a class """
        if HBNBCommand.check_arg_if_passed(arg) == 0:
            return
        if arg not in HBNBCommand.dictOfClasses.keys():
            print("** class doesn't exist **")
            return
        my_dict = HBNBCommand.get_obj_of_a_class(storage.all(), arg)
        print(len(my_dict))

    @classmethod
    def precmd(cls, line):
        """ happens before command is executed """
        if "." in line:
            listOfArgs = line.split(".")
            if listOfArgs[0] in HBNBCommand.dictOfClasses.keys():
                obj = HBNBCommand()
                methods = []
                for el in dir(obj):
                    if callable(getattr(obj, el)) and not el.startswith("__"):
                        methods.append(el)

                # used in adding a space before method to allow spliting
                i = 0
                for char in listOfArgs[1]:
                    if char == "(":
                        string = listOfArgs[1]
                        listOfArgs[1] = string[:i] + " " + string[i:]
                        break
                    i += 1

                otherArg = (listOfArgs[1]).split(" ")
                userMethod = "do_" + otherArg[0]
                userMethod = HBNBCommand().strip_char(userMethod, ["(", ")"])
                for method in methods:
                    if userMethod == (f"{method}"):
                        cmd = HBNBCommand.strip_char(otherArg[0], ["(", ")"])
                        if (len(otherArg) > 1):
                            arg = ' '.join(otherArg[1:])
                            arg = HBNBCommand.strip_char(arg, ["(", ")", '"', ",", "'"])
                            return f"{cmd} {listOfArgs[0]} {arg}"
                        else:
                            return f"{cmd} {listOfArgs[0]}"
                return line
            else:
                return line
        else:
            return line

    def postloop(self):
        """Called after the command loop exits."""
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
