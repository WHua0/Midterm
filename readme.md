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
3. App converts name_of_data_directory into an absolute path
4. Other files may retrieve the data_directory's absolute path from App 

## Logging

## LBYL & EAFP
