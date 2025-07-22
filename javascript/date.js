const date = new Date();

console.log(date.toString());
console.log(date.toJSON());
date.setDate(date.getDate() + 720)
console.log(date.toJSON())