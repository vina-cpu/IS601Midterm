import logging
from decimal import Decimal, InvalidOperation
from history import History
from commands.command import Command

class DeleteCommand(Command):
    description = "Type 'delete' to be asked for an index in the history to delete"
    
    def execute(self):
        print("What index would you like to delete:")
        index: str = input(">>> ").strip()
        print(f"Deleting index {index} now ... ")
        try:
            num = map(int, index)
            History.delete_index(num)
            print(f"Index {index} deleted!")
            logging.info(f"Index {index} in history deleted deleted!")
        except Exception as e:
            print(f"An error occured: {e}")
            logging.error(f"While attempting to delete an index, an error occured: {e}")

command = DeleteCommand()
