# pylint: disable = unused-argument

'''Test ShowFiles'''
import unittest
from unittest.mock import patch
from app.plugins.showfiles import ShowFilesCommand

class TestShowFilesCommand(unittest.TestCase):
    '''Tests ShowFilesCommand'''

    @patch("os.path.exists", return_value = True)
    @patch("os.makedirs")
    @patch("logging.info")
    def test_execute_with_valid_directory(self, mock_logging_info, mock_makedirs, mock_exist):
        '''Tests ShowFilesCommand if data directory exists'''
        show_files_command = ShowFilesCommand()
        show_files_command.execute()
        mock_logging_info.assert_called_once_with("Printed Data Directory.")

if __name__ == '__main__':
    unittest.main() # pragma: no cover
