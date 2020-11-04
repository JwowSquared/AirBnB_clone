#!/usr/bin/python3
"""This module handles reading input and the implemented console commands"""
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """class implementation of cmd"""
    prompt = "(hbnb) "
    __classLib = {
        "BaseModel": BaseModel
        "User": User
        "State": State
        "City": City
        "Amenity": Amenity
        "Place": Place
        "Review": Review
    }

    def do_help(self, arg):
        """displays the help command"""
        helpLib = {
            "EOF": "\nEOF HELP\n",
            "help": "\nHELP HELP\n",
            "quit": "\nQuit command to exit the program\n",
            "create": "\nCREATE HELP\n",
            "show": "\nSHOW HELP\n",
            "destroy": "\nDESTROY HELP\n",
            "all": "\nALL HELP\n",
            "update": "\nUPDATE HELP\n"
        }
        if arg in helpLib.keys():
            print(helpLib[arg])
        else:
            print("\nDocumented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit\n")

    def do_update(self, arg):
        """updates a key in an instance"""
        if arg == "":
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in HBNBCommand.__classLib.keys():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        obj = storage.all()[key]
        if len(args) < 3:
            print("** attribute name missing **")
            return

        vargs = arg.split("\"")
        if len(vargs) < 3:
            print("** value missing **")
            return

        setattr(obj, args[2], vargs[1])
        storage.save()

    def do_all(self, arg):
        """displays all instances of a class"""
        if arg == "":
            print([str(x) for x in storage.all().values()])
        else:
            lib = HBNBCommand.__classLib
            if arg in lib.keys():
                print([str(x) for x in storage.all().values() if type(x) is lib[arg]])
            else:
                print("** class doesn't exist **")

    def do_create(self, arg):
        """creates a new instance of a class"""
        if arg in HBNBCommand.__classLib.keys():
            x = HBNBCommand.__classLib[arg]()
            storage.save()
            print(x.id)
        elif arg == "":
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """removes an instance of a class"""
        if arg == "":
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in HBNBCommand.__classLib.keys():
            print ("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        objs = storage.all()
        if key not in objs.keys():
            print("** no instance found **")
            return

        objs.pop(key)
        storage.save()

    def do_show(self, arg):
        """shows all objects"""
        if arg == "":
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in HBNBCommand.__classLib.keys():
            print ("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + "." + args[1]
        objs = storage.all()
        if key not in objs.keys():
            print("** no instance found **")
            return

        print(objs[key])


    def do_EOF(self, arg):
        """Shows end of file"""
        return True

    def do_quit(self, arg):
        """quits the console"""
        return True

    def emptyline(self):
        """returns an empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
