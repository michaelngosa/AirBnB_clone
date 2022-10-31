#!/usr/bin/python3
"""
the entry point of the command interpreter
"""
import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
