from calculator.commands.command import Command

class MenuCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self, *args):
        print("Available commands:")
        for command_name in self.commands:
            print(f"- {command_name}")
        return None