'''Exit Command'''
import sys
import logging
from app.commandhandler import Command

class ExitCommand(Command):
    '''Exits python interpreter and terminates program'''
    def execute(self):
        logging.info("Executed Command: Exit.")
        raise sys.exit("Exiting Calculator App ...")
