enum LoggerType {
    INFO = "info",
    WARN = "warn",
    ERROR = "ERROR",
}

class Logger {
    public static info(message: string): void {
        console.log(`INFO: ${message}`);
    }
    protected static warnning(message: string): void {
        console.log(`WARN: ${message}`);
    }
    private static error(message: string): void {
        console.log(`Error: ${message}`);
    }

    public static wrapperLogger(type: LoggerType, message: string): void {
        const msg: string = `[${Date.now()}] ${message}`;
        switch (type) {
            case LoggerType.INFO:
                Logger.info(msg);
                break;
            case LoggerType.WARN:
                Logger.warnning(msg);
                break;
            case LoggerType.ERROR:
                Logger.error(msg);
                break;
        }
    }
}
