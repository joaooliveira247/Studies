const nums = [2, 3, 5];

const func = function(total, currentValue,) {
    // console.log(total);
    return total + currentValue;
};

const result = nums.reduce(func);
console.log(result);


const cart = [
    {productName: "Notebook", price: 2500},
    {productName: "Smartphone", price: 1600},
    {productName: "TV", price: 3600},
];

const total = cart.reduce((total, currentValue) => total + currentValue.price, 0);
console.log(total);

const users = [
    "John", "Peter", "Mariah",
];

let htmlUsers = users.reduce((total, currentValue) => total += `<li>${currentValue}</li>`,"");
console.log(htmlUsers);