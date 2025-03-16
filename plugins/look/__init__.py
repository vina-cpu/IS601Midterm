import logging
from history import History
from commands.command import Command

class LookCommand(Command):
    description = "Type 'look' to look at the current history without saving it"
    
    def execute(self):
        print("Fetching history ... ")
        try:
            print(History.get_history())
            logging.info("History fetched")
        except Exception as e:
            print(f"An error occured: {e}")
            logging.error(f"While attempting to look at history, an error occured: {e}")

command = LookCommand()