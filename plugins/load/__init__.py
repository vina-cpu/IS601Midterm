import logging
from decimal import Decimal, InvalidOperation
from history import History
from commands.command import Command

class LoadCommand(Command):
    description = "Type 'load' to load a history located in a .csv file: be sure to know where your file is!"
    def execute(self):
        print("What is your file:")
        new_file: str = input(">>> ").strip()
        print(f"Locating file now ... ")
        try:
            History.load_history(new_file)
            print(f"File {new_file} loaded!")
        except Exception as e:
            print(f"An error occured: {e}")

command = LoadCommand()