import "reflect-metadata";

const uppercaseParamsMetadataKey = Symbol("uppercaseParams");

function UppercaseParam(
    target: any,
    propertyKey: string,
    parameterIndex: number
) {
    const existingParams: number[] =
        Reflect.getOwnMetadata(
            uppercaseParamsMetadataKey,
            target,
            propertyKey
        ) || [];
    existingParams.push(parameterIndex);
    Reflect.defineMetadata(
        uppercaseParamsMetadataKey,
        existingParams,
        target,
        propertyKey
    );
}

function ApplyParamTransforms(
    target: any,
    propertyKey: string,
    descriptor: PropertyDescriptor
) {
    const originalMethod = descriptor.value;

    descriptor.value = function (...args: any[]) {
        const uppercaseParams: number[] =
            Reflect.getOwnMetadata(
                uppercaseParamsMetadataKey,
                target,
                propertyKey
            ) || [];

        uppercaseParams.forEach((index) => {
            if (typeof args[index] === "string") {
                args[index] = args[index].toUpperCase();
            }
        });

        return originalMethod.apply(this, args);
    };
}

class Greeter {
    @ApplyParamTransforms
    greet(@UppercaseParam name: string, punctuation: string) {
        console.log(`Olá, ${name}${punctuation}`);
    }
}

const g = new Greeter();
g.greet("john", "!");
