class Command:
    def execute(self, *args):
        raise NotImplementedError("Subclasses must implement the execute method.")