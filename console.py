#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User

Class_Dict = {"BaseModel": BaseModel,
              "User": User}


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """

    prompt = '(hbnb)'

    def do_quit(self, command):
        """
        to exit the program
        """
        exit()

    def help_quit(self):
        """
        help for quit command
        """
        print('Quit command to exit the program\n')

    def do_EOF(self, command):
        """
        EOF method
        """
        print()
        exit()

    def help_EOF(self):
        """
        help for EOF
        """
        print('EOF command to exit the program\n')

    def emptyline(self):
        """
        an empty line + ENTER shouldn’t execute anything
        """
        pass
    
    def do_create(self, args):
        """
        create new intance of BaseModel
        """
        if not args:
            print('** class name missing **')
            return
        elif args in Class_Dict:
            for key, value in Class_Dict.items():
                if key == args:
                    new_instance = Class_Dict[key]()
                storage.save()
                print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        '''
        Help for create
        '''
        print('Create command to create new instance\n')
    
    def do_show(self, args):
        """
        Print str repr of an instance
        bases on class name and id
        """
        new_instance = args.partition(' ')
        class_name = new_instance[0]
        class_id = new_instance[2]
        
        if not args:
            print('** class name missing **')
            return
        if class_name not in Class_Dict:
            print("** class doesn't exist **")
            return
        if not class_id:
            print('** instance id missing **')
            return
        new_key = class_name + "." + class_id
        try:
            print(storage._FileStorage__objects[new_key])
        except BaseException:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
