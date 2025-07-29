// let logType = "info";
// logType = "warn";

// let logType: "info";

type LogType = "info" | "warn" | "error";

export function logger(type: LogType, message: string): void {
    switch (type) {
        case "info":
            console.log(`Info: ${message}`);
            break;
        case "warn":
            console.warn(`Warn: ${message}`);
            break;
        case "error":
            console.error(`Error: ${message}`);
            break;
    }
}

logger("warn", "some message");
