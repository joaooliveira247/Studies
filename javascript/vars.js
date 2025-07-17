// var: tem escopo de função e é içado (hoisting), permite reatribuição e redeclaração.
var x = 1;

// let: tem escopo de bloco, permite reatribuição, mas não redeclaração no mesmo escopo.(mutavel)
let lastName = "Silva";

// const: escopo de bloco, **não permite reatribuição**, nem redeclaração.(imutavel)
const PI_VALUE = Math.PI;

console.log(`Number: ${x}, Last Name: ${lastName} & PI: ${PI_VALUE}`)
