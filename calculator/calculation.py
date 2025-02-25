from decimal import Decimal
from calculator.commands.command import Command

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Command):
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Command):
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        return self.operation.execute(self.a, self.b)

    def __repr__(self):
        return f"Calculation({self.a}, {self.b}, {self.operation.__class__.__name__})"
