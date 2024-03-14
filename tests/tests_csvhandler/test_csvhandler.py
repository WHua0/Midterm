# pylint: disable = unused-argument

'''Test CSVHandler'''
import unittest
import os
from unittest.mock import patch
from app.csvhandler import CSVHandler, CSVFactory
from app.historyhandler.csvfilechecker import CSVFileChecker

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
        CSVHandler.create_csv_file(filename, filepath)
        self.assertTrue(os.path.exists(filepath))

    @patch("logging.warning")
    def test_create_csv_file_if_file_already_exists(self, mock_logging_warning):
        '''Tests CSVHandler.create_csv_file if file already exists'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.create_csv_file(filename, filepath)
        CSVHandler.create_csv_file(filename, filepath)
        mock_logging_warning.assert_called_once_with(f"File '{filename}' already exists.")

    def test_delete_csv_file(self):
        '''Tests CSVHandler.delete_csv_file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.create_csv_file(filename, filepath)
        CSVHandler.delete_csv_file(filename, filepath)
        self.assertFalse(os.path.exists(filepath))

    @patch("logging.warning")
    def test_delete_csv_file_if_file_not_exists(self, mock_logging_warning):
        '''Tests CSVHandler.delete_csv_file if file does not exist'''
        CSVFileChecker.data_directory = self.testdir
        filename = "nofiletest.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.delete_csv_file(filename, filepath)
        mock_logging_warning.assert_called_once_with(f"File '{filename}' does not exist.")

    @patch("logging.info")
    def test_clear_csv_file(self,  mock_logging_info):
        '''Tests CSVHandler.clear_csv_file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.create_csv_file(filename, filepath)
        CSVHandler.clear_csv_file(filename, filepath)
        mock_logging_info.assert_any_call(f"Cleared File '{filename}'.")

    @patch("logging.warning")
    def test_clear_csv_file_if_file_not_exists(self, mock_logging_warning):
        '''Tests CSVHandler.clear_csv_file if file does not exist'''
        CSVFileChecker.data_directory = self.testdir
        filename = "nofiletest.csv"
        filepath = os.path.join(self.testdir, filename)
        CSVHandler.clear_csv_file(filename, filepath)
        mock_logging_warning.assert_called_once_with(f"File '{filename}' does not exist.")

    def test_csvfactory_create(self):
        '''Tests CSV Factory create CSV File'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test"
        filepath = os.path.join(self.testdir, "test.csv")
        CSVFactory("create", filename)
        self.assertTrue(os.path.exists(filepath))

    def test_csvfactory_delete(self):
        '''Tests CSV Factory delete CSV File'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test"
        filepath = os.path.join(self.testdir, "test.csv")
        CSVFactory("create", filename)
        CSVFactory("delete", filename)
        self.assertFalse(os.path.exists(filepath))

    @patch("logging.info")
    def test_csvfactory_clear(self,  mock_logging_info):
        '''Tests CSVHandler.clear_csv_file'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        CSVFactory("create", filename)
        CSVFactory("clear", filename)
        mock_logging_info.assert_any_call(f"Cleared File '{filename}'.")

    @patch("logging.warning")
    def test_csvfactory_if_file_name_is_invalid(self, mock_logging_warning):
        '''Tests CSV Factory if file name in invalid'''
        CSVFileChecker.data_directory = self.testdir
        filename = "$test.csv"
        CSVFactory("create", filename)
        mock_logging_warning.assert_called_once_with(f"Invalid File Name: {filename}.")

    def test_csvfactory_invalid_operation(self):
        '''Tests CSV Factory invalid operation'''
        operation = "invalid_operation"
        filename = "test"
        self.assertIsNone(CSVFactory(operation, filename))

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = False)
    @patch("sys.stdout", autospec = True)
    @patch("logging.error", autospec = True)
    def test_csvfactory_if_file_is_not_writable(self, mock_logging_error, mock_stdout, mock_access, mock_exists):
        '''Tests CSV Factory if file is not writable'''
        CSVFileChecker.data_directory = self.testdir
        filename = "test.csv"
        expected_filepath = os.path.join(self.testdir, filename)
        CSVFactory("create", filename)
        mock_logging_error.assert_any_call(f"File '{expected_filepath}' is not writable.")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
