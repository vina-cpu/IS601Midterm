import logging
from history import History
from commands.command import Command

class ClearCommand(Command):
    def execute(self):
        print("Clearing history now ... ")
        try:
            History.clear_history()
            print("History cleared!")
        except Exception as e:
            print(f"An error occured: {e}")

command = ClearCommand()