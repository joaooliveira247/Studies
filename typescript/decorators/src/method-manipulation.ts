function LogAndModifyResult(
    target: any,
    propertyKey: string,
    descriptor: PropertyDescriptor
) {
    const originalMethod = descriptor.value;

    descriptor.value = function (...args: any[]) {
        console.log(`➡️ Chamando ${propertyKey} com args:`, args);

        const result = originalMethod.apply(this, args);

        console.log(`⬅️ ${propertyKey} retornou:`, result);

        if (typeof result === "string") {
            return result.toUpperCase();
        }

        return result;
    };

    return descriptor;
}

class Greeter {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    @LogAndModifyResult
    greet(greeting: string): string {
        return `${greeting}, ${this.name}`;
    }
}

const greeter = new Greeter("John");
const message = greeter.greet("Hello");
console.log("Mensagem final:", message);
