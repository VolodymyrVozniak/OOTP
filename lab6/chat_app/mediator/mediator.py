from ..models.message import Message
from ..models.chatroom import ChatRoom


class Mediator:
    def __init__(self):
        self.users = []
        self.chat_rooms = {}

    def add_user(self, user):
        self.users.append(user)

    def create_chat_room(self, name):
        chat_room = ChatRoom(name)
        self.chat_rooms[name] = chat_room
        return chat_room

    def invite_user_to_chat_room(self, user, chat_room_name):
        chat_room = self.chat_rooms.get(chat_room_name)
        if chat_room:
            chat_room.add_user(user)
        else:
            print(f"Chat room {chat_room_name} not found.")

    def send_message(self, message, sender):
        if isinstance(message, Message):
            for user in self.users:
                if user != sender:
                    user.receive_message(message)
        elif isinstance(message, tuple):
            chat_room_name, message_content = message
            chat_room = self.chat_rooms.get(chat_room_name)
            if chat_room:
                chat_room.send_message(Message(message_content), sender)
            else:
                print(f"Chat room {chat_room_name} not found.")
