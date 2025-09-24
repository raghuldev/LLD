from DebugLogger import DebugLogger
from ErrorLogger import ErrorLogger
from InfoLogger import InfoLogger
from LogLevel import LogLevel
from ILogger import ILogger
class LoggerFactory:
    @staticmethod
    def createLogger(logLevel: LogLevel) -> ILogger | None:
        match logLevel:
            case "DEBUG":
                return DebugLogger()
            case "ERROR":
                return ErrorLogger()
            case "INFO":
                return InfoLogger()
            case _:
                return None
            
