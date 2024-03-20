# Python Calculator

## Setup Instructions

1. $ git clone <repository_url>
2. $ cd <directory_location>
3. $ python deactivate
4. $ pip install virtualenv
5. $ virtualenv venv
6. $ virtualenv -p /usr/bin/python3 venv
7. $ source ./venv/bin/activate
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
    +exit

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
     + Staticmethods add, sutract, multiply and divide provide an interface to execute for specific operations
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
   + Plugins
     + https://github.com/WHua0/Midterm/tree/master/app/plugins
     + Command Design Pattern for plugin classes that are subclasses (concrete command classes) of the abstract base class Command from CommandHandler, and serve as standalone objects with information to execute a specific action
   + CommandHandler
     + https://github.com/WHua0/Midterm/blob/master/app/commandhandler/__init__.py
     + Command Design Pattern for abstract base class Command, and class CommandHandler as an invoker that registers and executes commands with KeyError exception handling
   + App
     + https://github.com/WHua0/Midterm/blob/master/app/__init__.py
     + While not following any particular design patterns, class App serves as the entry point for starting the application
     + Class App configures logging and loads environment variables
     + Class App dynamically loads, registers, and executes plugin commands using the CommandHandler
     + Class App implements a Read-Eval-Print Loop (REPL) to allow continous interaction with the command-line interface until the session is terminated

## Environment Variables

1. $ touch .env
2. $ vi .env
3. add:
   + ENVIRONMENT = <name_of_environment> ; default is TESTING
   + DATABASE_USERNAME = <name_of_database_username> ; default is root
   + DATA_DIRECTORY = <name_of_data_directory> ; default is data

https://github.com/WHua0/Midterm/blob/master/app/__init__.py

class App

1. def __init__(self) ; self.settings = self.load_environment_variables()
   + Loads .env into App settings
2. def __init__(self) ; self.settings.setdefault("ENVIRONMENT", "TESTING")
   + Sets value of ENVIRONMENT as TESTING if none
3. def __init__(self) ; self.settings.setdefault("DATABASE_USERNAME", "root")
   + Sets value of DATABASE_USERNAME as root if none
4. def __init__(self) ; self.data_directory = self.settings.get("DATA_DIRECTORY", "data")
   + Sets self.data_directory as value of DATA_DIRECTORY or data if none 
5. def get_data_directory(cls)
   + Returns absolute path of self.data_directory 

https://github.com/WHua0/Midterm/blob/master/app/filehandler/csvfilechecker.py
https://github.com/WHua0/Midterm/blob/master/app/filehandler/__init__.py

6. data_directory = App.get_data_directory()

### Summary for .env DATA_DIRECTORY:

1. .env provides the name of the data_directory
2. App loads the name of data_directory from .env
3. App converts name of data_directory into an absolute path
4. Other files retrieve the data_directory's absolute path from App 

## Logging

## LBYL & EAFP
