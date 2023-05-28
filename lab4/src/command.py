from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, editor):
        self.editor = editor
    
    def execute(self):
        self.do_execute()
    
    @abstractmethod
    def do_execute(self):
        pass


class MacroCommand(Command):
    def __init__(self, editor):
        super().__init__(editor)
        self.commands = []
    
    def add_command(self, command: Command):
        self.commands.append(command)
    
    def do_execute(self):
        for command in self.commands:
            command.execute()


class CopyCommand(Command):
    def do_execute(self):
        if self.editor.selection:
            self.editor.clipboard = self.editor.text[self.editor.selection.start:self.editor.selection.end]
    

class PasteCommand(Command):
    def do_execute(self):
        if self.editor.clipboard:
            self.editor.text = self.editor.text[:self.editor.cursor_pos] + self.editor.clipboard + self.editor.text[self.editor.cursor_pos:]
            self.editor.cursor_pos += len(self.editor.clipboard)


class DeleteCommand(Command):
    def do_execute(self):
        if self.editor.selection:
            start, end = self.editor.selection.start, self.editor.selection.end
        else:
            start, end = self.editor.cursor_pos - 1, self.editor.cursor_pos
        self.editor.text = self.editor.text[:start] + self.editor.text[end:]
        self.editor.cursor_pos = start
