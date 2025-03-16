from history import History
from commands.command import Command

class LookCommand(Command):
    def execute(self):
        print("Fetching history ... ")
        try:
            print(History.get_history())
        except Exception as e:
            print(f"An error occured: {e}")

command = LookCommand()