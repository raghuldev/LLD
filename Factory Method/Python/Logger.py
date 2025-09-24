from abc import ABC, abstractmethod

# ILogger - Interface
class ILogger(ABC):
    @abstractmethod
    def log(self, msg) -> None:
        """Log the message"""
        pass

#  Logger implements-------------------------

class DebugLogger(ILogger):
    def log(self, msg):
        print(f"DEBUG: {msg}")

class ErrorLogger(ILogger):
    def log(self, msg):
        print(f"ERROR: {msg}")

class InfoLogger(ILogger):
    def log(self, msg):
        print(f"INFO: {msg}")
# -----------------------------------------------

# LoggerFactory Interface

class ILoggerFactory:
    @abstractmethod
    def createLogger(self):
        pass

# concrete factory loggers

class DebugFactory(ILoggerFactory):
    def createLogger(self):
        return DebugLogger()

class ErrorFactory(ILoggerFactory):
    def createLogger(self):
        return ErrorLogger()

class InfoFactory(ILoggerFactory):
    def createLogger(self):
        return InfoLogger()
 #----------------------------------------------

 #client

class Client():
    def getLogger(self):
        errorFactory = ErrorFactory()
        debugFactory = DebugFactory()
        infoFactory = InfoFactory()

        errorLogger = errorFactory.createLogger()
        debugLogger = debugFactory.createLogger()
        errorLogger.log("THIS IS ERROR log!!!")
        debugLogger.log("DEBUG ....!!")


if __name__ == "__main__":
    obj = Client()
    obj.getLogger()