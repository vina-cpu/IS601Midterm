import logging
from decimal import Decimal, InvalidOperation
from history import History
from commands.command import Command

class SaveCommand(Command):
    def execute(self):
        print(f"Saving a new file of the current history to 'saves' now ... ")
        try:
            History.save_history()
        except Exception as e:
            print(f"An error occured: {e}")

command = SaveCommand()