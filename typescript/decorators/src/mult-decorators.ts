function LogExecution(
    target: any,
    propertyKey: string,
    descriptor: PropertyDescriptor
) {
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
        console.log(`Executando ${propertyKey} com args:`, args);
        return original.apply(this, args);
    };
}

function MultiplyResultByTwo(
    target: any,
    propertyKey: string,
    descriptor: PropertyDescriptor
) {
    const original = descriptor.value;
    descriptor.value = function (...args: any[]) {
        const result = original.apply(this, args);
        return result * 2;
    };
}

class Calculator {
    @LogExecution
    @MultiplyResultByTwo
    sum(a: number, b: number) {
        return a + b;
    }
}

const calc = new Calculator();
console.log("Resultado:", calc.sum(2, 3));
