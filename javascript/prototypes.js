/*
const obj = {

};

console.log( obj.toString() );
console.log( obj.__proto__  == Object.prototype);
*/

class Car {
    constructor() {
        this.sign = "AMP-1230";
    }
}

class BMW extends Car {
    constructor() {
        super()
        this.name = "BMW 320i"
    }
}

const car = {
    sign: "AMP-1230",
}

const bmw = {
    name: "BMW 320i",
    __proto__: car
}

console.log(bmw.sign)