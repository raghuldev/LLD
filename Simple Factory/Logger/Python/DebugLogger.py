from ILogger import ILogger
class DebugLogger(ILogger):
    def log(self, msg):
        print(f"DEBUG: {msg}")