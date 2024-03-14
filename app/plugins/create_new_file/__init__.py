'''Create_New_File'''
import logging
from app.commandhandler import Command
from app.csvhandler import CSVHandler, CSV_Factory

class CreateCSVFileCommand(Command):
    '''Create CSV File Command'''

    def execute(self):
        CSVHandler.check_data_directory()

        filename = input("Please provide a file name: ")
        CSV_Factory("create", filename)
