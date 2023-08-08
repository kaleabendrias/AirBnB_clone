#!/usr/bin/env python3
"""console acting console"""

import cmd
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
