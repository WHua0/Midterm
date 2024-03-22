'''Command Handler'''
import logging
from abc import ABC, abstractmethod

class Command(ABC):
    '''Class Command'''

    @abstractmethod
    def execute(self):
        '''Any subclass of Command must implement its own execute method'''

class CommandHandler:
    '''Class CommandHandler'''

    def __init__(self):
        '''Constructor for a Commands Dictionary'''
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        '''Registers the Plugin Command'''
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        '''Executes the Command'''
        try:
            logging.info(f"Initiated command {command_name}.")
            self.commands[command_name].execute()
            logging.info(f"Completed command {command_name}.")

        except KeyError as e:
            print(f"Invalid Command: {command_name}")
            logging.warning(f"KeyError, Invalid command {command_name}.")
            print("Type 'menu' for list of commands.")
            print("Type 'exit' to exit.")

