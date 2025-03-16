import sys
import logging
from commands.command import Command

class ExitCommand(Command):
    description = "Type 'exit' to exit the program"
    
    def execute(self):
        logging.info("Program exited successfully!")
        print("Goodbye!")
        
        sys.exit(1)

command = ExitCommand()