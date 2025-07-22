const product = {
    productName: "Notebook",
}

Object.freeze( product );
product.productName = "Cellphone";
console.log(product);