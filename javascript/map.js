const people = ["John", "Peter", "Anna"];

const formatedPeople = people.map(currentValue => `Hello ${currentValue}`);

console.log(formatedPeople);

const dollarProducts = [
    {product: "Notebook", price: 1200}, { product: "SmartPhone", price: 800}
]

const newProducts = dollarProducts.map(currentValue => ({product: currentValue.product, price: currentValue.price * 5}));

console.log(newProducts)