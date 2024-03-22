'''App'''
import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from dotenv import load_dotenv
from app.introduction import introduction
from app.commandhandler import Command, CommandHandler
from app.plugins.menu import MenuCommand
from app.historyhandler import HistoryHandler

class App:
    '''Class App'''

    def __init__(self):
        '''Constructor'''
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault("ENVIRONMENT", "TESTING")
        self.settings.setdefault("DATABASE_USERNAME", "root")
        self.settings.setdefault("LOG_DIRECTORY", "logs")
        self.settings.setdefault("LOG_LEVEL", "INFO")
        self.settings.setdefault("DATA_DIRECTORY", "data")
        self.log_directory = self.settings.get("LOG_DIRECTORY")
        self.log_level = self.settings.get("LOG_LEVEL")
        self.data_directory = self.settings.get("DATA_DIRECTORY")
        self.configure_logging()
        self.command_handler = CommandHandler()
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))
        self.history = HistoryHandler.create_history()
        self.load_plugins()

    def configure_logging(self):
        '''Configures logging settings'''

        logging_conf_path = "logging.conf"
        if os.path.exists(logging_conf_path):
            os.makedirs("logs", exist_ok = True)
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers = False)
            logging.info("Configured logging from logging.conf.")
        else:
            log_directory = self.log_directory
            os.makedirs(log_directory, exist_ok = True)
            log_filepath = os.path.abspath(os.path.join(log_directory, "app.log"))
            log_level = getattr(logging, self.log_level.upper())
            logging.basicConfig(filename = log_filepath, level = log_level, format = "%(asctime)s - %(levelname)s - %(message)s")
            logging.info(f"Configured basic logging configuration: Directory {log_directory}, Level {self.log_level}.")

    @classmethod
    def get_data_directory(cls):
        '''Returns Data Directory in ENV'''
        return os.path.abspath(cls().data_directory)

    def load_environment_variables(self):
        '''Loads environment variables into settings dictionary'''
        settings = dict(os.environ.items())
        return settings

    def load_plugins(self):
        ''' Dynamically loads plugins from plugins directory'''

        plugins_package = "app.plugins"

        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):

            if is_pkg:

                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugins(plugin_name, plugin_module)
                    logging.info(f"Loaded command {plugin_name}.")

                except ImportError:
                    logging.error(f"ImportError, Failed to load command {plugin_name}.")

    def register_plugins(self, plugin_name, plugin_module):
        '''Imports and registers command from plugins'''

        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)

            try:
                if issubclass(item, Command):
                    command_instance = item()
                    self.command_handler.register_command(plugin_name, command_instance)
                    logging.info(f"Registered command {plugin_name}.")

            except TypeError:
                continue

    def start(self):
        '''Starts the App'''
        logging.info("Initiated App.")

        introduction()

        while True:
            self.command_handler.execute_command(input(">>> ").strip())
