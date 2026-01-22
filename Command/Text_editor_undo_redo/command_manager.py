from commands import Command, InsertCommand, DeleteCommand
from typing import List

class CommandManager:
    def __init__(self):
        self.history: List[Command] = []
        self.redo_stack: List[Command] = []
    
    def execute_command(self, command: Command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()
    
    def undo(self):
        command = self.history.pop()
        command.undo()
        self.redo_stack.append(command)
        print('Undo Successfull')
    
    def redo(self):
        command = self.redo_stack.pop()
        command.execute()
        self.history.append(command)
        print("Redo Successfull")