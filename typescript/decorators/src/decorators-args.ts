function UppercaseFirstParam(
    target: any,
    propertyKey: string,
    descriptor: PropertyDescriptor
) {
    const originalMethod = descriptor.value;

    descriptor.value = function (...args: any[]) {
        if (args.length > 0 && typeof args[0] === "string") {
            console.log(`🎯 Alterando parâmetro original: "${args[0]}"`);
            args[0] = args[0].toUpperCase();
        }
        return originalMethod.apply(this, args);
    };

    return descriptor;
}

class Greeter2 {
    @UppercaseFirstParam
    greet(name: string, punctuation: string) {
        console.log(`Olá, ${name}${punctuation}`);
    }
}

const g = new Greeter2();
g.greet("john", "!");
