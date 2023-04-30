from typing import List
from .command import Command, MacroCommand, UndoCommand, RedoCommand
from .text_selection import TextSelection


class Editor:
    def __init__(self, text: str = ''):
        self.text = text
        self.cursor_pos = 0
        self.commands_history: List[Command] = []
    
    def execute_command(self, command: Command):
        command.execute()
        if isinstance(command, MacroCommand):
            self.commands_history.extend(command.commands)
        else:
            self.commands_history.append(command)
    
    def execute_macro(self, macro: MacroCommand):
        macro.execute()

    def select_text(self, start: int, end: int):
        selection = TextSelection(start, end)
        return self.text[selection.start: selection.end]

    def move_cursor(self, pos: int):
        self.cursor_pos = pos
