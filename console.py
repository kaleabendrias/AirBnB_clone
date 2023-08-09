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
    prompt = "(hbnb)"
    dictOfClasses = {"BaseModel":BaseModel(), "User":User(),\
            "Place":Place(), "State":State(), "City":City(),\
            "Amenity":Amenity(), "Review":Review()}

    def do_exit(self, arg):
        """Exits the cmd interpreter """
        return True

    def do_EOF(self, arg):
        """ Exits the command interpreter """
        return True

    def emptyline(self):
        """ do nothing when an emptyline is entered """
        pass

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
            dictionaryOfAllObjects = storage.all()
            key = f"{listOfArg[0]}.{listOfArg[1]}"
            if key not in dictionaryOfAllObjects.keys():
                print("** no instance found **")
                return
            print(f"{dictionaryOfAllObjects[key]}")

    def do_destroy(self, arg):
        """ deletes the existence of an instance """
        if HBNBCommand.check_arg_if_passed(arg) == 0:
            return
        # arg must be broken since the cmd module does not multiple arg
        listOfArg = arg.split()
        if HBNBCommand.check_multiple_arg_passed(listOfArg) == 1:
            storage.reload()
            dictionaryOfAllObjects = storage.all()
            key = f"{listOfArg[0]}.{listOfArg[1]}"
            if key not in dictionaryOfAllObjects.keys():
                print("** no instance found **")
                return
            del dictionaryOfAllObjects[key]
            storage.save()

    def do_all(self, arg):
        """ prints all objects in the json file """
        if not arg:
            pass
        elif arg in HBNBCommand.dictOfClasses.keys():
            pass
        else:
            print("** class doesn't exist **")
            return
        storage.reload()
        dictionaryOfAllObjects = storage.all()
        print(dictionaryOfAllObjects)

    def do_update(self, arg):
        """ updates an instance based on class name and id """
        #TODO don't forget the problem with double quotation when you have quotation in argument     
        if HBNBCommand.check_arg_if_passed(arg) == 0:
            return
        # arg must be broken since the cmd module does not multiple arg
        listOfArg = arg.split()
        if HBNBCommand.check_multiple_arg_passed(listOfArg) == 1:
            storage.reload()
            dictionaryOfAllObjects = storage.all()
            key = f"{listOfArg[0]}.{listOfArg[1]}"
            if key not in dictionaryOfAllObjects.keys():
                print("** no instance found **")
                return
            if len(listOfArg) == 2:
                print("** attribute name missing **")
                return
            if len(listOfArg) == 3:
                print("** value missing **")
                return
            objectDict = dictionaryOfAllObjects[key]
            objectDict[listOfArg[2]] = str(listOfArg[3])
            storage.save()

    @classmethod
    def get_objects_for_specific_class(cls, dictionaryOfAllObjects, specifiedClass):
        """ gets all objects for a specific class """
        objectsDictionary = {}
        for key in dictionaryOfAllObjects.keys():
            if dictionaryOfAllObjects[key]["__class__"] == specifiedClass:
                objectsDictionary[key] = dictionaryOfAllObjects[key]
        return (objectsDictionary)

    @classmethod
    def strip_characters(cls,input_string, characters_to_remove):
        """
        removes certain characters and returns back the string
        """
        return ''.join(char for char in input_string if char not in characters_to_remove)


    @classmethod
    def precmd(cls, line):
        """ happens before command is executed """
        if "." in line:
            listOfArgs = line.split(".")
            if listOfArgs[0] in HBNBCommand.dictOfClasses.keys():
                obj = HBNBCommand()
                methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
                otherArgs = (listOfArgs[1]).split(" ")
                userMethod = "do_" + otherArgs[0]
                userMethod = HBNBCommand().strip_characters(userMethod, ["(", ")"])
                for method in methods:
                    if userMethod == (f"{method}"):
                        methodCall = HBNBCommand.strip_characters(otherArgs[0], ["(", ")"])
                        if (len(otherArgs) > 1):
                            otherPart = ' '.join(otherArgs[1:])
                            print(otherPart)
                            return f"{methodCall} {otherPart}"
                        else:
                            print(otherArgs)
                            return f"{methodCall} {listOfArgs[0]}"
                print(listOfArgs)
                print(methods)
                return line
            else:
                return line
        else:
            return line



if __name__ == "__main__":
    HBNBCommand().cmdloop()
