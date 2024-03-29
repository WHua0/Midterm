'''Menu'''
import logging
from app.commandhandler import Command

class MenuCommand(Command):
    '''Menu Command'''

    def __init__(self, command_handler):
        '''Constructor'''
        self.command_handler = command_handler

    def execute(self):
        '''Prints all plugin/command names'''
        print("List of Commands:")
        for plugin_name in self.command_handler.commands.keys():
            print(plugin_name)
        logging.info("Printed menu.")
