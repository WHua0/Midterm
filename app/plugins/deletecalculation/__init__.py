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
            logging.info("Input: '%s'.", value)
            index = int(value)

            if 0 <= index < len(df):
                deleted_data = df.iloc[index]
                history_handler.delete_calculation(history_instance, index)
                print("Calculation Deleted:")
                print(deleted_data.to_frame().T)
                logging.info("Deleted Calculation:\n%s.", deleted_data.to_frame().T)

            else:
                print("Index out of range.")
                logging.info("Index out of range.")

        except ValueError:
            print("Invalid input.")
            logging.warning("Invalid input.")
