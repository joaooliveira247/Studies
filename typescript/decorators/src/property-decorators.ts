function UppercaseProperty(target: any, propertyKey: string) {
    let value: string;

    const getter = function () {
        return value;
    };

    const setter = function (newValue: string) {
        console.log(
            `🎯 Alterando valor da propriedade "${propertyKey}":`,
            newValue
        );
        value =
            typeof newValue === "string" ? newValue.toUpperCase() : newValue;
    };

    Object.defineProperty(target, propertyKey, {
        get: getter,
        set: setter,
        enumerable: true,
        configurable: true,
    });
}

class User2 {
    @UppercaseProperty
    name: string;

    constructor(name: string) {
        this.name = name;
    }
}

const u = new User2("john");
console.log(u.name);

u.name = "maria";
console.log(u.name);
