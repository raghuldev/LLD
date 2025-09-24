from ILogger import ILogger
class ErrorLogger(ILogger):
    def log(self, msg):
        print(f"ERROR: {msg}")