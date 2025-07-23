const fruits = ["Strawberry", "Apple", "Avocado", "Banana", "Orange"];

const showItens = function(currentValue, index){
    console.log(`${index + 1}. ${currentValue}`);
}

fruits.forEach(showItens);

fruits.forEach((currentValue, index) => console.log(`${index + 1}. ${currentValue}`));

Array.prototype.showItens = function() {
    for (let i = 0; i < this.length; i++) {
        console.log(this[i]);
    }
}

fruits.showItens();