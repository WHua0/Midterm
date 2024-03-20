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
2. $ menu
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
3. $ exit

<Video_Demonstration_Link_to_be_Added>

## Design Patterns

## Environment Variables

1. $ touch .env
2. $ vi .env
3. add:
   + ENVIRONMENT = <name_of_environment> ; default is TESTING
   + DATABASE_USERNAME = <name_of_database_username>
   + DATA_DIRECTORY = <name_of_data_directory> ; default is data

## Logging

## LBYL & EAFP
