# pylint: disable = unused-argument

'''Test CSV File Checker'''
import unittest
import os
from unittest.mock import patch
from app.historyhandler.csvfilechecker import CSVFileChecker

class TestCSVFileChecker(unittest.TestCase):
    '''Tests CSV File Checker'''

    @patch("os.path.exists", return_value = False)
    @patch("os.makedirs")
    @patch("logging.info")
    def test_check_data_directory_if_directory_not_exists(self, mock_logging_info, mock_makedirs, mock_exists):
        '''Tests CSVFileChecker.check_data_directory if data directory does not exist'''
        CSVFileChecker.data_directory = "./data"
        CSVFileChecker.check_data_directory()
        mock_logging_info.assert_called_once_with(f"Created '{CSVFileChecker.data_directory}' directory.")

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = False)
    @patch("sys.stdout", autospec = True)
    @patch("logging.error", autospec = True)
    def test_check_data_directory_if_directory_not_writable(self, mock_logging_error, mock_stdout, mock_access, mock_exists):
        '''Tests CSVFileChecker.check_data_directory when directory is not writable'''
        CSVFileChecker.data_directory = "./data"
        CSVFileChecker.check_data_directory()
        mock_logging_error.assert_called_once_with(f"Directory '{CSVFileChecker.data_directory}' is not writable.")

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = False)
    @patch("sys.stdout", autospec = True)
    @patch("logging.error", autospec = True)
    def test_check_file_writable_if_not_writable(self, mock_logging_error, mock_stdout, mock_access, mock_exists):
        '''Tests CSVFileChecker.check_file_writable when file is not writable'''
        directory = "data"
        filename = "test_file.csv"
        expected_filepath = os.path.join(directory, filename)
        CSVFileChecker.check_file_writable(expected_filepath)
        mock_logging_error.assert_called_once_with(f"File '{expected_filepath}' is not writable.")

    def test_validate_valid_filename(self):
        '''Tests Valid File Name'''
        valid_filename = "valid_file.csv"
        self.assertTrue(CSVFileChecker.validate_filename(valid_filename))

    def test_validate_invalid_filename(self):
        '''Tests Invalid File Name'''
        invalid_filename = "invalid/file.csv"
        self.assertFalse(CSVFileChecker.validate_filename(invalid_filename))

    def test_get_filepath(self):
        '''Tests Get File Path'''
        directory = "data"
        filename = "test_file"
        expected_filepath = os.path.join(directory, filename + ".csv")
        self.assertEqual(CSVFileChecker.get_filepath(directory, filename), expected_filepath)

    def test_get_filepath_if_file_has_csv_extension(self):
        '''Tests Get File Path if File already has .csv'''
        directory = "data"
        filename = "test_file.csv"
        expected_filepath = os.path.join(directory, filename)
        self.assertEqual(CSVFileChecker.get_filepath(directory, filename), expected_filepath)

    @patch("os.path.exists", return_value = True)
    @patch("os.access", return_value = False)
    @patch("sys.stdout", autospec = True)
    @patch("logging.error", autospec = True)
    def test_get_filepath_if_file_not_writable(self, mock_logging_error, mock_stdout, mock_access, mock_exists):
        '''Tests CSVFileChecker.get_filepath when file is not writable'''
        directory = "data"
        filename = "test_file.csv"
        expected_filepath = os.path.join(directory, filename)
        CSVFileChecker.get_filepath(directory, filename)
        mock_logging_error.assert_called_once_with(f"File '{expected_filepath}' is not writable.")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
