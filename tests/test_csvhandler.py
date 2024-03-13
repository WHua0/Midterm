'''Test CSVHandler'''

import unittest
import os
from app.csvhandler import CSVHandler

class TestCSVHandler(unittest.TestCase):
    '''Tests CSVHandler'''

    def setUp(self):
        '''Creates temporary test_data directory before each test case'''
        self.test_dir = "./test_data"
        os.makedirs(self.test_dir, exist_ok = True)

    def tearDown(self):
        '''Deletes temporary test_data directory after each test case'''
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_check_data_directory_if_directory_does_not_exist(self):
        '''Tests CSVHandler.check_data_directory if data directory does not exist'''
        csv_handler = CSVHandler()
        csv_handler.data_directory = self.test_dir
        csv_handler.check_data_directory()
        self.assertTrue(os.path.exists(self.test_dir))

    def test_create_csv_file(self):
        '''Tests CSVHandler.create_csv_file'''
        CSVHandler.data_directory = self.test_dir
        filename = "test.csv"
        CSVHandler.create_csv_file(filename)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, filename)))

    def test_delete_csv_file(self):
        '''Tests CSVHanlder.delete_csv_file'''
        CSVHandler.data_directory = self.test_dir
        filename = "test.csv"
        file_path = os.path.join(self.test_dir, filename)
        CSVHandler.create_csv_file(filename)
        CSVHandler.delete_csv_file(filename)
        self.assertFalse(os.path.exists(file_path))

if __name__ == '__main__':
    unittest.main() # pragma: no cover
