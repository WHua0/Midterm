# pylint: disable = unused-import

'''Test App'''
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import logging
from app import App

class TestApp(unittest.TestCase):
    '''Tests App'''

    def setUp(self):
        self.app_instance = App()

    def test_configure_logging_with_logging_conf(self):
        '''Tests configure_logging'''
        with patch("os.path.exists", return_value = True), \
            patch("logging.config.fileConfig") as mock_file_config:
            self.app_instance.configure_logging()
            mock_file_config.assert_called_once_with("logging.conf", disable_existing_loggers = False)

    def test_configure_logging_without_logging_conf(self):
        '''Tests configure_logging without logging.conf'''
        with patch("os.path.exists", return_value = False), \
            patch("logging.basicConfig") as mock_basic_config:
            self.app_instance.configure_logging()
            mock_basic_config.assert_called_once_with(level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")

    def test_load_environment_variables(self):
        '''Tests load_environment_variables'''
        with patch("os.environ.items", return_value={"ENV_VAR1": "value1", "ENV_VAR2": "value2"}):
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
