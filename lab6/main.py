from chat_app.interpreter import Interpreter, SpanishExpression, EnglishExpression
from chat_app.mediator import Mediator
from chat_app.models import User, Message
from chat_app.utils import Logger


if __name__ == '__main__':
    mediator = Mediator()

    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    mediator.add_user(alice)
    mediator.add_user(bob)
    mediator.add_user(charlie)

    chat_room = mediator.create_chat_room("General")
    chat_room.add_user(alice)
    chat_room.add_user(bob)

    Logger.log("Sending message to all users...")
    message = Message("Hello, everyone!")
    mediator.send_message(message, alice)

    Logger.log("Sending message to chat room...")
    message = ("General", "How's it going?")
    mediator.send_message(message, bob)

    Logger.log("Translating message to Spanish...")
    message = Message("Good morning!")
    expression = SpanishExpression()
    interpreter = Interpreter(expression)
    translated_message = interpreter.interpret(message)
    Logger.log(translated_message)

    Logger.log("Translating message to English...")
    expression = EnglishExpression()
    interpreter = Interpreter(expression)
    translated_message = interpreter.interpret(message)
    Logger.log(translated_message)

    chat_room2 = mediator.create_chat_room("Python")
    chat_room2.add_user(charlie)
    mediator.invite_user_to_chat_room(alice, "Python")
    mediator.invite_user_to_chat_room(bob, "Python")
    mediator.send_message(Message(translated_message), charlie)
