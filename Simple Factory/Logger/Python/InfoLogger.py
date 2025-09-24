from ILogger import ILogger
class InfoLogger(ILogger):
    def log(self, msg):
        print(f"INFO: {msg}")