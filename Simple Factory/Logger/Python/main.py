from LoggerFactory import LoggerFactory
from LogLevel import LogLevel
class Main:
    @staticmethod
    def start():
        errorLogger = LoggerFactory.createLogger(LogLevel.ERROR)
        debugLogger = LoggerFactory.createLogger(LogLevel.DEBUG)
        infoLogger = LoggerFactory.createLogger(LogLevel.INFO)

        errorLogger.log("THIS IS error LOG")
        debugLogger.log("Debug logger!")
        infoLogger.log("INFO LOgger >>>>")


if __name__ == "__main__":
    Main.start()