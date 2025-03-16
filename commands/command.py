import importlib
import pkgutil
import plugins
import logging

class Command:
    #@abstractmethod
    def execute(self):
        pass
    
class CommandHandler():
    def __init__(self):
        self.commands = {}
    
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
            logging.error(f"No such command: {command_name}")

    def load_commands(self):
        '''adds all of the plugins in plugins'''
        for _, name, _ in pkgutil.iter_modules(plugins.__path__):
            module = importlib.import_module(f"plugins.{name}.__init__")
            if hasattr(module, "command"):
                self.register_command(name, module.command)
                logging.info(f"{name} command loaded")
