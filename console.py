#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity

Class_Dict = {"BaseModel": BaseModel,
              "User": User,
              "City": City,
              "Place": Place,
              "Review": Review,
              "State": State,
              "Amenity": Amenity
              }


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """

    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "Amenity": Amenity,
               "Review": Review,
               "City": City}

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

    def do_destroy(self, args):
        """
        delete an instance base on class name and id
        """
        new_args = ""
        class_name = ""
        class_id = ""
        try:
            new_args = args.split(" ")
            class_name = new_args[0]
            class_id = new_args[1]
            class_id = class_id.strip('\"')
        except BaseException:
            pass
        if not class_name:
            print('** class name missing **')
        elif class_name not in Class_Dict:
            print("** class doesn't exist **")
        elif not class_id:
            print('** instance id missing **')
        else:
            new_key = class_name + '.' + class_id
            try:
                del storage._FileStorage__objects[new_key]
                storage.save()
            except KeyError:
                print('** no instance found **')

    def help_destroy(self):
        '''
        Help for destroy
        '''
        print('Destroy command to show delete an instance based\
        on class name and id\n')

    def do_all(self, args):
        """
        print all instances based on class
        """
        new_list = []
        if args:
            if args not in Class_Dict:
                print("** class doesn't exist **")
                return
            for key, value in storage._FileStorage__objects.items():
                if key.split(".")[0] == args:
                    new_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                new_list.append(str(value))
        print(new_list)

    def help_all(self):
        """
        display all instances [based on class if chosen]
        """
        print("displays all instances [based on the class if choosen]")
        print("all [class]")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by
        adding or updating attribute (save the change into the JSON file)
        """
        class_name = ""
        class_id = ""
        new_object = ""
        attr_name = ""
        attr_val = ""
        objects = ""
        try:
            new_object = args.split(" ")
            class_name = new_object[0]
            class_id = new_object[1]
            attr_name = new_object[2]
            attr_val = new_object[3]
            objects = storage.FileStorage__objects.items()
        except (IndexError, NameError):
            pass
        if not class_name:
            print("** class name missing **")
            return
        if class_name not in Class_Dict:
            print("** class doesn't exist **")
            return
        if not id:
            print("** instance id missing **")
            return
        if not attr_name:
            print("** attribute name missing **")
            return
        if not attr_val:
            print("** value missing **")
            return

        new_key = class_name + "." + class_id
        no_touchy = ["id", "created_at", "updated_at"]
        for key, value in storage._FileStorage__objects.items():
            if new_key not in no_touchy:
                if new_key == key:
                    setattr(value, attr_name, attr_val)
                    new = value
                    new.save()
        print("** no instance found **")
        if new_key not in storage._FileStorage__objects.keys():
            print("** no instance found **")

    def help_update(self):
        """
        help for update
        """
        print("updates and objects with new information")
        print('update <class name> <id> <attribute name> "<attribute value>"')

    def do_count(self, args):
        """
        count number of instances by class
        """
        counter = 0

        new_arg = args.split(" ")
        if new_arg[0] not in Class_Dict:
            print("** class doesn't exist **")
            return
        new_list = storage._FileStorage__objects.items()
        for key, value in new_list:
            temp_key = str(key)
            new_key = temp_key.split(".")
            if new_key[0] == new_arg[0]:
                counter = (counter + 1)
        print(counter)

    def help_count(self):
        """
        counts the number of instances of a class
        """
        print("count <class>")

    def default(self, line):
        '''
        Advanced
        '''
        _cmd = storage.all()
        if '.' in line:
            cmd_parse = line.split('.')
            class_name = cmd_parse[0]
            method_name = cmd_parse[1]
            if class_name in Class_Dict:
                if method_name[0:5] == 'all()':
                    self.do_all(class_name)
                if method_name[0:7] == 'count()':
                    self.do_count(class_name)
                if method_name[0:5] == 'show(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    arg = class_name + ' ' + show_id
                    print(arg)
                    self.do_show(arg)
                if method_name[0:8] == 'destroy(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    arg = class_name + ' ' + show_id
                    self.do_destroy(arg)
                if method_name[0:7] == 'update(':
                    method_name2 = method_name.split('"')
                    show_id = method_name2[1]
                    show_att_name = method_name2[3]
                    show_att_val = method_name2[5]
                    arg = class_name + ' ' + show_id +\
                        ' ' + show_att_name + ' ' + show_att_val
                    print(arg)
                    self.do_update(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
