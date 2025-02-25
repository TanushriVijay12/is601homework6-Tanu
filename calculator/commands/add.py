from decimal import Decimal
from calculator.commands.command import Command

class AddCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        return a + b
