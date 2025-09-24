public class Main {
    public static void main(String[] args) {
        ILogger debugLogger = LoggerFactory.createLogger(LogLevel.DEBUG);
        ILogger errorLogger = LoggerFactory.createLogger(LogLevel.ERROR);
        ILogger infoLogger = LoggerFactory.createLogger(LogLevel.INFO);

        debugLogger.log("THIS IS DEBUG!!!!");
        errorLogger.log("THIS IS ERROR!!");
        infoLogger.log("THIS is INFO!!!");
    }
}