class User:
    def __init__(self, username):
        self.username = username

    def send_message(self, message, mediator):
        mediator.send_message(message, self)

    def receive_message(self, message):
        print(f"{self.username} received message: {message.content}")
