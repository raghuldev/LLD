from abc import ABC, abstractmethod
from text_editor import TextEditor

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class InsertCommand(Command):
    def __init__(self, editor: TextEditor, text:str, position:int):
        self.editor = editor
        self.text = text
        self.position = position


    def execute(self):
        self.editor.insertText(text=self.text, position=self.position)
    
    def undo(self):
        self.editor.deleteText(position=self.position, length=len(self.text))


class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, position: int, length: int):
        self.editor = editor
        self.position = position
        self.length = length
        self.deleted_text = ""
    
    def execute(self):
        self.deleted_text = self.editor.deleteText(self.position, self.length)
    
    def undo(self):
        self.editor.insertText(text=self.deleted_text, position=self.position)