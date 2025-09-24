public class LoggerFactory {
    public static ILogger createLogger(LogLevel logLevel) {
        switch(logLevel) {
            case DEBUG:
                return new DebugLogger();
            case ERROR:
                return new ErrorLogger();
            case INFO:
                return new InfoLogger();
            default:
                return null;

        }
    }
}