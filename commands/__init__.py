import os
import logging
from dotenv import load_dotenv
from datetime import datetime
from commands.command import CommandHandler

class Interface:
    def __init__(self):
        load_dotenv()
        self.logging_level = self.load_env("LOG_LEVEL") # saving my environment variable to where to save log files
        self.logging_destination = self.load_env("LOG_DESTINATION")
        self.configure_logging(self.logging_level, self.logging_destination)
        self.commandHandler = CommandHandler()
    
    @staticmethod
    def newInterface():
        return Interface()
    
    def configure_logging(self, logging_level, logging_destination):
        log_dir = logging_destination
        os.makedirs(log_dir, exist_ok = True)
        log_file = os.path.join(log_dir, datetime.now().strftime("%m.%d.%H.%M.log"))
        log_level = getattr(logging, logging_level.upper()) # maps the logging_level to right logging, also makes sure it's upppercase
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt="%m-%d-%Y %H:%M:%S",
            filename=log_file
        )
        logging.info("Logging configured, environment variables loaded!")
    
    def load_env(self, reference_key):
        key: str = os.getenv(reference_key)
        return key
    
    def get_env(self, reference_key) -> str:
        if reference_key == "LOG_LEVEL":
            return self.logging_level
        elif reference_key == "LOG_DESTINATION":
            return self.logging_destination
        else:
            return None

    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, type 'menu' for a full list of commands including saving and loading, or type 'exit' to exit!")
        self.commandHandler.load_commands()
        while True:
            self.commandHandler.execute_command(input(">>> ").strip())     
