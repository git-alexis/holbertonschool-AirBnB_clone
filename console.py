#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    """
    This class represents the command-line interface for the AirBnB clone.
    It provides various commands to interact with the application.
    """

    prompt = "(hbnb) "
    __class = ["BaseModel", "User", "State", "City", "Amenity", "Place",
               "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel

        Args:
            arg (str): The name of the class to create an instance of.

        Returns:
        None
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.__class:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id

        Args:
            arg (str): The argument passed to the command. Should be in the
            format <class name> <instance id>.

        Returns:
            None
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.__class:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                from models import storage
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id

        Args:
            arg (str): The argument containing the class name and instance id.

        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.__class:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                from models import storage
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name.

        Args:
            arg (str): The class name. If provided, only instances of the
                specified class will be printed.

        Returns:
            None
        """
        from models import storage
        if not arg:
            instance_list = []
            for value in storage.all().values():
                instance_list.append(str(value))
            print(instance_list)
        elif arg not in self.__class:
            print("** class doesn't exist **")
        else:
            instance_list = []
            for key, value in storage.all().items():
                if key.split(".")[0] == arg:
                    instance_list.append(str(value))
            print(instance_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute

        Args:
            arg (str): The arguments passed to the command.

        Returns:
        None
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] not in self.__class:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                from models import storage
                if key in storage.all():
                    setattr(storage.all()[key], args[2], args[3])
                    storage.save()
                else:
                    print("** no instance found **")


if __name__ == "__main__":

    HBNBCommand().cmdloop()
