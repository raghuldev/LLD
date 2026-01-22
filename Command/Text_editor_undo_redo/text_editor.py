class TextEditor:
    def __init__(self):
        self.content = ""
    
    def insertText(self, text, position):
        self.content = self.content[:position] + text + self.content[position:]
        print(f"Inserted {text} at postion {position}")
    
    def deleteText(self, position, length):
        deleted = self.content[position: position+length]
        self.content = self.content[:position] + self.content[position + length:]
        print(f"Deleted {deleted} from postion {position}")
        return deleted
    
    def showText(self):
        print(f"{self.content}")