'''App'''
import os
import pkgutil
import importlib
import sys
import logging
import logging.config
from app.introduction import introduction
from app.commandhandler import Command, CommandHandler
from app.plugins.menu import MenuCommand

class App:
    '''Class App'''

    def __init__(self):
        '''Constructor'''
        os.makedirs("logs", exist_ok = True)
        self.configure_logging()
        self.command_handler = CommandHandler()
        self.command_handler.register_command("menu", MenuCommand(self.command_handler))

    def configure_logging(self):
        '''Configures logging settings'''

        logging_conf_path = "logging.conf"
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers = False)
        else:
            logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Configured logging.")

    def load_plugins(self):
        ''' Dynamically loads plugins from the plugins directory'''

        plugins_package = "app.plugins"

        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):

            if is_pkg:

                try:
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugins(plugin_name, plugin_module)
                    logging.info("Imported Command '%s' from Plugin '%s'.", plugin_name, plugins_package)

                except ImportError as e:
                    logging.error("Failed to import Command '%s' from Plugin '%s': '%s'.", plugin_name, plugins_package, str(e))

    def register_plugins(self, plugin_name, plugin_module):
        '''Imports and registers commands from plugins.'''

        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)

            try:
                if issubclass(item, Command):
                    command_instance = item()
                    self.command_handler.register_command(plugin_name, command_instance)

            except TypeError:
                continue

    def start(self):
        '''Starts the App'''
        logging.info("Initiated App.")

        introduction()
        self.load_plugins()

        while True:
            self.command_handler.execute_command(input(">>> ").strip())
