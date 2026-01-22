from text_editor import TextEditor
from command_manager import CommandManager
from commands import InsertCommand, DeleteCommand


editor = TextEditor()

manger = CommandManager()

manger.execute_command(InsertCommand(editor=editor, text="HI RAGHUL", position=0))
editor.showText()
manger.execute_command(DeleteCommand(editor=editor, position=0, length=3))
editor.showText()
manger.undo()
editor.showText()