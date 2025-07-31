const numbers = [1, 2, 3, 4];

// falsy
console.log(false ? "truthy" : "falsy");
console.log(0 ? "truthy" : "falsy");
console.log("" ? "truthy" : "falsy");
console.log(null ? "truthy" : "falsy");
console.log(undefined ? "truthy" : "falsy");
console.log(NaN ? "truthy" : "falsy");

// truthy
console.log(true ? "truthy" : "falsy");
console.log(-1 ? "truthy" : "falsy");
console.log(" " ? "truthy" : "falsy");
console.log([] ? "truthy" : "falsy");
console.log({} ? "truthy" : "falsy");
