import logging
from decimal import Decimal, InvalidOperation
from history import History
from commands.command import Command

class DeleteCommand(Command):
    def execute(self):
        print("What index would you like to delete:")
        index: str = input(">>> ").strip()
        print(f"Deleting index {index} now ... ")
        try:
            num = map(int, index)
            History.delete_index(num)
            print(f"Index {index} deleted!")
        except Exception as e:
            print(f"An error occured: {e}")

command = DeleteCommand()
