import sys
from commands.command import Command

class ExitCommand(Command):
    description = "Type 'exit' to exit the program"
    
    def execute(self):
        print("Goodbye!")
        
        sys.exit(1)

command = ExitCommand()