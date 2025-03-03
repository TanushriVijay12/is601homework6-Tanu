from decimal import Decimal
from calculator.commands.command import Command

class PowerCommand(Command):
    def execute(self, a: Decimal, b: Decimal) -> Decimal:
        """Calculate a raised to the power of b."""
        return a ** b