#!/usr/bin/env python3
"""console acting console"""

import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    prompt = "(hbnb) "
    dictt = {"BaseModel": BaseModel}

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
            for inst in insts:
                if inst.startswith(arg + '.'):
                    results.append(str(insts[inst]))
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
                    setattr(instance, args[2], args[3].strip('"'))
                    instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
