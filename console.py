#!/usr/bin/python3
"""x"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """x"""
    prompt = "(hbnb) "

    def do_help(self, arg):
        """x"""
        if arg == "":
            print("\nDocumented commands (type help <topic>):")
            print("========================================")
            print("EOF  help  quit\n")
        elif arg == "EOF":
            print("\nSome help text regarding EOF\n")
        elif arg == "help":
            print("\nSome help text regarding help\n")
        elif arg == "quit":
            print("\nQuit command to exit the program\n")
        else:
            print("\n" + arg + " does not exist\n")

    def do_EOF(self, arg):
        """x"""
        return True

    def do_quit(self, arg):
        """x"""
        return True

    def emptyline(self):
        """x"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
