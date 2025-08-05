// Using prototype
/*
type ConstructorFunction = { new (...args: any[]): {} };

function AddLogMethod<T extends ConstructorFunction>(constructor: T): void {
    console.log("It's from decorator");

    constructor.prototype.loggerInfo = function () {
        console.log(
            `${new Date().toLocaleString("pt-BR")} - ${JSON.stringify(this)}`
        );
    };
}

@AddLogMethod
class Product {
    name: string;
    loggerInfo!: () => void;

    constructor(name: string) {
        this.name = name;
    }
}

@AddLogMethod
class Person {
    name: string;
    age: number;
    loggerInfo!: () => void;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

const product = new Product("Smartphone");
product.loggerInfo();

const p1 = new Person("John", 21);
p1.loggerInfo();
*/

type ConstructorFunction = { new (...args: any[]): {} };

function AddLogMethod<T extends ConstructorFunction>(constructor: T): T {
    console.log("It's from decorator");
    return class extends constructor {
        loggerInfo = () => {
            console.log(
                `${new Date().toLocaleString("pt-BR")} - ${JSON.stringify(
                    this
                )}`
            );
        };
    };
}

@AddLogMethod
class Product {
    name: string;
    loggerInfo!: () => void;
    constructor(name: string) {
        this.name = name;
    }
}

@AddLogMethod
class Person {
    name: string;
    age: number;
    loggerInfo!: () => void;
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
}

const product = new Product("Smartphone");
product.loggerInfo();

const p1 = new Person("John", 21);
p1.loggerInfo();
