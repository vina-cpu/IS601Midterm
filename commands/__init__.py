import os
import logging
from dotenv import load_dotenv
from datetime import datetime
from commands.command import CommandHandler
from history import History

class Interface:
    def __init__(self):
        self.configure_logging()
        load_dotenv()
        History.read_csv_loc = self.loadEnv() # saving my environment variable to where to read csvs for this 
        self.commandHandler = CommandHandler()
    
    @staticmethod
    def newInterface():
        return Interface()
    
    def configure_logging(self):
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok = True)
        log_file = os.path.join(log_dir, datetime.now().strftime("%m.%d.%H.%M.log"))
        logging.basicConfig(
            level=logging.INFO, 
            format='%(asctime)s %(levelname)s %(message)s',
            datefmt="%m-%d-%Y %H:%M:%S",
            filename=log_file
        )
        logging.info("Logging configured")
    
    def load_env(self):
        logging.info("Environment variable loaded")
        key: str = os.getenv("MYKEY")
        return key
    
    def get_env(self):
        return self.myEnvironment

    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, type 'menu' for a full list of commands, or type 'exit' to exit!")
        self.commandHandler.load_commands()
        while True:
            self.commandHandler.execute_command(input(">>> ").strip())     
