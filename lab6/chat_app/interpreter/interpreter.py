class Interpreter:
    def __init__(self, expression):
        self.expression = expression

    def interpret(self, message):
        return self.expression.interpret(message)
