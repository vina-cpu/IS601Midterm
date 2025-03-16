from commands.command import CommandHandler

class Interface:
    def __init__(self):
        self.commandHandler = CommandHandler()
    
    @staticmethod
    def newInterface():
        return Interface()

    def start(self):
        print("Hello! Type calculator commands to utilize the calculator, type 'menu' for a full list of commands, or type 'exit' to exit!")
        self.commandHandler.load_commands()
        while True:
            self.commandHandler.execute_command(input(">>> ").strip())     
