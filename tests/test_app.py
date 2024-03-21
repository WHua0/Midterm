# pylint: disable = unused-import
# pylint: disable = unused-argument

'''Test App'''
import unittest
from unittest import TestCase, mock
from unittest.mock import patch
from io import StringIO
import sys
import logging
import os
import shutil
from app import App

class TestApp(unittest.TestCase):
    '''Tests App'''

    def setUp(self):
        self.app_instance = App()
        self.temp_dir = "test_logs"

    def tearDown(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_configure_logging_with_logging_conf(self):
        '''Tests configure_logging'''
        with patch("os.path.exists", return_value = True), \
            patch("logging.config.fileConfig") as mock_file_config:
            self.app_instance.configure_logging()
            mock_file_config.assert_called_once_with("logging.conf", disable_existing_loggers = False)

    @mock.patch.dict("os.environ", {})
    @mock.patch.object(App, "load_environment_variables", return_value = {"LOG_DIRECTORY": "test_logs", "LOG_LEVEL": "WARNING"})
    def test_configure_logging_without_logging_conf_and_with_dotenv(self, mock_load_env):
        '''Tests configure_logging without logging.conf and with dotenv configuration'''
        app_instance = App()
        test_log_filepath = os.path.abspath(os.path.join("test_logs", "app.log"))
        with mock.patch("os.path.exists", return_value = False), \
            mock.patch("logging.basicConfig") as mock_basic_config:
            app_instance.configure_logging()
            mock_basic_config.assert_called_once_with(filename = test_log_filepath, level = logging.WARNING, format = "%(asctime)s - %(levelname)s - %(message)s", disable_existing_loggers = False)

    @mock.patch.dict("os.environ", {})
    @mock.patch.object(App, "load_environment_variables", return_value = {})
    def test_configure_logging_without_logging_conf_and_without_dotenv(self, mock_load_env):
        '''Tests configure_logging without logging.conf and without dotenv configuration'''
        app_instance = App()
        test_log_filepath = os.path.abspath(os.path.join("logs", "app.log"))
        with mock.patch("os.path.exists", return_value = False), \
            mock.patch("logging.basicConfig") as mock_basic_config:
            app_instance.configure_logging()
            mock_basic_config.assert_called_once_with(filename = test_log_filepath, level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s", disable_existing_loggers = False)

    @patch("app.load_dotenv")
    def test_get_data_directory(self, mock_load_dotenv):
        '''Tests get_data_directory'''
        os.environ["DATA_DIRECTORY"] = "test_data"
        expected_data_directory = os.path.abspath("test_data")
        actual_data_directory = App.get_data_directory()
        self.assertEqual(actual_data_directory, expected_data_directory)

    def test_load_environment_variables(self):
        '''Tests load_environment_variables'''
        with patch("os.environ.items", return_value = {"ENV_VAR1": "value1", "ENV_VAR2": "value2"}):
            settings = self.app_instance.load_environment_variables()
            self.assertEqual(settings, {"ENV_VAR1": "value1", "ENV_VAR2": "value2"})

    def test_load_plugins(self):
        '''Tests load_plugins'''
        app = App()
        app.load_plugins()
        self.assertTrue(len(app.command_handler.commands) > 0)

    def test_load_plugins_importerror(self):
        '''Tests load_plugins importerror'''
        with patch("app.importlib.import_module") as mock_import_module:
            mock_import_module.side_effect = ImportError("Mock ImportError")
            self.app_instance.load_plugins()
            mock_import_module.assert_called()

    @patch("sys.stdout", new_callable=StringIO)
    def test_start(self, mock_stdout):
        '''Tests start'''
        app = App()
        with patch("builtins.input", side_effect=["fake_command", "exit"]):
            try:
                app.start()
            except SystemExit as e:
                self.assertEqual(e.code, "Exiting Calculator App ...")
            else:
                self.fail("Expected SystemExit but it did not occur.")  # pragma: no cover
        self.assertIn("Calculator App Initiated ...\nPlease type a command.\nInvalid Command: fake_command\nType 'menu' for list of commands.\nType 'exit' to exit.\n", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
