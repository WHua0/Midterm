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
        logging.info("Registered Command: '%s'.", command_name)

    def execute_command(self, command_name: str):
        '''Executes the Command'''
        try:
            logging.info("Attempted Command: '%s'.", command_name)
            self.commands[command_name].execute()
            logging.info("Executed Command: '%s'.", command_name)

        except KeyError:
            logging.warning("Invalid Command: '%s'.", command_name)
            print(f"Invalid Command: {command_name}")
            print("Type 'menu' for list of commands.")
            print("Type 'exit' to exit.")
