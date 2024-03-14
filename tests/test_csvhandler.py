# pylint: disable = unused-argument

'''Test CSVHandler'''
import unittest
import os
from unittest.mock import patch
from app.csvhandler import CSVHandler, CSVFactory

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

    @patch("os.path.exists", return_value = False)
    @patch("os.makedirs")
    @patch("logging.info")
    def test_check_data_directory_if_directory_not_exists(self, mock_logging_info, mock_makedirs, mock_exists):
        '''Tests CSVHandler.check_data_directory if data directory does not exist'''
        csv_handler = CSVHandler()
        csv_handler.data_directory = "./data"
        csv_handler.check_data_directory()
        mock_logging_info.assert_called_once_with(f"Created '{csv_handler.data_directory}' directory.")

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = False)
    @patch("sys.stdout", autospec = True)
    @patch("logging.error", autospec = True)
    def test_check_data_directory_if_directory_not_writable(self, mock_logging_error, mock_stdout, mock_access, mock_exists):
        '''Tests CSVHandler.check_data_directory when directory is not writable'''
        csv_handler = CSVHandler()
        csv_handler.data_directory = "./data"
        csv_handler.check_data_directory()
        mock_logging_error.assert_called_once_with(f"Directory '{csv_handler.data_directory}' is not writable.")

    def test_create_csv_file(self):
        '''Tests CSVHandler.create_csv_file'''
        CSVHandler.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.create_csv_file(filename)
        self.assertTrue(os.path.exists(filepath))

    @patch("logging.warning")
    def test_create_csv_file_if_file_already_exists(self, mock_logging_warning):
        '''Tests CSVHandler.create_csv_file if file already exists'''
        CSVHandler.data_directory = self.testdir
        filename = "test.csv"
        CSVHandler.create_csv_file(filename)
        CSVHandler.create_csv_file(filename)
        mock_logging_warning.assert_called_once_with(f"File '{filename}' already exists.")

    def test_delete_csv_file(self):
        '''Tests CSVHandler.delete_csv_file'''
        CSVHandler.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.create_csv_file(filename)
        CSVHandler.delete_csv_file(filename)
        self.assertFalse(os.path.exists(filepath))

    @patch("logging.warning")
    def test_delete_csv_file_if_file_not_exists(self, mock_logging_warning):
        '''Tests CSVHandler.delete_csv_file if file does not exist'''
        CSVHandler.data_directory = self.testdir
        filename = "nofiletest.csv"
        CSVHandler.delete_csv_file(filename)
        mock_logging_warning.assert_called_once_with(f"File '{filename}' does not exist.")

    def test_csvfactory_create(self):
        '''Tests CSV Factory create CSV File'''
        CSVHandler.data_directory = self.testdir
        filename = "test"
        filepath = os.path.join(self.testdir, "test.csv")
        CSVFactory("create", filename)
        self.assertTrue(os.path.exists(filepath))

    def test_csvfactory_delete(self):
        '''Tests CSV Factory delete CSV File'''
        CSVHandler.data_directory = self.testdir
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
