const productFactory = function(productName, price){
    return {productName, price};
}

let notebook = productFactory("Notebook", 2100);
let smartTv = productFactory("SmartTV", 3400);

console.log(notebook, smartTv)

