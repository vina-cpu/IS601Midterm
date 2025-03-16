import logging
from decimal import Decimal, InvalidOperation
from history import History
from commands.command import Command

class SaveCommand(Command):
    description = "Type 'save' to save the current history into a new file in the 'saves' folder; if the 'saves' folder does not exist, this will also create the 'saves' folder"
    def execute(self):
        print(f"Saving a new file of the current history to 'saves' now ... ")
        try:
            History.save_history()
            logging.info("New history saved to file, see 'saves' folder")
        except Exception as e:
            print(f"An error occured: {e}")
            logging.error(f"While attempting to save, an error occured: {e}")

command = SaveCommand()