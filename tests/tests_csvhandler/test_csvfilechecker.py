'''Test CSV File Checker'''
import unittest
import os
from app.csvhandler.csvfilechecker import CSVFileChecker

class TestCSVFileChecker(unittest.TestCase):
    '''Tests CSV File Checker'''

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

if __name__ == '__main__':
    unittest.main() # pragma: no cover
