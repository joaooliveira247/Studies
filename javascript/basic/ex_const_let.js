const fullName = "SomeOne";

const age = 31;

const weight = 80.0;

const height = 1.8;

let imc = weight / Math.pow(height, 2);

console.log(
  `${fullName} is ${age}, weight ${weight} KG, height ${height} and your IMC is ${imc.toFixed(
    1
  )}`
);
