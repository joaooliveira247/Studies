const brazilianStates = ["Rio de Janeiro", "São Paulo", "Minas Gerais", "Bahia", "Ceará"];

brazilianStates.pop(); // last element

console.log(brazilianStates);

brazilianStates.shift(); // first element

console.log(brazilianStates);

brazilianStates.push("Teste"); // end of array

brazilianStates.unshift("Teste"); // start of array


const newStates = brazilianStates.splice(0, 2, "more 1", "more 2", "more 3");

console.log(brazilianStates);