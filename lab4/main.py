from src import Editor, CopyCommand, PasteCommand, DeleteCommand, MacroCommand


if __name__ == "__main__":
    editor = Editor('Hello, world!')
    print(editor.text)

    editor.select_text(0, 5)  # Select "Hello"
    copy_command = CopyCommand(editor)
    editor.execute_command(copy_command)
    print(editor.text)

    editor.move_cursor(12)  # Move cursor after "d"
    paste_command = PasteCommand(editor)
    editor.execute_command(paste_command)
    print(editor.text)

    editor.select_text(12, 18)  # Select 2nd "Hello"
    delete_command = DeleteCommand(editor)
    editor.execute_command(delete_command)
    print(editor.text)

    editor.select_text(0, 12)
    editor.move_cursor(12)
    macro_command = MacroCommand(editor)
    macro_command.add_command(CopyCommand(editor))
    macro_command.add_command(PasteCommand(editor))
    editor.execute_command(macro_command)
    print(editor.text)
