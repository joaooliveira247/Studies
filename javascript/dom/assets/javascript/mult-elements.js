const obj = document.getElementsByTagName('li');
console.log(obj[0], obj[1]);

const arr = Array.from(obj);

console.log(arr);

arr.forEach((item) => console.log(item));

const objClass = document.getElementsByClassName('container');

const arrDiv = Array.from(objClass);

console.log(arrDiv);