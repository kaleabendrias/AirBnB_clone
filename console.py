#!/usr/bin/env python3
"""console acting console"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = "(hbnb) "
    dictt = {"BaseModel": BaseModel, "User": User, "Place": Place,
             "State": State, "City": City, "Amenity": Amenity,
             "Review": Review}

    @classmethod
    def strip_characters(cls, input_string, characters_to_remove):
        """removes certain characters and returns back the string"""
        filtered_string = ""
        for char in input_string:
            if char not in characters_to_remove:
                filtered_string += char
        return filtered_string

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using Ctrl+D (EOF)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel"""
        args = arg.split()
        if not len(args):
            print("** class name missing **")
            return
        if args[0] in self.dictt.keys():
            new_inst = self.dictt[args[0]]()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on th"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in self.dictt:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                inst = models.storage.all()
                inst_key = class_name + '.' + args[1]
                if inst_key in inst:
                    print(inst[inst_key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.dictt:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            instance_key = args[0] + '.' + args[1]
            if instance_key in instances:
                del instances[instance_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        insts = models.storage.all()
        if not arg:
            print([str(insts[inst]) for inst in insts])
        elif arg not in self.dictt:
            print("** class doesn't exist **")
        else:
            results = []
            class_name = arg
            for inst in insts.values():
                if isinstance(inst, self.dictt[class_name]):
                    results.append(str(inst))
            print(results)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.dictt:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            instance_key = args[0] + '.' + args[1]
            if instance_key in instances:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    instance = instances[instance_key]
                    setattr(instance, args[2], args[3].strip("'\""))
                    instance.save()
            else:
                print("** no instance found **")

    @classmethod
    def precmd(cls, line):
        """ happens before command is executed """
        if "." in line:
            listOfArgs = line.split(".")
            if listOfArgs[0] in HBNBCommand.dictt.keys():
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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
