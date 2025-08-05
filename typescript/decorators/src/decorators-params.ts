function Logger(prefix: string) {
    return function <T extends { new (...args: any[]): {} }>(constructor: T) {
        return class extends constructor {
            constructor(...args: any[]) {
                super(...args);
                console.log(
                    `${prefix} - Instância criada de:`,
                    constructor.name
                );
            }
        };
    };
}

@Logger("INFO")
class User {
    constructor(public name: string) {}
}

const user = new User("João");
