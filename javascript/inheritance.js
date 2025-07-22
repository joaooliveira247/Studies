class Animal {
    constructor(color, size, weight) {
        this.color = color;
        this.size = size;
        this.weight = weight;
    }

    run() {
        return "Animal is running";
    }

    sleep() {
        return "Animal is sleeping";
    }
}

class Dog extends Animal{
    bark() {
        return "Dog is Barking";
    }
}

class Bird extends Animal{
    constructor(feather) {
        super()
        this.feather = feather
    }
    fly() {
        return "Bird is flying";
    }
}

class Parrot extends Bird {
    fly() {
        return `${super.fly} like a Parrot.`
    }
    talk() {
        return "Parrot is talking";
    }
}