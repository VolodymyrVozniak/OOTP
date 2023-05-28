from typing import List
from .command import Command, MacroCommand
from .text_selection import TextSelection


class Editor:
    def __init__(self, text: str = ''):
        self.text = text
        self.cursor_pos = 0
        self.commands_history: List[Command] = []
    
    def execute_command(self, command: Command):
        command.execute()

    def select_text(self, start: int, end: int):
        self.selection = TextSelection(start, end)
        return self.text[self.selection.start: self.selection.end]

    def move_cursor(self, pos: int):
        self.cursor_pos = pos
