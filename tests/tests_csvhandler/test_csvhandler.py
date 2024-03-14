# pylint: disable = unused-argument

'''Test CSVHandler'''
import unittest
import os
from unittest.mock import patch
from app.csvhandler import CSVHandler, CSVFactory
from app.csvhandler.csvfilechecker import CSVFileChecker

class TestCSVHandler(unittest.TestCase):
    '''Tests CSVHandler'''

    def setUp(self):
        '''Creates temporary test_data directory before each test case'''
        self.testdir = "./test_data"
        os.makedirs(self.testdir, exist_ok = True)

    def tearDown(self):
        '''Deletes temporary test_data directory after each test case'''
        for filename in os.listdir(self.testdir):
            filepath = os.path.join(self.testdir, filename)
            if os.path.isfile(filepath):
                os.remove(filepath)
        os.rmdir(self.testdir)

    def test_create_csv_file(self):
        '''Tests CSVHandler.create_csv_file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.create_csv_file(filename)
        self.assertTrue(os.path.exists(filepath))

    @patch("logging.warning")
    def test_create_csv_file_if_file_already_exists(self, mock_logging_warning):
        '''Tests CSVHandler.create_csv_file if file already exists'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        CSVHandler.create_csv_file(filename)
        CSVHandler.create_csv_file(filename)
        mock_logging_warning.assert_called_once_with(f"File '{filename}' already exists.")

    def test_delete_csv_file(self):
        '''Tests CSVHandler.delete_csv_file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.create_csv_file(filename)
        CSVHandler.delete_csv_file(filename)
        self.assertFalse(os.path.exists(filepath))

    @patch("logging.warning")
    def test_delete_csv_file_if_file_not_exists(self, mock_logging_warning):
        '''Tests CSVHandler.delete_csv_file if file does not exist'''
        CSVFileChecker.data_directory = self.testdir
        filename = "nofiletest.csv"
        CSVHandler.delete_csv_file(filename)
        mock_logging_warning.assert_called_once_with(f"File '{filename}' does not exist.")

    def test_csvfactory_create(self):
        '''Tests CSV Factory create CSV File'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test"
        filepath = os.path.join(self.testdir, "test.csv")
        CSVFactory("create", filename)
        self.assertTrue(os.path.exists(filepath))

    @patch("logging.warning")
    def test_csvfactory_if_file_name_is_invalid(self, mock_logging_warning):
        '''Tests CSV Factory if file name in invalid'''
        CSVFileChecker.data_directory = self.testdir
        filename = "$test.csv"
        CSVFactory("create", filename)
        mock_logging_warning.assert_called_once_with(f"Invalid File Name: {filename}.")

    def test_csvfactory_delete(self):
        '''Tests CSV Factory delete CSV File'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test"
        filepath = os.path.join(self.testdir, "test.csv")
        CSVFactory("create", filename)
        CSVFactory("delete", filename)
        self.assertFalse(os.path.exists(filepath))


    def test_csvfactory_invalid_operation(self):
        '''Tests CSV Factory invalid operation'''
        operation = "invalid_operation"
        filename = "test"
        self.assertIsNone(CSVFactory(operation, filename))

if __name__ == '__main__':
    unittest.main() # pragma: no cover
