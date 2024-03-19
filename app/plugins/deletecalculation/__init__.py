'''DeleteCalculation'''
import logging
import pandas as pd
from app.commandhandler import Command
from app.historyhandler import HistoryHandler

class DeleteCalculationCommand(Command):
    '''DeleteCalculation Command'''

    def execute(self):
        history_handler = HistoryHandler()
        history_instance = history_handler.create_history()
        history_data = history_handler.retrieve_history(history_instance)
        df = pd.DataFrame(history_data)

        try:
            value = (input("Please provide an index number: "))
            index = int(value)

            if 0 <= index < len(df):
                deleted_data = df.iloc[index]
                history_handler.delete_calculation(history_instance, index)
                print("Calculation Deleted:")
                print(deleted_data.to_frame().T)
                logging.info("Deleted Calculation:\n%s.", deleted_data.to_frame().T)

            else:
                print(f"Index out of range: '{value}'.")
                logging.info(f"Index out of range: '{value}'.")

        except ValueError:
            print(f"Invalid Input: '{value}'.")
            logging.warning(f"Invalid Input: '{value}'.")
