const users = [
    {name: "John", age: 32},
    {name: "Peter", age: 16},
    {name: "Mariah", age: 40}
];

const validUsers = users.filter((currentValue) => currentValue.age >= 18);

console.log(validUsers);

const cars = [
    {name: "Gol", brand: "volkswagem"},
    {name: "iX35", brand: "hyundai"},
    {name: "Santa Fé", brand: "hyundai"},
    {name: "Polo", brand: "volkswagem"},
];

const validCars = cars.filter((currentValue) => currentValue.brand == "hyundai");

console.log(validCars)