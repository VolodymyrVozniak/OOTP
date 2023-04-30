from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def interpret(self, message):
        pass


class EnglishExpression(Expression):
    def interpret(self, message):
        return f"{message.content} (translated to English)"


class SpanishExpression(Expression):
    def interpret(self, message):
        return f"{message.content} (translated to Spanish)"
