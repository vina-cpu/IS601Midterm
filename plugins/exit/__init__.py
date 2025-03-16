import sys
from commands.command import Command

class ExitCommand(Command):
    def execute(self):
        print("Goodbye!")
        
        sys.exit(1)

command = ExitCommand()