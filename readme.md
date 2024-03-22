# Python Calculator

## Setup Instructions

1. $ git clone <repository_url>
2. $ cd <directory_location>
3. $ deactivate
4. $ pip install virtualenv
5. $ virtualenv venv
6. $ virtualenv -p /usr/bin/python3 venv
7. $ source venv/bin/activate
8. $ pip3 install -r requirements.txt

## Testing Instructions
1. $ pytest --num_records = <#> ; default is 5
2. $ pytest --pylint --cov 

## Usage & Video Demostration
1. $ python main.py
   + menu
   + add / subtract / multiply / divide
     + <Operand_A> <Operand_B>
   + showhistory / clearhistory
   + deletecalculation
     + <index_number_of_the_calculation>
   + showfiles
   + filemanager
     + save <file_name>
     + delete <file_name>
     + load <file_name>
    + exit

<Video_Demonstration_Link_to_be_Added>

## Design Patterns

### Calculator
   + operations.py 
     + https://github.com/WHua0/Midterm/blob/master/app/calculator/operations.py
     + Factory Method Design Pattern for class Operations with staticmethods add, subtract, multiply and divide that each return a result as a decimal value or ZeroDivisionError
   + calculation.py
     + https://github.com/WHua0/Midterm/blob/master/app/calculator/calculation.py
     + Strategy Design Pattern for class Calculation that encapsulates operandA, operandB and Operation into a calculation, and computes operandA and operandB according to the Operation
   + history.py 
     + https://github.com/WHua0/Midterm/blob/master/app/calculator/history.py
     + Singleton Design Pattern for class History that insures that only one instance of History is created and accessed at any given point in the program, and provides methods to manipulate the instance
   + calculator
     + https://github.com/WHua0/Midterm/blob/master/app/calculator/__init__.py
     + Facade Design Pattern for class Calculator with staticmethods that serve as interfaces to calculator functionality
     + Staticmethod execute acts as a facade for performing calculations
     + Staticmethods add, subtract, multiply and divide provide an interface to execute for specific operations
     + Staticmethod calculate_and_print provides a centralized way to perform calculations and handle exceptions

### HistoryHandler
   + historyhandler
     + https://github.com/WHua0/Midterm/blob/master/app/historyhandler/__init__.py
     + Mostly a Facade Design Pattern for class HistoryHandler with staticmethods that serve as an interface for history.py to manipulate an instance of history
     + Staticmethod create_history follows a Factory Method Design Pattern to create an instance of history
     + Staticmethod import_history follows an Adapter Design Pattern that allows for the intergration of external dataframes to class History

### FileHandler
   + csvfilechecker.py
     + https://github.com/WHua0/Midterm/blob/master/app/filehandler/csvfilechecker.py
     + While not following any particular design patterns, class CSVFileChecker utilizes staticmethods to adhere to the Single Responsiblity Principle (SRP) of checking and validating directories and files
   + csvfactory.py
     + https://github.com/WHua0/Midterm/blob/master/app/filehandler/csvfactory.py
     + Factory Method Design Pattern for class CSVHandler with staticmethods that manipulate CSV files and an instance of history with exception handling.
   + filehandler
     + https://github.com/WHua0/Midterm/blob/master/app/filehandler/__init__.py
     + Facade Design Pattern for class FileHandler with a staticmethod that acts as an interface for csvfactory.py

### App
   + plugins
     + https://github.com/WHua0/Midterm/tree/master/app/plugins
     + Command Design Pattern for plugin classes that are subclasses (concrete command classes) of the abstract base class Command from CommandHandler, and serve as standalone objects with information to execute a specific action
   + commandhandler
     + https://github.com/WHua0/Midterm/blob/master/app/commandhandler/__init__.py
     + Command Design Pattern for abstract base class Command, and class CommandHandler as an invoker that registers and executes commands with KeyError exception handling
   + app
     + https://github.com/WHua0/Midterm/blob/master/app/__init__.py
     + While not following any particular design patterns, class App serves as the entry point for starting the application
     + Class App loads environment variables and configures logging
     + Class App dynamically loads, and registers and and executes plugin commands using the CommandHandler
     + Class App implements a Read-Eval-Print Loop (REPL) to allow continous interaction with the command-line interface until the session is terminated

## Environment Variables

1. $ touch .env
2. $ vi .env
3. add:
   + ENVIRONMENT = <name_of_environment> ; default is TESTING
   + DATABASE_USERNAME = <name_of_database_username> ; default is root
   + DATA_DIRECTORY = <name_of_data_directory> ; default is data
   + LOG_DIRECTORY = <name_of_log_directory> ; default is logs
   + LOG_LEVEL = <INFO/WARNING/ERROR> ; default is INFO

https://github.com/WHua0/Midterm/blob/master/app/__init__.py

class App

1. def __init__(self) ; self.settings = self.load_environment_variables()
    + Loads .env into App settings
2. def __init__(self) ; self.settings.setdefault("ENVIRONMENT", "TESTING")
    + Sets value of ENVIRONMENT as TESTING if none
3. def __init__(self) ; self.settings.setdefault("DATABASE_USERNAME", "root")
    + Sets value of DATABASE_USERNAME as root if none
4. def __init__(self) ; self.log_directory = self.settings.get ("LOG_DIRECTORY", "logs")
    + Gets value of LOG_DIRECTORY or logs if none
5. def __init__(self) ; self.log_level = self.settings.get("LOG_LEVEL", "INFO")
    + Gets value of LOG_LEVEL or INFO if none
6. def __init__(self) ; self.data_directory = self.settings.get("DATA_DIRECTORY", "data")
    + Gets value of DATA_DIRECTORY or data if none 
7. def get_data_directory(cls)
    + Returns absolute path of self.data_directory 

https://github.com/WHua0/Midterm/blob/master/app/filehandler/csvfilechecker.py

https://github.com/WHua0/Midterm/blob/master/app/filehandler/__init__.py

8. data_directory = App.get_data_directory()

### Summary for .env LOG_DIRECTORY and LOG_INFO:

1. .env provides the values of LOG_DIRECTORY and LOG_INFO
2. App loads the values from .env
3. If logging.conf exists, App wil create a "logs" directory if it does not exist, and configure logging according to logging.conf
4. Or else, App will use the values of LOG_DIRECTORY and LOG_INFO to create a logs directory if it does not exist, and configure basic logging.

### Summary for .env DATA_DIRECTORY:

1. .env provides the name of the data_directory
2. App loads the name of data_directory from .env
3. App converts name of data_directory into an absolute path
4. Other files retrieve the data_directory's absolute path from App 

## Logging

### INFO
  + Used to monitor normal executions of code.
### WARNING
  + Used to monitor expected exceptions that do not affect program functionality.
### ERROR
  + Used to monitor exceptions that may affect program functionality.
### Examples
  + calculator: Calculation.calculate_and_print(a, b, operation_name)
    + https://github.com/WHua0/Midterm/blob/master/app/calculator/__init__.py
    + Info - successful calculate and print with log of the parameters
    + Error - unknown operation
    + Warning - invalid Operand a or Operand b
    + Warning - ZeroDivisionError
  + csvfilechecker.py
    + https://github.com/WHua0/Midterm/blob/master/app/filehandler/csvfilechecker.py
    + Info - successful creation of a data directory
    + Error - data directory is not writable
    + Error - file is not writable
    + Warning - file was not found
    + Warning - file already exists
    + Warning - invalid filename
  + csvfactory
    + https://github.com/WHua0/Midterm/blob/master/app/filehandler/csvfactory.py
    + Info - saved history to file
    + Info - deleted file
    + Info - loaded history from file
    + Error - failed to load history from file
  + filehandler
    + https://github.com/WHua0/Midterm/blob/master/app/filehandler/__init__.py
    + Warning - invalid file operation
  + plugins
    + https://github.com/WHua0/Midterm/tree/master/app/plugins
    + add, subtract, multiply, and divide
      + Info - user inputs two values with log of the inputs: Operand a and Operand B
      + Warning - user inputs incorrect number of values
    + filemanager
      + Info - user inputs two values with log of the inputs: csvcommand and filename in data directory
      + Warning - user inputs incorrect number of values
    + deletecalculation
      + Info - sucessful execution with log of the calculation deleted: dataframe
      + Warning - index is out range with log of the input
      + Warning - invalid inputs with log of the inputs
    + showhistory, clearhistory, menu, and exit
      + Info - successful execution
    + showfiles
      + Error - failed to execute
      + Info - successful execution
  + commandhandler
    + https://github.com/WHua0/Midterm/blob/master/app/commandhandler/__init__.py
    + Info - initiated command
    + Info - completed command
    + Warning - invalid command
  + app
    + https://github.com/WHua0/Midterm/blob/master/app/__init__.py
    + Info - configured logging from logging.conf
    + Info - configured basic logging configuration
    + Info - loaded command
    + Info - registered loaded command
    + Error - failed to load command

## Look Before You Leap (LBYL) & Easier To Ask For Forgiveness than Permission (EAFP)

1. operation.py
    + https://github.com/WHua0/Midterm/blob/master/app/calculator/operations.py
    + LYBL in method divide(a, b) for ZeroDivisionError
      +  Assuming that the parameters provided are always decimals, if b == 0, raise ZeroDivisionError, or else a / b.
2. calculator
    + https://github.com/WHua0/Midterm/blob/master/app/calculator/__init__.py
    + EAFP in calculate_and_print(a, b, operation_name) for InvalidOperation and Exception
      + The method tries to convert parameters a and b into decimals, and handles the InvalidOperation and any other Exceptions if it cannot.
    + LBYL in calculate_and_print(a, b, operation_name) for "unknown operation"
      + If parameter operation_name is not found in operation_mapping, the method prints "unknown operation". 
3. csvfilechecker.py
    + https://github.com/WHua0/Midterm/blob/master/app/filehandler/csvfilechecker.py
    + LBYL in all methods
      + Except for method get_filepath, all other methods will return True or False depending if the condition is or is not met.
      + Method get_filepath will add .csv if not in the filename, return False if the filepath is not writable, or else return the filepath.
4. csvfactory.py
    + https://github.com/WHua0/Midterm/blob/master/app/filehandler/csvfactory.py
    + LBYL in all methods
      + All Methods return if the file does not pass the csvfilechecker method, or else will run through its code.
    + EAFP load_csv_file_to_history for Exception
      + Method tries to read a csv file and return it as a dataframe, but returns None if there is an Exception. 
5. filehandler
    + https://github.com/WHua0/Midterm/blob/master/app/filehandler/__init__.py
    + LBYL in CSVCommands(operation, filename)
      + Method returns if the file does not pass the csvfilechecker methods. Then, method runs though the if-elif conditions for a matching operation, or else method prints "invalid file operation".
6. plugin: add, subtract, multiply, divide
    + https://github.com/WHua0/Midterm/blob/master/app/plugins/divide/__init__.py
    + LBYL in execute
      + If total number of parameters provided == 2, calculator.calculate_and_print(a, b, operation_name) will run, or else the method prints "incorrect number of inputs". 
7. plugin: showfiles
    + https://github.com/WHua0/Midterm/blob/master/app/plugins/showfiles/__init__.py
    + LBYL in execute
      + Method will return if the file does not pass the csvfilechecker method, or else will run through its code.
    + EAFP in execute for Exception
      + Method tries to the obtain a list of filenames from a directory, but handles Exception and returns if cannot. Otherwise, method continues to run through its code. 
8. plugin: deletecalculation
    + https://github.com/WHua0/Midterm/blob/master/app/plugins/deletecalculation/__init__.py
    + EAFP in execute for ValueError
      + Method tries to convert input into an integer, but handles ValueError if it cannot.
    + LBYL in execute
      + If the try passes, method checks if the input is a valid index number in the dataframe, or else method method prints "index out of range".
9. plugin: filemanager
    + https://github.com/WHua0/Midterm/blob/master/app/plugins/filemanager/__init__.py
    + LBYL in execute
      +  If total number of parameters provided == 2, filemanager.CSVCommands(csvcommand, filename) will run, or else the method prints "incorrect number of inputs".
10.  commandhandler
      + https://github.com/WHua0/Midterm/blob/master/app/commandhandler/__init__.py
      + EAFP in CommandHandler.excute_command(self, command_name) for KeyError
        + Method tries to execute command_name, and handles KeyError if command_name does not exist.
11. app
    + https://github.com/WHua0/Midterm/blob/master/app/__init__.py
    + LPYL in configure_logging
      + If logging.conf exists, method configures logging settings, or else method configures basic logging settings.
    + LPYL in load_plugins
      + Method checks if module is a package. If yes, method tries the below, or else passes.
    + EAFP in load_plugins for ImportError
      + Method tries to import the package, and handles ImportError if it cannot.
    + EAFP in register_plugins for TypeError
      + Method tries the below, and handles TypeError if it cannot.
    + LPYL in register_plugins
      + If current item is a subclass of Command, method tries commandhandler.register(plugin_name, plugin_module).