from decimal import Decimal
from calculator.commands.command import Command

class SquareRootCommand(Command):
    def execute(self, a: Decimal, *args) -> Decimal:
        """Calculate the square root of a."""
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return a.sqrt()