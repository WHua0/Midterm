'''Exit'''
import sys
import logging
from app.commandhandler import Command

class ExitCommand(Command):
    '''Exit Command'''

    def execute(self):
        logging.info("Exited App.")
        raise sys.exit("Exiting Calculator App ...")
