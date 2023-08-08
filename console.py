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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
