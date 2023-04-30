from src import Editor, CopyCommand, PasteCommand, DeleteCommand, UndoCommand


if __name__ == "__main__":
    editor = Editor('Hello, world!')
    editor.select_text(2, 7)  # Select "llo, "
    copy_command = CopyCommand(editor)
    editor.execute_command(copy_command)

    editor.move_cursor(9)  # Move cursor after "d"
    paste_command = PasteCommand(editor)
    editor.execute_command(paste_command)

    editor.select_text(0, 5)  # Select "Hello"
    delete_command = DeleteCommand(editor)
    editor.execute_command(delete_command)

    undo_command = UndoCommand(editor)
    editor.execute_command(undo_command)  # Undo delete
